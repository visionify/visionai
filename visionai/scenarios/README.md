# VisionAI Scenarios

This repo consists of all the scenarios supported by the [Vision AI Toolkit](https://github.com/visionify/visionai). Main file is `scenarios.json` which is one large JSON file with all scenarios, categories, tags etc.

TODO: Later we would like to add some automation in terms of easily being able to add scenarios from our model experiements folder.

## Schema

The JSON file is organized as an array of scenarios. Each scenario can have all the details related to it, including name, category, tags, model_file locations, training & accuracy details, versions etc. This file lists all publicly available scenarios. Each scenario has the schema:

```json
{
    "id": "5991c1bb-be6a-4f60-99a2-3db1973c96ad",
    "name": "smoke-and-fire-detection",
    "version": "0.0.2",
    "overview": "Detect early signs of sparks, smoke or fire. Get real-time events when a smoke, fire, sparks, embers are detected. It is trained with 240032 images, out of which 183453 images were from outdoors environment, and remaining images were indoor environment. There is a good balance between day and night pictures (44-56%)",
    "docs": "https://docs.visionify.ai/scenarios/smoke-and-fire-detection.md",
    "image": "https://scenariosblob.blob.core.windows.net/scenarios-smoke-and-fire-description.jpg",
    "thumbnail": "https://scenariosblob.blob.core.windows.net/scenarios-smoke-and-fire-description-200x200.jpg",
    "models": {
        "latest": {
            "version": "0.1.1",
            "name": "yolov5-small-based",
            "accuracy": 98.2,
            "recall": 95.2,
            "f1": 95,
            "datasetSize": 240032,
            "model_url": "https://workplaceos.blob.core.windows.net/models/smoke-and-fire-detection/smoke-and-fire-detection-0.0.1.zip",
            "model_hash": "35285fefb794bb175f10aa7468a69c5d"
        },
        "other": [
            {
                "version": "0.1.0",
                "name": "yolov5-medium",
                "accuracy": 98.2,
                "recall": 95.2,
                "f1": 95,
                "datasetSize": 240032,
                "model_url": "https://workplaceos.blob.core.windows.net/models/smoke-and-fire-detection/smoke-and-fire-detection-0.0.1.zip",
                "model_hash": "35285fefb794bb175f10aa7468a69c5d"
            },
            {
                "version": "0.1.0",
                "name": "yolov5-large",
                "accuracy": 98.2,
                "recall": 95.2,
                "f1": 95,
                "datasetSize": 240032,
                "model_url": "https://workplaceos.blob.core.windows.net/models/smoke-and-fire-detection/smoke-and-fire-detection-0.0.1.pt",
                "model_hash": "35285fefb794bb175f10aa7468a69c5d"
            }
        ]
    },
    "tags": [
        "Smoke",
        "Fire",
        "Sparks",
        "Embers",
        "Early Fire Signature",
        "Hazard warning"
    ],
    "categories": [
        "Personnel health",
        "Hazard warning"
    ],
    "events": [
        "Smoke Detected",
        "Fire Detected"
    ],
    "configuration": [
        {
            "name": "focus_area",
            "type": "region_of_interest",
            "required": false,
            "default": [
                0,
                0,
                1,
                1
            ]
        }
    ]
}
```


## Why a giant JSON file?

We thought about controlling this information through a DB/redis approach, but the problem was a good version control availability. With a JSON file, the size can increase and make it unreadable - but it would provide much better version control. Later we plan to add to add more tools that would make it easier to get just individual scenarios, scenarios by categories etc. All of these would be auto-generated files based on a single-source-of-truth.

## How to add and test a new scenario

- Create a new model using traditional means. Once the model is created, you can use the methods below to add this as a scenario.


## Testing the model with Triton Server

You need to test your model with Triton server. More information about Triton Server is available [here](https://github.com/triton-inference-server).

1. Pull the Docker image for triton

```bash
docker pull nvcr.io/nvidia/tritonserver:22.12-py3
```

2. Create a model repository with your model.

```
$ mkdir model-repo
$ cp yolov5s-face/ model-repo/yolov5s-face/  # Copy your model
$ cd model-repo
$ tree
.
├── 1
│   └── model.onnx
├── config.pbtxt
└── labels.txt
```

3. Start triton server with this model repo

```bash
docker run --gpus=1 --rm --net=host -v /workspace/harsh-env/edge-inference/models-repo:/models nvcr.io/nvidia/tritonserver:22.12-py3 tritonserver --model-repository=/models
```

Make sure that the triton server comes up and stays up. If there is any error - it would just exit. Following should be the output.

```bash
+--------------------------+---------+--------+
| Model                    | Version | Status |
+--------------------------+---------+--------+
| yolov5s-small            | 1       | READY  |
+--------------------------+---------+--------+

I0127 07:04:03.443093 1 grpc_server.cc:4819] Started GRPCInferenceService at 0.0.0.0:8001
I0127 07:04:03.443328 1 http_server.cc:3477] Started HTTPService at 0.0.0.0:8000
I0127 07:04:03.485587 1 http_server.cc:184] Started Metrics Service at 0.0.0.0:8002

```

4. Test out the model. You can use yolov5 detect.py method with triton url. Instead of providing weights file, you can provide the URL for triton (both HTTP or GRPC endpoints can be provided). Once the model looks good - then you can go to next steps to upload the model.

```
python3 detect.py --weights http://localhost:8000
```

## Upload the model to the cloud

- Once the final models weight file is available - upload it to the cloud.

We will be using Triton Server to serve the models. While uploading models, need to make sure that they follow the Triton Server recommended format for the models.

- For now - let's stick with ONNX format. Export onnx model from your model by using the following command:

```bash
    python export.py --include onnx weights.pt
```

- Sometimes it may throw an error that Opset version is not supported. In such cases, specify `--opset 15` to the above option. Or try `--opset 14` or `--opset 13` if that does not work.

- Note down the model output sizes created. This is dependent on the number of classes. For example: PyTorch: starting from yolov5s.pt with output shape (1, 25200, 14) (14.1 MB). To find the input and output shape of the model file, open [https://netron.app](https://netron.app) and upload your model there. Note down the input and out sizes for your model, along with input and output tensor names.

- Create a config.pbtxt for the model. It shouls look like this. Use the input and output tensorname, and sizes that you find from [netron.app](https://netron.app).

```yaml
    name: "ppe-detection"
    platform: "onnxruntime_onnx"
    max_batch_size: 0
    input [
        {
            name: "images"
            data_type: TYPE_FP32
            dims: [1, 3, 640, 640 ]
        }
        ]
        output [
        {
            name: "output0"
            data_type: TYPE_FP32
            dims: [1, 25200, 14]
            label_filename: "labels.txt"
        }
    ]
```

- Create a `labels.txt` which contains all the labels for this model. If it's a yolov5 model - the labels would be in data.yaml file. Convert this into a `labels.txt` file which is a plain-text file with each line for a label.
- The folders should look like this:

```bash
$ tree
.
├── phone-detection
│   ├── 1
│   │   └── model.onnx
│   ├── config.pbtxt
│   └── labels.txt
├── ppe-detection
│   ├── 1
│   │   └── model.onnx
│   ├── config.pbtxt
│   └── labels.txt
├── rust-and-corrosion-detection
│   ├── 1
│   │   └── model.onnx
│   ├── config.pbtxt
│   └── labels.txt
├── smoke-and-fire-detection
│   ├── 1
│   │   └── model.onnx
│   ├── config.pbtxt
│   └── labels.txt
└── smoking-detection
    ├── 1
    │   └── model.onnx
    ├── config.pbtxt
    └── labels.txt

```

- Zip individual folders so we can upload them. For example:

```bash
zip phone-detection.zip -r phone-detection/
```

- Run this command to upload to the cloud.

```bash
python upload_model.py upload --model smoke-and-fire-detection --version 0.0.3 --file model-files.zip
```

- Note down the URL for the uploaded model.

- Checkout `visionai` repo. Create a new branch with your changes.

```bash
git clone git@github.com:visionify/visionai.git
cd visionai
git checkout -b smoke-and-fire-detection-dev
```

- Make changes to the `scenairos.json`. If this is a new scenario, add an entire scenario element into the the file. If it is just updating a model file, change just the URL and hash for it.

## Inference code

The inference code for each scenario is organized in a similar manner. This is to make sure the calling function for it (be it Web-APIs or CLIs), have a single mechanism to call this function. As such the structure of the file, and the naming conventions here are to be strictly followed.

---
| What              | How it should be named       | Explanation                                          |
| :---------------- | :----------------------------| :--------------------------------------------------- |
| `scenario`        | `smoke-and-fire-detection`   | The end use scenario name (same in `scenarios.json`) |
| `filename`        | `smoke_and_fire_detection.py`| The file name implementing this scenario             |
| `class_name`      | `SmokeAndFireDetection`      | The class implementing this scenario                 |
---

The implementation file should look like this:

```python

from util.general import LOGGER
from scenarios import Scenario
from events.events_engine import EventsEngine()
from config import TRITON_HTTP_URL

class SmokeAndFireDetection(Scenario):
    def __init__(self, scenario_name='smoke-and-fire-detection', camera_name=0, events=None, triton_url=TRITON_HTTP_URL):

        from models.triton_client_yolov5 import yolov5_triton
        # write model name for your scenario (from scenario.json)
        model_name = 'smoke-and-fire-detection'
        self.model = yolov5_triton(triton_url, model_name)
        super().__init__(scenario_name, camera_name, events, triton_url)

        self.eventsEngine = EventsEngine()

    def start(self, camera=0):
        '''
        Start processing the stream.

        The camera name parameter would include the name to the camera instance.
        It can be either 0 indicating web-cam, or 'OFFICE-01' indicating a named
        camera instance.
        '''

        import cv2

        cam = get_camera_stream(camera)
        video = cv2.VideoCapture(cam)

        while True:
            # Do processing
            ret, frame = video.read()
            if ret is False:
                LOGGER.error('ERROR: reading from video frame')
                time.sleep(1)
                continue

            # Detect smoke & fire
            results = self.model(frame, size=640)

            # Do some processing with the events.
            # Fire an event when detected.
            if is_smoke_or_fire_detected(results):
                self.eventsEngine.fire_event(
                    Event.CRITICAL,
                    camera,
                    'people-taking-picture-detection',
                    'TAKING_PICTURE',
                    events_data={})

            # Show the results on screen if needed.
            results.show()

            # if result contains people but PPE are not detected - then fire an event.
            # For now fire-an-event == print the event details.

            # if stop_evt is set, then break
            if self.stop_evt.is_set():
                break

```


- Test the new `scenarios.json` is working correctly with VisionAI executable. To do this, we need to do this. Because the new `scenarios.json` is not available in main repository yet - we cannot test out fully. So do this workaround to test it out.

```bash
cp visionai/scenarios/scenarios.json visionai/config/scenarios-override.json
```

- Test your changes with:
```bash
visionai scenarios test smoke-and-fire-detection
```

- You should be able to see a web-cam being opened on your machine and the scenarios are run on top of that. Monitor the events being fired are correct. Once this is validated - you can push the changes.

- Commit and push the changes, and create a new PR.

```bash
git add .
git commit
<add commit message and clearly explain what we are adding>
create a new PR
```

