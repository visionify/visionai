# Triton Server Instructions

- Download all folders to `models-repo` folder. This folder should look like this:

```console

$ tree

.
├── README.md
├── ppe-detection
│   ├── 1
│   │   └── model.onnx
│   ├── config.pbtxt
│   └── labels.txt
├── smoke-and-fire-detection
│   ├── 1
│   │   └── model.onnx
│   ├── config.pbtxt
│   └── labels.txt
└── yolov5s
    ├── 1
    │   └── model.onnx
    ├── config.pbtxt
    └── labels.txt

6 directories, 16 files

```

- Update the `config.pbtxt` file in each directory to include the output tensor size correctly. This would depend upon the number of classes were used for training. (I think it is num_classes + 5).

```bash
name: "smoke-and-fire-detection"
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
    dims: [1, 25200, 7]
    label_filename: "labels.txt"
  }
]

```


- Run triton server by using the latest docker image.

```bash
docker run --gpus=1 --rm --net=host -v /workspace/harsh-env/visionai/models-repo:/models nvcr.io/nvidia/tritonserver:22.12-py3 tritonserver --model-repository=/models
```

- You should see an output like this which indicates all models are getting served now:

```console
I0127 07:04:03.407110 1 server.cc:633]
+--------------------------+---------+--------+
| Model                    | Version | Status |
+--------------------------+---------+--------+
| ppe-detection            | 1       | READY  |
| smoke-and-fire-detection | 1       | READY  |
| yolov5s                  | 1       | READY  |
+--------------------------+---------+--------+

I0127 07:04:03.443093 1 grpc_server.cc:4819] Started GRPCInferenceService at 0.0.0.0:8001
I0127 07:04:03.443328 1 http_server.cc:3477] Started HTTPService at 0.0.0.0:8000
I0127 07:04:03.485587 1 http_server.cc:184] Started Metrics Service at 0.0.0.0:8002

```

 