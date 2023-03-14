# Vehicle Policies

> An intelligent alarm system that could be used to detect fraudulent vehicle activity

# Overview
Vehicle policies at the workplace are a set of guidelines and rules that govern the use of vehicles owned or leased by a company or used by employees for work-related purposes. These policies are designed to ensure the safe and responsible use of company vehicles, as well as to protect the company from liability in case of accidents or other incidents.


## Vision AI based monitoring

VisionAI technology can be used to monitor and enforce vehicle policies in the workplace. With our Vision AI monitoring you can authorize access as well as continuous monitor live feeds inside a restricted area for real-time detection of unauthorized personnel. Our fully automated detection models are not only more powerful and accurate than existing systems but also more affordable and easy to integrate into existing infrastructure allowing users to scale the power of i-based real-time detection with a few simple clicks.



## Events

VisionAI model's generated events would be:

- Vehicle activity detected in non-designtated areas
- Vehicle activity detected during after-hours
- Collision event detected
- Near collision event detected

It is recommended that any instance of such events be reported to the appropriate authority.
An event data may include information such as:

- Date and time of the event
- Location of the event
- Type of event (collision, near collision, etc.)
- Image of the event
- Video of the event
- Vehicle license plate number



## Configuration

Camera setups can be used to detect and enforce vehicle policies in the workplace. The location of cameras to monitor vehicle policies will depend on the specific policies being enforced and the nature of the work environment. For example, 

- if the company has a policy that prohibits employees from using company vehicles for personal use, then cameras should be installed in areas where employees are likely to park their vehicles. 


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

- We use existing camera feeds from the premises to monitor and detect occurrences of vehicle non-compliance events. 

- VisionAI systemis able to run on edge devices. It uses camera feeds for processing. 

- We detect various vehicle events in the camera feed, an alert is raised.


=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test vehicle-detection

        Downloading models for scenario: vehicle-detection
        Model: vehicle-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
        

        Starting scenario: vehicle-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of vehicle monitoring within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)



## Features

VisionAI based vehicle monitoring can offer several features to enhance vehicle monitoring and policy enforcement. Here are some examples of features:

- Object Detection: Our monitoring systems can use computer vision to detect objects such as other vehicles, , which can provide additional information about the driving environment and help identify potential hazards.



- Anomaly Detection: AI-based systems can use machine learning algorithms to detect anomalous behavior, such as unusual driving patterns or irregular fuel consumption, which can help identify potential policy violations or security breaches.

- Real-time Alerts: Our AI-based systems can provide real-time alerts for vehicle policy violations, allowing for prompt corrective action to be taken.

Data Analytics: VisionAI system can provide detailed analytics and reports on vehicle usage, and compliance with policies, which can help identify areas for improvement and inform policy adjustments.

!!! Note

    Overall, AI-based vehicle monitoring can provide enhanced monitoring capabilities and valuable insights into vehicle usage and driver behavior, which can help improve safety, efficiency, and compliance with vehicle policies.

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).