# **Ergonomics Monitoring**

> Ensure safety and comfort of employees by monitoring ergonomics. 

## Overview 
 Ergonomics is the study of designing and arranging products, systems, and environments to fit the capabilities and limitations of people, with the goal of improving efficiency, safety, and comfort. The primary focus of ergonomics is to create environments that optimize human performance and well-being.
## Vision AI based monitoring 

Vision AI based monitors can be used to monitor productivity and workers health by providing real-time video feeds of different areas. These cameras can be used to monitor and track number of objects moved by persons from one place to the other, as well as the bending information of workers while performing this work. 

Companies can put compliance policies in place to ensure that workers are made aware of work-related injuries and illnesses due to unnecessary bending.  

It is important to note that these camera-based monitoring provides should be supplanted by strong compliance processes to ensure their accuracy and reliability. In addition, workers working in companies should always be trained on ergonomics and its significance for safety and its impact on human health.


## Model Details 

 

### Dataset 

Model training is carried out with Microsoft COCO: Common Objects in Context dataset. Person and Book classes are considered for model building. Person class is considered here because the problem of ergonomics is related to pose estimation and the object used to show movement is the book. It is the object carried by a person from one location to the other. Other objects can be considered as per the requirement.  

Basically, COCO is a  large-scale dataset that addresses three core research problems in scene understanding: detecting non-iconic views (or non-canonical perspectives of objects, contextual reasoning between objects and the precise 2D localization of objects.  

The dataset is made up of a large number of images and it is curated to ensure a true  representation of the real world for: 

- Indoor vs Outdoor environments 

- Variations in time  

- Different types of clothing for persons 

- Different distances from the camera 

- Various lighting conditions 

- Various camera angles, resolutions and calibrations 

- Using security camera feeds 

 

### Model 

The Yolov5 pre-trained model for detecting person and book (an example of an item) classes are used to build the model. DenseNet is employed to estimate each person's landmarks. These landmarks are used to estimate poses. This is mostly used to track a person's bending motion. To guarantee the counting of boxes, object tracking using a strong sort algorithm is also built. 

This provides ergonomics data that may be utilised for a variety of tasks, such as alarm generation when the number of bends exceeds predetermined levels and productivity counting to determine how many objects were transported from one location to another. 

The DenseNet Model for Landmark detection provides the following metrics: 

|Accuracy |	Recall	|Precision	|
|---------|---------|-------|
|84.0%	  |72.8%    |84.9%  |

<div class="table">
    <table class="fl-table">
        <thead>
        <tr><th>Model Name</th>
            <th>Accuracy</th>
            <th>Recall</th>
            <th>Precision</th>  
        </thead>
        <tbody>
        <tr>
            <td>ERGONOMICS DETECTION</td>
            <td>84.0% </td>
            <td>72.8% </td>
            <td>84.9% </td>
        </tr>
        </tbody>
    </table>
</div>

 

The model is lightweight enough to be run on any edge device. 

### Scenario details 

 

The business logic for this scenario is as follows: 

- We use existing camera feeds from the premises to monitor the presence of workers. 

-  VisionAI system is able to run on edge devices. It uses camera feeds for processing. 

- We detect and track the number of objects transported and we monitor the total number of bending motions of a person while working.

 

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
$ visionai scenario test ergonomics-detection

Downloading models for scenario: ergonomics-detection
Model: ergonomics-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
---> 100%

Starting scenario: ergonomics-detection..

```
</div>


- You should be able to see the events generated on your console window with slip and fall being detected within the camera field of view.

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
$ visionai scenario download ergonomics-detection

Downloading models for scenario: ergonomics-detection
Model: ergonomics-detection
https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
---> 100%
```

</div>

- Add the camera feed to the scenario

<div class=termy>

```console
$ visionai camera add OFFICE-01 --url rtsp://192.168.0.1/stream1
$ visionai camera OFFICE-01 add-scenario ergonomics-detection
$ visionai run

Starting scenario: ergonomics-detection..

```

</div>

- You should be able to see the events generated on your console window with slip and fall being detected within the camera field of view.

For more details visit VisionAI [web application](https://visionify.ai/).


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please (contact us)[contact.md].


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).