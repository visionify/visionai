# **Pressure Monitoring**
> Measure pressure in real-time, ensuring safe equipment and work conditions.

## Overview

Pressure sensors are essential for smooth equipment functioning and safe work conditions within the facility. Pressure sensors are used for various purposes, from automotive to medical, industrial to consumer, and building devices. A pressure sensor simply monitors the pressure of liquids, air, and gas and displays it in several units, such as Pascal, Bar, and PSI.

Various types of pressure sensors are used across industries to measure three common pressure types, i.e., Gauge Pressure, Absolute Pressure, and Differential Pressure. Submersible pressure sensors, for instance, are placed at the bottom of tanks for alert signals when the tank level falls below or rises above a safe limit. 

There are several other uses of pressure sensors in industries. However, the core mechanism remains the same, which we will discuss in the next section.

## Vision AI based monitoring

Visionify’s pressure sensors empower industry players to maintain and monitor the pressure in real time. Our intelligent sensors can measure the air, gas, or liquid pressure and alert you for preventive care of your infrastructure. 

When the surrounding environment’s pressure exceeds or falls a threshold value, an alarm signal gets triggered for your proactive action. You can use a suite of sensors (temperature, humidity, gas sensors) for more effective environmental monitoring.

## Model Details

### Dataset

- Measuring safe pressure levels: The dataset includes safe pressure, voltage, and current output values. It needs to be adequately calibrated.

- Pressure difference: The dataset includes values of pressure difference (i.e., a difference between upstream pressure and downstream pressure). This helps in keeping the pressure difference minimum.

- Temperature and humidity: Temperature and pressure data are also helpful in pressure monitoring. Integrate your monitoring devices via IoT for a connected experience and better decision-making.

- Indoor vs. Outdoor environments: The dataset includes images and videos of indoor and outdoor environments. The temperature sensors in IR cameras can differentiate between the two settings and present relevant data and best actions.

- Different distances from the camera: The dataset contains images and videos captured from different distances from the pressure sensor. This will help in better pressure monitoring from varied distances.

- Multiple camera angles and resolutions The dataset includes images taken from different angles, such as top-down, side view, or angled view, and available in varied resolutions.

- Using security camera feeds: The dataset includes images and videos collected from your existing security camera installations to make monitoring more accurate.


### Model

The model to monitor pressure in the surrounding environment is in progress and it will be released soon.

### Scenario details

- When the pressure crosses a high/low threshold value, the sensors can ring an alarm for immediate inspection.
- Share notifications with detailed insight on pressure data.
- Integrate existing temperature, humidity, and gas sensors for centralized data intelligence.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test pressure-monitoring

        Downloading models for scenario: pressure-monitoring
        Model: pressure-monitoring: https://workplaceos.blob.core.windows.net/models/yolov5s-pressure-monitoring/yolov5s-pressure-monitoring-0.0.1.zip
        

        Starting scenario: pressure-monitoring..

        ```
    - You should be able to see the events generated on your console window when pressure crosses a high/low threshold value.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)





## Features

- Alerting system: The model is able to send alerts and notifications to relevant stakeholders if environmental parameters exceed predefined thresholds or if there is a sudden change in the environment.

- Customization: The model is customizable and can be trained with custom datasets to suit your specific needs.

- Scalability and Integration: The model is scalable and easily integrated with other systems, allowing for seamless data exchange and collaboration across multiple departments or organizations.



## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).