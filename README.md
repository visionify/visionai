# visionai
VisionAI open-source library

## Overview
Goal of this library is to create a easy-to-use Computer Vision inference library that can be used on all platforms without compromising performance.

## #BuildInPublic
This is the first project I am building using #BuildInPublic paradigm, and I am really looking forward to get your feedback. This also means that the project is not production-ready. I am pushing all my changes to main branch directly. I am breaking backward compatibility recklessly. Please be careful while using this code for any production deployment!

## What is the end goal?
The end goal is to have an easy-to-use, performant edge inference library that would run similarly on:
- Different Operating Systems (Linux/Windows/Mac)
- Different Compute Architectures (Intel/ARM64)
- Different GPU Combinations (CPU only vs. GPU enabled)

## Example Use-cases
### Installing & using this library
- Using this library should be as simple using any other Python package.
- [This is still WIP] 
```python
# Install visionai library
pip install visionai

# Detect objects using visionai
objectDetector = visionai.ObjectDetector('SSD-Mobilenet-v2')
objects = objectDetector.detect(image)
```

### Camera Input
- Single interface for opening any type of Cameras.
```python
camera = visionai.Camera('/dev/video0')
or 
camera = visionai.Camera('rtsp://admin:12345@localhost:8000')
or
camera = visionai.Camera('https://youtube.com/kj89238mla1')
```
- IMO, the library should internally figure out whether the camera is USB or RTSP or CSI or a media file & open it accordingly.

### Object Detection
- Simple interface for detecting object based on any type of models.
```python
objectDetector = visionai.ObjectDetector('SSD-Mobilenet-v2')
objects = objectDetector.detect(image)
``` 

### Classification
- Simple interface for classifying an image based on any type of model.
```python
classDetector = visionai.Classification()
classes = classDetector.classify(image)
```

### Video Streamer
- TODO.

### Object Tracker
- Sometimes we need a mechanism to track different objects after they are detected.
- TODO: Add details about how to use it.

### Markup
- Easy set of utilities for marking up an image with different meta data.
- Many times we want to write simple text like FPS, or objects detected or even simpler things like datetime on the image frame. This class will provide utility methods to provide that information.

### Video Streamer
- A lot of devices I work with are headless. They are deployed in an environment without a direct monitor connected. It is hard to debug what's happening without looking at the video frames coming from the device.
- Goal is to be able to stream from the local device to a web-server easily. Maybe we can make web-server SaaS for ease of access. Also provide open-source web-streamer code for individual developer testing. 

### Model
- TODO

### Stats
- Maybe add prometheus stats?

### Logger
- Does this belong here?
