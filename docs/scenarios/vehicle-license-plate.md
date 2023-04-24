# Vehicle Licence Plate Detection

> An intelligent alarm system that could be used to detect vehicle license plate numbers

# Overview
Vehicle license plate detection uses image processing algorithms to identify and extract the license plate information from images or video frames captured by a camera. License plate detection can be used for various purposes, including enforcing traffic laws, toll collection, parking management, and law enforcement.

## Vision AI based monitoring

VisionAI's license plate monitoring is an advanced technology that uses computer vision algorithms and machine learning models to detect and read license plates in real-time.

## Events

VisionAI model's generated events would be:

- Vehicle licence plate detected event

It is recommended that any instance of such event be reported to the appropriate authority.
An event data may include information such as:

- Date and time of the event
- Location of the event
- license plate number
- Image of the event
- Video of the event


## Model Details

### Dataset

The dataset consists of images and videos collected from diverse sources and is designed to reflect real-world scenarios. It is evenly distributed with;
 
- *Different environments*: Both indoor and outdoor with varying/contrasting surrounding and infrastructure details
- *Different lighting conditions*: Day and night with varying light intensities
- *Different camera angles*: Front, side, and rear views
- *Different vehicle types*: Cars, trucks, buses, and motorcycles
- *Different vehicle colors* etc.

### Model

The model is based on the YOLOv5 algorithm to detect licence plates. It is trained on the curated dataset. Licence plate blurring is performed using computer vision-based blurring operations. The model is developed in a way that it generalizes well for different environments and situations.

### Model card

 <div class="table">
    <table class="fl-table">
        <thead>
        <tr><th>Dataset size</th>
            <th>Version</th>
            <th>Camera support</th>
            <th>Precision</th>
            <th>Recall</th>
            <th> mAP  </th>  
        </thead>
        <tbody>
        <tr>
            <td>3220</td>
            <td>v1</td>
            <td>Straight</td>
            <td>96%<td>
            <td>97%</td>
            <td>98%</td>
        </tr>
        </tbody>
    </table>
</div>

The model is adaptable enough to run on any edge computing device.




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
        $ visionai scenario test vehicle-licence-detection

        Downloading models for scenario: vehicle-licence-detection
        Model: vehicle-licence-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
        

        Starting scenario: vehicle-licence-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of vehicle licence plate monitoring event within the camera field of view.

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