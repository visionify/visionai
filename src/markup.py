import cv2

class Markup:
    @classmethod
    def markup_fps(cls, frame, fps):
        fps = str(fps)
        cv2.putText(frame, 'FPS: {}'.format(fps), (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    @classmethod
    def top_left_text(cls, frame, text_arr):
        for idx, text in enumerate(text_arr):
            cv2.putText(frame, text, (20, 30 + idx*30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    @classmethod
    def bottom_left_text(cls, frame, text_arr):
        arr_len = len(text_arr)
        start_y = frame.shape[0] - arr_len * 30
        for idx, text in enumerate(text_arr):
            cv2.putText(frame, text, (20, start_y + idx*30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
