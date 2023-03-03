# Environment Monitoring

> Temperature monitoring, Air quality, Humidity, CO2 levels, Noise levels through AI.

## Overview


AI-based environment monitoring models can provide real-time insights into the environmental conditions of the workplace. This can be especially useful in industries such as manufacturing, retail, and healthcare, in which the environment must be closely monitored for safety and efficiency. AI-based environment monitoring models can detect changes in temperature, humidity, and other factors, allowing employers to take action quickly to correct any issues that may arise. Additionally, AI-based models can help employers identify areas of improvement and save energy by reducing the need for manual monitoring.

VisionAI toolkit can help with environment monitoring at a workplace by providing insights into environmental data such as temperature, humidity, CO2 levels, noise levels, air quality, and more. Our models trained to detect anomalies in environmental data, enabing employers to take proactive steps to ensure the safety of their employees. 

## Vision AI based monitoring using Sensors

Vision AI based monitors can be used to analyze weather patterns and predict future environmental conditions, allowing employers to plan ahead and make changes to their workplace environment accordingly. Additionally, our models can be used to develop automated systems for monitoring and controlling the environment, allowing employers to maintain a safe and healthy work environment with minimal effort.

Several sensors can be used to monitor different parameters, such as:

- Temperature sensors: Used to measure the temperature of a room or equipment.
- Humidity sensors: Used to measure the amount of moisture in the air.
- CO2 sensors: Used to detect the concentration of carbon dioxide in the air.

The parameters that are monitored depend on the needs of the user. For example, a homeowner may want to monitor the temperature and humidity levels in their home, while a business may want to monitor the air quality in their workspace to ensure the health and productivity of their employees.

Thresholds can be set up for each parameter, which can trigger an alert if the value goes above or below the specified limit. For example, if the temperature in a server room rises above a certain temperature, it can trigger an alert to prevent the equipment from overheating and causing damage.

If the sensors go out of battery, they will stop transmitting data to the monitoring system. Therefore, it's important to have a backup power source or replace the batteries as needed.
    
## Events

Event thresholds can be set up to determine how often alerts should be sent. For example, if the temperature in a room fluctuates frequently, it may be useful to set up an alert to be sent every 30 minutes. However, if the temperature remains relatively stable, an alert may only need to be sent once a day.

In summary, the Environment Monitoring Model is a valuable tool for monitoring and managing environmental conditions. With the use of sensors and threshold settings, users can be alerted to potential issues and take corrective actions to maintain a safe and productive environment.


## Configuration

Environment Monitoring Model is based on sensor data.
However, if a camera is desired or necessary for a specific monitoring application, a configuration that includes a high-resolution camera with infrared capabilities would be recommended. This type of camera would be able to capture clear images in low light conditions, making it useful for monitoring spaces that may not have adequate lighting. Additionally, an IP (Internet Protocol) camera can be used to allow for remote viewing and monitoring, enabling users to access live video feeds or recorded footage from anywhere with an internet connection. The specific camera configuration will depend on the needs of the user and the environment being monitored.


## Model Details

### Dataset

Environment monitoring dataset collection is in progress.


### Model

The model to detect environment monitoring events is in progress and it will be released soon.

### Scenario details

TODO: Enforcement scenarios. How to configure & use this scenario.


=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test environment-monitoring

        Downloading models for scenario: environment-monitoring
        Model: environment-monitoring: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
        

        Starting scenario: environment-monitoring..

        ```
    - You should be able to see the events generated on your console window with the detections of spills and leak event within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)



## Features

- Improved safety: By continuously monitoring environmental conditions, potential hazards can be identified and addressed before they become a safety concern.

- Increased productivity: Monitoring the environment in a workplace can help identify factors that may impact productivity, such as poor air quality or uncomfortable temperatures.

- Remote monitoring: With an environment monitoring model, users can remotely access data and receive alerts, allowing for quick response times and reducing the need for on-site inspections.

- Compliance: Certain industries and applications may have environmental regulations that require monitoring and reporting. An environment monitoring model can help ensure compliance with these regulations.

- Customization: Users can select specific sensors and configure thresholds to meet their unique monitoring needs, making the system customizable and flexible.

Overall, an environment monitoring model can help ensure the safety, comfort, and efficiency of monitored spaces, while also reducing costs and environmental impact.


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md)


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).