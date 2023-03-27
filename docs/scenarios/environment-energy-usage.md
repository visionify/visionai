# **Energy Usage Monitoring**

> Empowering Sustainability: Innovations in Energy Usage Monitoring and Management with Vision AI.

<figure markdown>
  ![]("Energy Usage Monitoring at work-place!"){ width="350" }
  <figcaption>Energy Usage Monitoring events</figcaption>
</figure>

## Overview
Energy usage monitoring refers to the process of collecting and analyzing data on how energy is being used in buildings, facilities, and other settings. The purpose of energy usage monitoring is to identify opportunities for energy conservation and efficiency improvements, reduce energy waste and costs, and promote sustainability.


Overall, energy usage monitoring is an essential component of sustainable energy management, helping to reduce energy waste, lower costs, and promote a more sustainable future.

## Vision AI based monitoring

Vision AI based monitors can be used for the detection of energy usage monitoring events by providing real-time video feeds of the factory area. The cameras scan every frame and monitor the energy usage of machines and equipment in a factory and help identify inefficiencies, optimize processes, and reduce energy costs.

## Events

VisionAI model's generated events would be:

- Energy usage exceeds limit

It is recommended that any instance of energy level's exceeding should be reported. This is because it is a sign of inefficiency and can be used to optimize processes and reduce energy costs.

An event data for this may include the following information:


- Date and Time: The date and time when the event was detected.

- Location: The location where the event was detected.

- Device: The device where the event was detected.   

## Configuration
To set up a camera system for energy usage monitoring,You will need a camera capable of capturing footage of your energy meter or other relevant devices that you want to monitor. 

  

## Model Details

### Dataset
The dataset for this scenario is based on real-world energy usage monitoring detection events.
The dataset consists of images and videos collected from various sources. 

### Model

The model to detect energy usage monitoring is in progress and it will be released soon.


### Scenario details

The business logic for this scenario is as follows:

- We use existing camera feeds from the premises for raising energy usage monitoring events.
- VisionAI system is able to run on edge devices. It uses camera feeds for processing.
- From the camera feed we identify inefficiencies, optimize processes, and reduce energy costs.
- If energy usage monitoring event is detected, an alert is raised.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:
     
     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test energy-usage-monitoring-detection

        Downloading models for scenario: energy-usage-monitoring-detection
        

        Starting scenario: energy-usage-monitoring-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of energy usage monitoring within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features
The VisionAI solution is the most efficient way of implementing energy usage monitoring scenario, as evidenced by the following features:                           

- Accurate measurement: VisionAI energy usage monitoring systems are designed to provide highly accurate measurements of energy consumption. This helps to provide reliable data for various applications.

- Real-time monitoring: VisionAI energy usage monitoring systems can provide real-time monitoring of energy consumption. 

- Data analytics: VisionAI systems can use advanced data analytics to identify energy usage patterns and trends. 

- Automated insights: VisionAI usage monitoring systems can automatically provide insights and recommendations for energy savings based on the data analysis. 

- Integration with other systems: VisionAI usage monitoring systems can be integrated with other systems such as smart buildings, HVAC systems, and lighting systems. This helps to improve the overall efficiency and effectiveness of the systems.

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).