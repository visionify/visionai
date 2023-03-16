# **Intrusion Detection**

> An advanced physical intrusion detection system powered with Computer Vision and AI.

## Overview

Intrusion detection is a system to monitor suspicious activities indicating an intrusion. Intrusion detection is important to detect and prevent unauthorized access to the facility, production area and other restricted areas within a building or manufacturing setup. An intrusion detection system helps prevent theft and vandalism, protecting the facility from malicious activities that can disrupt production, damage equipment, and compromise sensitive information. In addition, an effective intrusion detection system helps to ensure compliance with regulations and standards related to security and safety in the industry.

The current physical intrusion detection systems have a limited detection range and a number of other problems. 
Existing solutions:
- Do not provide comprehensive coverage across a large sprawling area.
- Can be affected by environmental factors in the outdoors and raise false alarms.
- Are vulnerable to tampering.
- Do not offer much flexibility in terms of getting integrated well with other security measures like video surveillance not cost-effective. 


## Vision AI based monitoring

Expand your security capabilities with VisionAI, a modern AI and ML solution to detect intrusions and protect your premises against all potential physical intrusion threats. Our model can accurately identify suspicious behaviors that may indicate a physical intrusion and instantly alerts the security personnel, allowing them to take appropriate and timely action against it to avoid associated dangers.
 
Our smart solution seamlessly integrates with the existing camera infrastructure and analyzes the real-time video feed. It can help in different ways, offers a comprehensive solution to detect all forms of physical intrusion, and ensures compliance with all security and safety regulations.
 

## Model Details

### Dataset

The dataset consists of high-quality images and videos collected from diverse sources and is designed to reflect real-world scenarios. The dataset is representative of all types of environments that should be taken care of while detecting physical intrusion.  
 
- Different locations/environments – The dataset includes images/videos from a variety of indoor and outdoor environments, locations, weather conditions and building layouts.
 
- Diversity of intruders – The dataset considers images and videos of intruders from different backgrounds trying to intrude in various poses such as standing, walking, running, crawling etc. 

- Balanced - The dataset is evenly distributed and balanced between intrusion and non-intrusion examples to prevent bias towards one class of data.

- Different angles and perspectives - The dataset includes images and videos captured from different angles and lighting conditions to ensure the model can detect intrusion in various real-world scenarios.

### Model

The model to detection intrusion is in progress and will be released soon.

### Scenario details

Our VisionAI solution for intrusion detection can be deployed to a physical perimeter integrated with the existing camera infrastructure and works in different scenarios to detect physical intrusion. The model is equipped to detect the following;

- Any person with suspicious behavior
- Anybody trying to intrude in a building or perimeter
- Anybody trying to trespass a restricted area without permission
- Anybody loitering around a restricted area for an extended period 

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test intrusion-detection

        Downloading models for scenario: intrusion-detection
        Model: intrusion-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-intrusion-detection/yolov5s-intrusion-detection-0.0.1.zip
        

        Starting scenario: intrusion-detection..

        ```
    - You should be able to see the events generated on your console window with detection of intrusions within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)



## Features

- Real-time monitoring: The model can be deployed to a physical perimeter integrated with the existing camera infrastructure and works in real-time to detect physical intrusion.

- Comprehensive coverage: The model can detect intrusion in a variety of environments, locations, weather conditions and building layouts.

- Customizable: The model can be customized to detect intrusion in a specific area or location based on user requirements.

-Integration: The model can be integrated with other security measures like video surveillance to provide a comprehensive solution to detect all forms of physical intrusion.

- Alert system: The solution has an alert system to notify the security personnel in case of an intrusion.


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).
