# **Vehicle Cargo Monitoring**

> An intelligent alarm system that could be used to detect cargo in vehicles

<figure markdown>
  ![Vehicle Cargo Monitoring](https://github.com/visionify/visionai-images/blob/main/visionai-images/vehicle-cargo-limit.png "Vehicle cargo monitoring at workplace!"){ width="350" }
  <figcaption>Vehicle cargo monitoring event</figcaption>
</figure>

# Overview
Vehicle cargo monitoring is a system that uses cameras to monitor the cargo in vehicles. It is used to enforce cargo limits and calculate fine amounts, as well as to manage the flow of traffic. It is also used to detect vehicles that are carrying cargo that is not allowed for the conditions, such as when the road is wet or icy, or when there is heavy traffic.

## Vision AI based monitoring

VisionAI's cargo monitoring technology can be used to monitor and enforce vehicle cargo in the workplace. With our Vision AI monitoring you can authorize access as well as continuous monitor live feeds inside a restricted area for real-time detection of unauthorized personnel. Our fully automated detection models are not only more powerful and accurate than existing systems but also more affordable and easy to integrate into existing infrastructure allowing users to scale the power of i-based real-time detection with a few simple clicks.

## Events

VisionAI model's generated events would be:

- Vehicle cargo exceeds volume limit
- Vehicle cargo subceeds volume limit

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

### Model card

 <div class="table">
    <table class="fl-table">
        <thead>
        <tr><th>Dataset size</th>
            <th>Version</th>
            <th>Camera support</th>
            <th>Precision</th>
            <th>Recall</th>
            <th>mAP</th>  
        </thead>
        <tbody>
        <tr>
            <td>2350</td>
            <td>v1</td>
            <td>Both(Ceiling and Straight)</td>
            <td>95.0% </td>
            <td>78.6% </td>
            <td>91.0% </td>
        </tr>
        </tbody>
    </table>
</div>

### Scenario details

The business logic for this scenario is as follows: 

- We use existing camera feeds from the premises to monitor occurrences of vehicle cargo usage events. 

- VisionAI systemis able to run on edge devices. It uses camera feeds for processing. 

- We detect vehicle cargos in the camera feed, an alert is raised.


=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test vehicle-cargo-detection

        Downloading models for scenario: vehicle-cargo-detection
        Model: vehicle-cargo-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
        

        Starting scenario: vehicle-cargo-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of vehicle cargo  monitoring event within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)



## Features

VisionAI based cargo monitoring system exhibits following features:

- **Real-time detection**: VisionAI based cargo monitoring system can detect cargo in vehicles in real-time. This is achieved by running the detection model on the camera feed.

-   **Scalable**: VisionAI based cargo monitoring system can be scaled to monitor multiple cameras at the same time. This is achieved by running the detection model on the camera feed.

-   **Accurate**: VisionAI based cargo monitoring system can detect cargo in vehicles with high accuracy. This is achieved by running the detection model on the camera feed.

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).