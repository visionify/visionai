import os
import sys
from pathlib import Path

FILE = Path(__file__).resolve()
SCENARIOS = FILE.parents[0]
ROOT = FILE.parents[1]  # Root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

def yolov5_triton(url, model_name):

    from models.common import AutoShape, Yolov5Triton
    from util.general import LOGGER, check_requirements
    from util.image_utils import select_device

    device = select_device()
    LOGGER.info(f'Using {url} as Triton inference server. Model name {model_name}')
    check_requirements('tritonclient[all]', install=True)

    model = Yolov5Triton(url=url, model_name=model_name)
    model = AutoShape(model)    # Add nms, auto-scaling results
    return model.to(device)

if __name__ == '__main__':

    import cv2
    import numpy as np
    from PIL import Image
    from util.general import WorkingDirectory

    # Model
    model_smoke = yolov5_triton(url='http://localhost:8000', model_name='smoke-and-fire-detection')
    # model_ppe = yolov5_triton(url='http://localhost:8000', model_name='ppe-detection')
    # model_yolov5s = yolov5_triton(url='http://localhost:8000', model_name='yolov5s')

    # or use grpc
    # model = yolov5_triton(url='grpc://0.0.0.0:8001', model='ppe-detection')

    with WorkingDirectory(SCENARIOS):
        # Images
        imgs = [
            'data/images/zidane.jpg',  # filename
            Path('data/images/zidane.jpg'),  # Path
            'https://ultralytics.com/images/zidane.jpg',  # URI
            # cv2.imread('data/images/bus.jpg')[:, :, ::-1],  # OpenCV
            # Image.open('data/images/person-helmet.jpg'),  # PIL
            np.zeros((320, 640, 3))]  # numpy

        # Inference
        for idx, img in enumerate(imgs):
            results = model_smoke(img, size=640)  # batched inference
            results.print()
            results.show()
            # results.save()

            # results = model_ppe(img, size=640)  # batched inference
            # results.print()
            # results.save()

            # results = model_yolov5s(img, size=640)  # batched inference
            # results.print()
            # results.save()
