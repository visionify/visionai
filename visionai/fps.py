import time


class FPS(object):
    def __init__(self):
        self._start_time = time.time()
        self._cur_time = time.time()
        self._frame_idx = 0

    def update(self):
        self._cur_time = time.time()
        self._frame_idx += 1

    def get(self):
        return round(self._frame_idx/(time.time() - self._start_time), 2)

    def reset(self):
        self._start_time = time.time()
        self._cur_time = time.time()
        self._frame_idx = 0

    def start(self):
        self.reset()
        return self
