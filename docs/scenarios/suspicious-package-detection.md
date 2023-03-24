# **Suspicious Package Detection**

> Reliable and accurate Suspicious package detection for a safe and secure workplace environment
<figure markdown>
  ![Suspicious Package Detection](https://github.com/visionify/visionai-images/raw/main/visionai-images/Suspicious%20package%20detection-01.jpg"Detection of suspicious packages!"){ width="350" }
  <figcaption>Detection of Suspicious Package event</figcaption>
</figure>

## Overview

Manual inspection of every package or parcel is time-consuming and can lead to delays in delivering important items. An automated detection model can quickly screen packages and prioritize those that require additional inspection. By detecting suspicious packages early, it may be possible to prevent an incident from occurring. This can save lives and minimize damage to property.

Suspicious packages could contain hazardous materials such as explosives or chemicals, which could pose a significant risk to the safety of employees and the public. A detection model can quickly identify potential threats and allow for timely evacuation or other appropriate actions.

Implementing a suspicious package detection model can enhance workplace safety and security, improve operational efficiency, and ensure compliance with legal requirements.


## Vision AI based monitoring

VisionAI suspicious package detection model is trained on a large dataset of known suspicious packages, as well as non-suspicious packages, to learn to recognize the characteristics that are most indicative of a threat.  VisionAI based suspicious package monitoring can be used to analyze new packages and determine whether they are suspicious or not. If a package is flagged as suspicious, security personnel can be alerted to investigate further and take appropriate action.



## Model Details

### Dataset

The dataset for this type of model typically consists of a large number of images or videos, captured from a variety of angles and under different lighting conditions. The images or videos may be collected from surveillance cameras or from other sources, such as social media posts or news reports.

To ensure that the model is able to generalize to new and unseen images or videos, the dataset should include a diverse range of packages, with different sizes, shapes, colors, and markings. The dataset should also include examples of packages that are not suspicious or abandoned, in order to provide a balanced training set.

### Model
The model to detect agressive behaviour events is in progress and it will be released soon.


### Scenario details

The business logic for this scenario is as follows:

- We use existing camera feeds from the premises to monitor suspicious packages within the camera field of view.
- The model is able to detect suspicious packages and an alert system is in place to notify the appropriate authorities in the event that a suspicious package is detected. It is designed to minimize false alarms and provide timely and accurate information.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test suspicious-package-detection

        Downloading models for scenario: suspicious-package-detection
        Model: suspicious-package-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-suspicious-package-detection/yolov5s-suspicious-package-detection-0.0.1.zip
        

        Starting scenario: suspicious-package-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of aggressive behavior within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features

- Real-time monitoring: The model is able to analyze data in real-time to detect potential suspicious packages.

- Integration with other systems: The model is able to integrate with other security systems, such as access control systems, to provide a comprehensive approach to package security.

- Alert system: The model is having an alert system that can notify the appropriate authorities in the event that a suspicious package is detected. It is designed to minimize false alarms and provide timely and accurate information.

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).