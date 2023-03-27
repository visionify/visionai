# **Maximum Occupancy**

> Transform the way you manage occupancy in real-time with our cutting-edge Computer Vision Occupancy Monitoring Solution.

<figure markdown>
  ![Maximum Occupancy](https://github.com/visionify/visionai-images/raw/main/visionai-images/max-occupancy.jpg "Maximum occupancy monitoring at work-place!"){ width="350" }
  <figcaption>Maximum Occupancy monitoring event</figcaption>
</figure>

# Overview
Effective crowd management is critical for many workplaces like airports, hospitals, factories, and retail shops, among others. One key aspect is maintaining compliance with maximum occupancy limits which is  crucial for maintaining safety, mitigating potential injuries, and legal issues. 

Existing solutions for tracking maximum occupancy typically rely on manual monitoring, which can be labor-intensive, prone to errors, and time-consuming while other systems such as sensors and RFID (Radio-Frequency Identification) tags produce a lot of false readings, have limited range and incur significant expenses.

As such, there is a need for more efficient and reliable methods for monitoring and managing maximum occupancy. A promising solution lies in the use of computer vision technology, which can accurately detect and track individuals in real-time, providing an automated and seamless approach to crowd management.


## Vision AI based monitoring

Maintain workplace occupancy limits flawlessly by leveraging computer vision-powered occupancy monitoring. Monitor Occupancy levels in Real-Time, get instant alerts and warnings whenever count exceeds threshold limit. With our ready-to-deploy models, businesses can effortlessly adhere to regulations and maintain a safe environment without the need for manual monitoring or complex sensor installations. 

A single camera can cover a wide area, allowing businesses to leverage our AI-based technology with minimal effort. You can easily augment your existing infrastructure and get started with our models with just a few clicks.


<figure markdown>
  ![]( "Maximum monitoring at a work-place!"){ width="350" }
  <figcaption>monitoring maximum occupancy</figcaption>
</figure>

## Events

VisionAI model's generated events would be:

- Person count exceeds limit (Max occupancy exceeded)
- Person count is below limit (Max occupancy not exceeded)

## Event Data
An event data for maximum occupancy scenario may include information such as:

- Date and time of the event
- Location of the event
- type of event (Max occupancy exceeded, etc.)
- Image of the event

## Configuration

It is recommended to set up camera setups to monitor maximum occupancy in the workplace. The location of cameras to monitor maximum occupancy will depend on the specific policies being enforced and the nature of the work environment.

## Model Details

### Dataset
The dataset consists of images and videos of people in different scenarios.    

### Model
The model to monitor maximum occupancy is in progress and it will be released soon.

### Scenario details
  

Real-time detection and alerts for different scenarios includes but are not limited to:

- When person count exceeds the predefined limit
- When the threshold is about to be reached as a safety warning
- Warnings based on population flow

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test max-occupancy
        ```

        Downloading models for scenario: max-occupancy
        Model: max-occupancy: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
        

        Starting scenario: max-occupancy..

        ```
    - You should be able to see the events generated on your console window with the detections of maximum occupancy event within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)



## Features

Some potential features of VisionAI for monitoring maximum occupancy include:

- Real-time monitoring of maximum occupancy: VisionAI can monitor maximum occupancy in real-time, providing an automated and seamless approach to crowd management.

- Instant alerts and warnings: VisionAI can send instant alerts and warnings whenever count exceeds threshold limit.

- Easy to deploy: VisionAI can be easily deployed with minimal effort, allowing businesses to leverage our AI-based technology with minimal effort.

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).