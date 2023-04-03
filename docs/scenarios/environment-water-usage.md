# Water Usage Monitoring

>Advanced Technologies for Effective Water Management and Conservation with Vision AI.


## Overview

Water management involves the planning, development, distribution, and conservation of water resources for various purposes, including drinking, irrigation, industrial processes, and environmental conservation. Effective water management is essential for ensuring the availability of clean water, protecting natural ecosystems, and promoting sustainable economic development.

Water management can be a complex and multifaceted process, involving a range of technologies, policies, and stakeholders. 

Advanced technologies, such as remote sensing, geographic information systems (GIS), and data analytics, are increasingly being used to support water management efforts. These technologies can provide valuable insights into water availability, usage, and quality, helping to inform decision-making and improve the efficiency and effectiveness of water management practices.

## Vision AI based monitoring

Vision AI based monitors can be used to for the detection of water management events by providing real-time video feeds of the factory area. The cameras scan every frame and help identify water leaks, reduce water waste, and comply with environmental regulations.

## Events

VisionAI model's generated events would be:

- Water level exceeds limit

It is recommended that any instance of water level's exceeding should be reported. This is because it is a sign of inefficiency and can be used to optimize processes and reduce water costs. 

An event data for this may include the following information:

 - Date and time of the event: This is important for tracking the duration and frequency of the event, which can help in identifying patterns and potential causes.

- Location of the event: This refers to the area or facility where the water levels exceeded the normal range. This information helps in identifying areas that are prone to flooding or other water-related problems.

- Type of water source: This refers to the type of water body or source, such as a river, lake, reservoir, or groundwater. 

- Level of water exceeding normal range: This refers to the degree to which the water level exceeded the normal range, which can help in assessing the severity of the event and the potential damage caused.

- Water level: This refers to the actual water level at the time of the event. This information can be used to determine the cause of the event and the extent of the damage caused.


!!! Note

    By collecting and analyzing this event data, water management organizations can develop effective waste management strategies, reduce waste generation, and promote recycling and sustainable waste management practices.

## Configuration
To set up a camera system for water usage monitoring,You will need a camera capable of capturing footage of water bodies you want to monitor. 

## Model Details

### Dataset
The dataset for this scenario is based on real-world water management detection events.
The dataset consists of images and videos collected from various sources. 

### Model

The model to detect water management event is in progress and it will be released soon.


### Scenario details

The business logic for this scenario is as follows:

- We use existing camera feeds from the premises for raising water management events.
- VisionAI system is able to run on edge devices. It uses camera feeds for processing.
- From the camera feed we identify opportunities for water leaks, reduce water waste, and comply with environmental regulations.
- If water management event is detected, an alert is raised.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:
     
     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test water-management-detection

        Downloading models for scenario: water-management-detection
        

        Starting scenario: water-management-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of water management within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features
The VisionAI solution is the most efficient way of implementing this scenario, as evidenced by the following features:

- Accurate measurement: VisionAI solution is designed to provide accurate measurements of water consumption. 

- Real-time monitoring: Our solution can provide real-time monitoring of water usage. This helps to provide up-to-date information about the water usage patterns.

- Data logging: Our solution helps to track water usage patterns over time and analyze the data.

- Remote monitoring: Our solution can be accessed remotely. This means that the data can be accessed from anywhere, allowing for remote monitoring and management.

- Integration with other systems: Our solution can be integrated with other systems such as smart homes, irrigation systems, and water management systems. This helps to improve the overall efficiency and effectiveness of the systems.

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).