# **Firearms And Knives Detection**

> New Technology aims to improve Firearm Detection and Save Lives with VisionAI.

<figure markdown>
  ![Firearms And Knives Detection](https://github.com/visionify/visionai-images/raw/main/visionai-images/firearms-detection.png "Detection of firearms and knives at a work-place!"){ width="350" }
  <figcaption>Detection of firearms and knives event</figcaption>
</figure>

## Overview

Firearms detection refers to the use of technology and methods to identify the presence of firearms in a particular location or setting. The goal of firearms detection is to prevent violence and ensure public safety by detecting and responding to the presence of firearms including knives, guns and other weapons.

There are various methods and technologies used for firearms detection, including metal detectors, X-ray machines, and millimeter-wave scanners. All these solutions are invasive. 

With the advent in technology, our VisionAI solution for fire-arms detection is non-invasive in nature and it works by analyzing video footage to detect the presence of firearms or other weapons.

## Vision AI based monitoring

Vision AI based monitors can be used to detect Firearms and knives events by providing real-time video feeds of the factory area. The cameras scan every frame to ensure there is no sign of firearms and knives.


## Events

VisionAI model's generated events would be:

- Person brandishing firearm
- Person brandishing knives


## Camera Configuration

Recommended to set up camera in ceiling view to detect weapons including guns and knives.


### Camera Placement

- Install cameras at the entry and exit points of the building, as well as in areas where firearms and knives may be stored, such as security checkpoints, storage areas, and break rooms.
- Place cameras in areas where employees can easily see and respond to suspicious behavior.

### Camera Height

- Cameras should be installed at a height of 7-8 feet above the floor level.

- Place the camera 10-12 feet from the focal point.

### Camera Angle Mounting Ranges

- Place the camera at an angle to capture footage of the firearms and knives and surrounding area.


Find more details about camera placement [here](../overview/cameras.md).

## Model Details

### Dataset
The dataset for this scenario is based on real-world firearms and knives events.
The dataset consists of images and videos collected from various sources including UC Berkeley Anomaly Detection Dataset, UCF Crime Dataset etc.

### Model

The model is based off of the YOLOv5 algorithm. The model is trained on a custom dataset of images and videos. The model is trained based on the above dataset compiled by our team.

### Model card

<div class="table">
    <table class="fl-table">
        <thead>
        <tr><th>Dataset size</th>
            <th>Version</th>
            <th>Accuracy</th>
            <th>Recall</th>
            <th>F1 score</th>  
        </thead>
        <tbody>
        <tr>
            <td>4230</td>
            <td>v7</td>
            <td>98.2</td>
            <td>95.2</td>
            <td>95</td>
        </tr>
        </tbody>
    </table>
</div>

The model is adaptable enough to run on any edge computing device.

### Scenario details

The business logic for this scenario is as follows:

- We use existing camera feeds from the premises to detect firearms and knives events.
- VisionAI system is able to run on edge devices. It uses camera feeds for processing.
- We detect people in the camera feed and we monitor whether the person is carrying any firearms and knives.
- If the person is detected with this event, an alert is raised.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:
     
     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test firearms-knives-detection

        Downloading models for scenario: firearms-knives-detection

        

        Starting scenario: firearms-knives-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of firearms and knives within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features


The VisionAI solution is the most efficient way of implementing this scenario, as evidenced by the following features:

-  *Unmatched accuracy*

    Trained and Tested to give the best results. Our systems are trained to detect firearms and knives at the earliest detection with an accuracy of 99%

- *Lightning Fast and Response Time*

    Our Ultra-fast Processing provides real-time inference results and feedback (~30 frames per second processing). 

- *Minimizing false-positives/negatives*

    Our systems create a fail-proof system by ensuring there are no false-positives or false-negatives. 

- *Scalability and Deployment* 

    Our pre-trained/custom models can be deployed instantly and are camera independent which means they can be pre-installed with existing cameras on site. We also offer cameras, IoT sensors and edge devices with strategic placement that helps scale a large workplace area with minimum installations. 

- *Custom Integrations*

    Our detection system can be integrated with other safety systems, such as building management systems or alarm systems, allowing for a coordinated response to emergencies.

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please (contact us)[contact.md].


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).