# **Forklift Zone Monitoring**

> An intelligent alarm system that could be used to detect forklifts entering restricted zones

<figure markdown>
  ![Forklift Zone Monitoring](https://github.com/visionify/visionai-images/raw/main/visionai-images/forklift-breach-zone.png "Forklift Zone Monitoring at a work-place!"){ width="350" }
  <figcaption>Forklift Zone Monitoring event</figcaption>
</figure>

## Overview
Vehicle forklift zone monitoring is a system that uses cameras to monitor the forklifts entering restricted zones. It is used to enforce safety rules and calculate fine amounts, as well as to manage the flow of traffic. 

## Vision AI based monitoring
VisionAI based forklift zone monitoring is an advanced technology that can be used to monitor and enforce forklifts entering restricted zones in the workplace. 

With our Vision AI monitoring you can authorize access as well as continuous monitor live feeds inside a restricted area for real-time detection of unauthorized personnel. Our fully automated detection models are not only more powerful and accurate than existing systems but also more affordable and easy to integrate into existing infrastructure allowing users to scale real-time detection with a few simple clicks.                       

## Events

VisionAI model's generated events would be:

- Forklift observed outside of configured zone
- Pedestrian observed in forklift zone

It is recommended that any instance of such event be reported to the appropriate authority.
An event data may include information such as:

- Date and time of the event
- Location of the event
- license plate number
- Image of the event
- Video of the event

## Configuration

To set up a camera system to detect forklifting of vehicles, you will need to consider the following:

- Camera Placement: Cameras should be placed in locations where they can capture clear images of license plates, such as at entrances and exits to parking lots, toll booths, or intersections. Cameras should be mounted at an appropriate height and angle to capture the entire license plate.

- Camera Type: High-resolution cameras with a minimum resolution of 1080p are recommended for license plate detection. Cameras with a wide field of view (FOV) are also recommended to capture license plates from a distance.

- Lighting: Adequate lighting is essential for license plate detection. The lighting should be bright and evenly distributed to minimize shadows and glare.

## Model Details

### Dataset

The dataset consists of images and videos collected from diverse sources and is designed to reflect real-world scenarios. It is evenly distributed with;
 
- *Different environments*: Both indoor and outdoor with varying/contrasting surrounding and infrastructure details
- *Different lighting conditions*: Day and night with varying light intensities
- *Different camera angles*: Front, side, and rear views
- *Different vehicle types*: Cars, trucks, buses, and motorcycles
- *Different vehicle colors* etc.

### Model


The model to monitor enforcement of vehicle forklifting event is in progress and it will be released soon.

### Scenario details

The business logic for this scenario is as follows: 

- We use existing camera feeds from the premises to monitor occurrences of vehicle forklifting events. 

- VisionAI system is able to run on edge devices. It uses camera feeds for processing. 

- We detect vehicle forklifting event in the camera feed, an alert is raised.


=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test vehicle-forklift-detection

        Downloading models for scenario: vehicle-forklift-detection
        Model: vehicle-forklift-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
        

        Starting scenario: vehicle-forklift-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of vehicle cargo  monitoring event within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)

## Features

VisionAI based vehicle forklifting monitoring system exhibits following features:

- **Real-time detection**: VisionAI based vehicle forklifting monitoring system can detect vehicle forklifting event in real-time.

- **Scalable**: VisionAI based vehicle forklifting monitoring system can be scaled to monitor multiple cameras at the same time.

- **Easy to use**: VisionAI based vehicle forklifting monitoring system is easy to use and can be integrated with existing infrastructure with a few simple clicks.


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).