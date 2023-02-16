from util.general import check_requirements

def opencv_stream():
    check_requirements(['opencv-python', 'imutils'])

    import cv2
    import time
    from imutils.video import WebcamVideoStream

    rtsp_url = "rtsp://username:password@ip_address:port_number/stream_name"
    fourcc = cv2.VideoWriter_fourcc(*"H264")

    src = 0 # 0 for the default camera
    vs = WebcamVideoStream(src).start()
    time.sleep(2.0) # Wait for the camera to warm up

    out = cv2.VideoWriter(rtsp_url, fourcc, 10, (640, 480), True)

    while True:
        frame = vs.read()
        out.write(frame)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    out.release()
    vs.stop()
    cv2.destroyAllWindows()
