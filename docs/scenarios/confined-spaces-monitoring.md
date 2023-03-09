# **Confined Spaces Monitoring**

> Ensure safety of employees in confined spaces. Get real-time alerts when workers are present in the space for too long.

## Overview
Confined spaces refer to areas that are partially or fully enclosed and are not designed for continuous human occupancy. Examples include tanks, silos, storage bins, manholes, and underground vaults. These spaces can be hazardous due to limited ventilation, lack of natural light, and potential for hazardous atmospheric conditions.

Workers entering confined spaces are at risk of being overcome by toxic gases, asphyxiation, or other hazards. In addition, workers may be trapped in the confined space if an emergency occurs. Therefore, it is important to monitor confined spaces to ensure that they remain safe for workers.

To monitor confined spaces, cameras can be used - with an oversight manager observing these spaces. Along with cameras other IoT devices can be used to measure atmospheric conditions such as air quality, temperature, humidity, and toxic gas levels.

## Vision AI based monitoring

Vision AI based monitors can be used to monitor confined spaces by providing real-time video feeds of the area. These cameras can be used to monitor the presence of workers in the confined space, as well as the duration of how long they are present within the space. Companies can put compliance policies in place to ensure that workers are not present in the confined space for an extended period of time. Camera based monitors can track workers entering the premises, and monitor their total duration of stay; and if that exceeds the compliance policy, an alert can be raised.

It is important to note that these camera based monitoring provides should be supplanted by strong compliance processes to ensure their accuracy and reliability. In addition, workers entering confined spaces should always be trained on proper use of the monitoring equipment and be familiar with the hazards associated with confined spaces.


## Model Details

### Dataset
The datasets for this scenario is based off of people detection and tracking algorithms that are used in the industry. The dataset is a combination of images and videos from various sources. The dataset is curated to ensure that it is representative of the real world. It has equal distributions for:

- Indoor vs Outdoor environments
- Male vs Female
- Day vs Night
- Different types of clothing
- Different distances from the camera
- Various lighting conditions
- Various camera angles and resolutions
- Using seurity camera feeds

Total number of images used was 387,644

### Model
The model is based off of the YOLOv5 algorithm. The model is trained on a custom dataset of images and videos. The model is trained based on the above dataset curated by our team.

The model provides the following metrics:

<div class="main">
    <div class="bar">
        <h4>Precision <i class="fa fa-info-circle"></i></h4>
        <div role="progressbar" style="--value:94"></div>
    </div>
    <div class="bar">
        <h4>Recall <i class="fa fa-info-circle"></i></h4>
        <div role="progressbar1" style="--value:96"></div>
    </div>
    <div class="bar">
        <h4>mAP <i class="fa fa-info-circle"></i></h4>
        <div role="progressbar2" style="--value:94"></div>
    </div>
</div>


The model is light-weight enough to be run on any edge devices.

### Scenario details

The business logic for this scenario is as follows:
- We use existing camera feeds from the premises to monitor the presence of workers in the confined space.
- VisionAI system is run at the edge. It uses the camera feeds for processing.
- We detect and track people identified in this camera feed.
- We monitor the total duration of stay of these people in the confined space.
- If the duration of stay exceeds the compliance policy, an alert is raised.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test obstructed-camera-detection

        Downloading models for scenario: obstructed-camera-detection
        Model: obstructed-camera-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-obstructed-camera-detection/yolov5s-obstructed-camera-detection-0.0.1.zip
        

        Starting scenario: obstructed-camera-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of smoking/vaping event within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)

## Events Supported

This scenario supports the following events:

- **Person detected**: This event is generated when a person is detected in the camera feed.
- **Person left**: This event is generated when a person is no longer detected in the camera feed.
- **Person duration exceeded**: This event is generated when a person is detected for more than the specified duration in the camera feed. The duration amount is configurable through the web-app.


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).
