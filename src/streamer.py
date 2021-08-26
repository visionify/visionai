import os
import time
import argparse
import socketio
import cv2
import base64
import platform
from .fps import FPS

stream_server = os.environ.get('LIVE_STREAM_SERVER') or '0.0.0.0'
stream_port = os.environ.get('LIVE_STREAM_PORT') or 8000
device_id = str(platform.node()).lower().strip().replace('.', '-').replace('_', '-').replace(' ', '-')

class OpenCVStreamer(object):
    def __init__(self, server_addr=stream_server, server_port=stream_port, room_name=device_id):
        self._server_addr = server_addr
        self._server_port = server_port
        self._last_update_t = time.time()
        self._connected = False
        self._wait_t = 1/30 # Max is 30 FPS supported.
        self._room_name = room_name
        if self._room_name is None:
            self._room_name = device_id

        self.sio = socketio.Client()

        @self.sio.event
        def connect():
            print('[INFO] Successfully connected to server.')

        @self.sio.event
        def connect_error():
            print('[ERROR] Failed to connect to server.')

        @self.sio.event
        def disconnect():
            print('[INFO] Disconnected from server.')

    def __enter__(self):
        return self

    def connect(self):
        if self._connected is True:
            return True

        print('[INFO] Connecting to server http://{}:{}...'.format(self._server_addr, self._server_port))
        try:
            self.sio.connect(
                    'http://{}:{}'.format(self._server_addr, self._server_port),
                    transports=['websocket'],
                    namespaces=['/', '/cv'])

            self.sio.emit('join', {'room': self._room_name})
            self._connected = True
        except Exception as ex:
            print('ERROR: Unable to connect to server: http://{}:{}'.format(stream_server, stream_port))
            self._connected = False
        finally:
            return self._connected

    def _convert_image_to_jpeg(self, image):
        # Encode frame as jpeg
        frame = cv2.imencode('.jpg', image)[1].tobytes()
        # Encode frame in base64 representation and remove
        # utf-8 encoding
        frame = base64.b64encode(frame).decode('utf-8')
        return "data:image/jpeg;base64,{}".format(frame)

    def send_data(self, frame, text):
        cur_t = time.time()
        if cur_t - self._last_update_t > self._wait_t:
            self._last_update_t = cur_t
            frame = cv2.resize(frame, (int(frame.shape[1]/2), int(frame.shape[0]/2)))
            self.sio.emit('my_room_event', {
                'room': self._room_name,
                'data': {
                    'image': self._convert_image_to_jpeg(frame),
                    'text': text,
                    'device_id': device_id
                }})

    def stop(self):
        self.sio.disconnect()
        self._connected = False

    def check_exit(self):
        pass

    def __exit__(self, exc_type, exc_val, tb):
        ret = True
        if exc_type is not None:
            import traceback
            traceback.print_exception(exc_type, exc_val, tb)
            ret = False

        try:
            if self._connected is False:
                self.sio.disconnect()
        finally:
            return ret

def _test_open_cv_streamer(camera, server_addr, server_port, device_id):

    # Open streamer
    with OpenCVStreamer(server_addr, server_port, room_name=device_id) as streamer:
        # Connect streamer.
        streamer.connect()

        # Open video camera (using OpenCV).
        video = cv2.VideoCapture(camera)

        # Read frames & send to webstreamer
        fps = FPS()
        fps.start()
        while True:
            ret, frame = video.read()
            frame = cv2.flip(frame, 1)
            fps.update()

            fps_text = ['FPS: {}'.format(fps.get())]
            streamer.send_data(frame, fps_text)

            if streamer.check_exit():
                video.release()
                break

    print("Program Done.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Visionify Video Streamer')
    parser.add_argument(
            '--camera', type=int, default='0',
            help='The camera index to stream from.')
    parser.add_argument(
            '--server-addr',  type=str, default='0.0.0.0',
            help='The IP address or hostname of the SocketIO server.')
    parser.add_argument(
            '--server-port',  type=int, default=8000,
            help='The Port number for where this is hosted.')
    parser.add_argument(
            '--stream-fps',  type=float, default=30.0,
            help='The rate to send frames to the server.')
    parser.add_argument(
        '--device-id',  type=str, default=device_id,
        help='The IP address or hostname of the SocketIO server.')
    args = parser.parse_args()
    _test_open_cv_streamer(args.camera, args.server_addr, args.server_port, args.device_id)
