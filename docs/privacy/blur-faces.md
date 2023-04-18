# **Face Blur** 

> Ensure the privacy of individuals in public spaces
<figure markdown>
  ![Face blur](https://github.com/visionify/visionai-images/raw/main/visionai-images/faceblur_collage.png"Face blur!"){width="400"}
  <figcaption>Face blur as part of preprocessing</figcaption>
</figure>


## Overview

Face blurring is a privacy model which is becoming increasingly popular in the digital age. It involves the use of technology to blur or obscure the facial features of individuals in digital images and videos. This technology can be used to protect the identity of individuals in images.

The concept of face blurring is based on the idea that a person’s identity should remain private, and that images of a person should not be shared without their consent. In a world where people are increasingly sharing images and videos of themselves and others, face blurring is becoming a necessary tool to protect people’s privacy. This technology can be used to blur the faces of individuals in images, or even to remove them entirely.

The face blurring technology is designed to be easy to use and understand. It can be used on both still images and videos, and can be applied in a matter of seconds with just a few clicks. It is also fairly simple to configure and requires no technical expertise. The user simply choose the image or video that they want to blur and the algorithm will automatically detect and blur the faces.


## Vision AI-based monitoring 

Vision AI-based Model for Face Blurring is designed to ensure that the privacy of individuals is respected while still allowing the public to have access to the video feed.

This model uses a combination of facial recognition algorithms and image processing techniques to automatically blur faces in real-time video streams. The system is designed to detect faces in real-time, and then blur them out so that they are not recognizable. This model has been used in various applications including public surveillance, online video streaming, and social media platforms.

## Model Details

### Dataset

WIDER FACE dataset is a face detection benchmark dataset, of which images are selected from the publicly available WIDER dataset. WIDER FACE dataset is organized based on 61 event classes. For each event class, we randomly select 40%/10%/50% data as training, validation and testing sets. 
The dataset contains faces with:

- Variant illumination scene images
- Multiple face expressions
- Different lighting conditions
- Variations in scale, pose and occlusion



### Model 

The model is based off of the YOLOv5-face algorithm. The model is trained on WIDER FACE dataset. We intend to develop a model that generalizes well in real world situations. Implemented a custom logic for face blurring with the help of face detections from yolo face.

### Model card

 <div class="table">
    <table class="fl-table">
        <thead>
        <tr><th>Dataset size</th>
            <th>Version</th>
            <th>Camera support</th>
            <th>Precision</th>
            <th>Recall</th>
            <th> mAP  </th>  
        </thead>
        <tbody>
        <tr>
            <td>32,203</td>
            <td>v1</td>
            <td>Both(Ceiling or Straight cameras)</td>
            <td>95% </td>
            <td>93% </td>
            <td>85% </td>
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

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test face-blur

        Downloading models for scenario: face-blur
        Model: face-blur: https://workplaceos.blob.core.windows.net/models/yolov5s-face-blur/yolov5s-face-blur-0.0.1.zip
        

        Starting scenario: face-blur..

        ```
    - You should be able to see faces being blurred as part of preprocessing.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)



## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).

## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).