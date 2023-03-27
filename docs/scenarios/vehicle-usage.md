# **Vehicle Usage Detection**

> An intelligent alarm system that could be used to detect vehicle usage

<figure markdown>
  ![Vehicle Usage Detection](https://github.com/visionify/visionai-images/blob/main/visionai-images/vehicle-usage.png "Detection of vehicle collision!"){ width="350" }
  <figcaption>Detection of vehicle usage event</figcaption>
</figure>

# Overview
Vehicle usage monitoring is a system that uses cameras to monitor the usage of vehicles on a road. It is used to enforce usage limits and calculate fine amounts, as well as to manage the flow of traffic. It is also used to detect vehicles that are travelling at an unsafe speed for the conditions, such as when the road is wet or icy, or when there is heavy traffic.

## Vision AI based monitoring

VisionAI's vehicle usage detection model can be used to monitor and enforce vehicle usage in the workplace. With our Vision AI monitoring you can authorize access as well as continuous monitor live feeds inside a restricted area for real-time detection of unauthorized personnel. Our fully automated detection models are not only more powerful and accurate than existing systems but also more affordable and easy to integrate into existing infrastructure allowing users to scale the power of i-based real-time detection with a few simple clicks.              

## Events

VisionAI model's generated events would be:

- Daily summary event of vehicle usage
- Path-map of vehicle usage

It is recommended that any instance of such event be reported to the appropriate authority.


## Configuration

To set up a camera system to detect vehicle usage, you need to consider several factors including:

- **Camera type**: The type of camera you use will depend on the environment you are monitoring. For example, if you are monitoring a parking lot, you may want to use a camera with a wide field of view. If you are monitoring a road, you may want to use a camera with a narrow field of view. You may also want to consider the camera’s resolution, frame rate, and other specifications to ensure that it can capture license plates clearly and accurately.

- **Camera placement**: The location of cameras to monitor license plates will depend on the specific policies being enforced and the nature of the work environment. For example, if you are monitoring a parking lot, you may want to place cameras at the entrance and exit of the lot. If you are monitoring a road, you may want to place cameras at intersections or other locations where vehicles are likely to stop. You may also want to consider the camera’s field of view and other specifications to ensure that it can capture license plates clearly and accurately.

          


## Model Details

### Dataset

The dataset consists of images and videos collected from diverse sources and is designed to reflect real-world scenarios. It is evenly distributed with;
 
- *Different environments*: Both indoor and outdoor with varying/contrasting surrounding and infrastructure details
- *Different lighting conditions*: Day and night with varying light intensities
- *Different camera angles*: Front, side, and rear views
- *Different vehicle types*: Cars, trucks, buses, and motorcycles
- *Different vehicle colors* etc.

### Model

The model to detect enforcement of vehicle policies event is in progress and it will be released soon.


### Scenario details

The business logic for this scenario is as follows: 

- We use existing camera feeds from the premises to monitor occurrences of vehicle licence events. 

- VisionAI systemis able to run on edge devices. It uses camera feeds for processing. 

- We detect vehicle licence plates in the camera feed, an alert is raised.


=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test vehicle-usage-detection

        Downloading models for scenario: vehicle-usage-detection
        Model: vehicle-usage-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
        

        Starting scenario: vehicle-usage-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of vehicle usage event within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)



## Features

VisionAI based vehicle usage monitoring can offer several features to enhance vehicle monitoring and policy enforcement. Here are some examples of features:

- **Daily Summary report**: A daily summary of vehicle usage events can provide valuable insights into the performance, efficiency, and compliance of a fleet of vehicles. This information can be used to identify areas for improvement, optimize vehicle utilization, reduce costs, and ensure compliance with policies and regulations.

- **Path-map of vehicle usage**: This refers to a graphical representation of the routes taken by a vehicle over a given period of time. This map can provide a visual representation of the vehicle's movements, including the starting and ending locations, stops along the way, and the route taken.

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).