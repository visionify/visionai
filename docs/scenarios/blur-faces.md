# **Face blur** 

> Ensure the privacy of individuals in public spaces

![Face blur by custom model](../img/faceblur_collage.png)

## Overview

Face blurring is a privacy model which is becoming increasingly popular in the digital age. It involves the use of technology to blur or obscure the facial features of individuals in digital images and videos. This technology can be used to protect the identity of individuals in images.

The concept of face blurring is based on the idea that a person’s identity should remain private, and that images of a person should not be shared without their consent. In a world where people are increasingly sharing images and videos of themselves and others, face blurring is becoming a necessary tool to protect people’s privacy. This technology can be used to blur the faces of individuals in images, or even to remove them entirely.

The face blurring technology is designed to be easy to use and understand. It can be used on both still images and videos, and can be applied in a matter of seconds with just a few clicks. It is also fairly simple to configure and requires no technical expertise. The user simply choose the image or video that they want to blur and the algorithm will automatically detect and blur the faces.


## Vision AI-based monitoring 

Vision AI-based Model for Face Blurring is designed to ensure that the privacy of individuals is respected while still allowing the public to have access to the video feed.

This model uses a combination of facial recognition algorithms and image processing techniques to automatically blur faces in real-time video streams. The system is designed to detect faces in real-time, and then blur them out so that they are not recognizable. This model has been used in various applications including public surveillance, online video streaming, and social media platforms.

### Dataset 

WIDER FACE dataset is a face detection benchmark dataset, of which images are selected from the publicly available WIDER dataset. WIDER FACE dataset is organized based on 61 event classes. For each event class, we randomly select 40%/10%/50% data as training, validation and testing sets. 
The dataset contains faces with:

- Variant illumination scene images
- Multiple face expressions
- Different lighting conditions
- Variations in scale, pose and occlusion

Total number of mages used was 32,203


### Model 

The model is based off of the YOLOv5-face algorithm. The model is trained on WIDER FACE dataset. We intend to develop a model that generalizes well in real world situations. Implemented a custom logic for face blurring with the help of face detections from yolo face.

The model recorded the following performance metrics:

<div class="table">
    <table class="fl-table">
        <thead>
        <tr><th>Model Name</th>
            <th>Easy</th>
            <th>Medium</th>
            <th> Hard</th>  
        </thead>
        <tbody>
        <tr>
            <td>FACE BLUR</td>
            <td>95.3% </td>
            <td>93.7% </td>
            <td>85.2% </td>
        </tr>
        </tbody>
    </table>
</div>



The model is adaptable enough to run on any edge computing device.


### Scenario details

The business logic for this scenario is as follows: 

- We use existing camera feeds from the premises to Ensure the privacy of individuals.
- VisionAI system is able to run on edge devices. It uses camera feeds for processing. 
- We detect and blur the faces identified in this camera feed.


## Try it now

### Quick method - using your local web-cam

To test this model & scenario, you can use the following steps:

- Install the visionai package from PyPI

<div class=termy>

```console

$ pip install visionai
---> 100%
```
</div>

- Test the scenario from your local web-cam

<div class=termy>

```console
$ visionai scenario test face-blur

Downloading models for scenario: face-blur
Model: face-blur: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
---> 100%

Starting scenario: face-blur..

```
</div>


### In an actual environment


To use this scenario in an actual environment, you can follow these steps:

- Install the visionai package from PyPI

<div class=termy>

```console
$ pip install visionai
---> 100%
```
</div>

- Download the scenario

<div class=termy>

```console
$ visionai scenario download face-blur

Downloading models for scenario: face-blur
Model: face-blur
https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
---> 100%
```

</div>

- Add the camera feed to the scenario

<div class=termy>

```console
$ visionai camera add OFFICE-01 --url rtsp://192.168.0.1/stream1
$ visionai camera OFFICE-01 add-scenario face-blur
$ visionai run

Starting scenario: face-blur..

```

</div>


For more details visit VisionAI [web application](https://visionify.ai/).



## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please (contact us)[contact.md].


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).