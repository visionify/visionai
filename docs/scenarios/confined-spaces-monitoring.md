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
- Total number of images used was 387,644

### Model
The model is based off of the YOLOv5 algorithm. The model is trained on a custom dataset of images and videos. The model is trained based on the above dataset curated by our team.

The model provides the following metrics:

- Accuracy: 0.945
- Precision: 0.96
- Recall: 0.94
- mAP: 0.945

The model is light-weight enough to be run on any edge devices.

### Scenario details

The business logic for this scenario is as follows:
- We use existing camera feeds from the premises to monitor the presence of workers in the confined space.
- VisionAI system is run at the edge. It uses the camera feeds for processing.
- We detect and track people identified in this camera feed.
- We monitor the total duration of stay of these people in the confined space.
- If the duration of stay exceeds the compliance policy, an alert is raised.

## Try it now

### Quick method - using your local web-cam

To test this model & scenario, you can use the following steps:

- Install the visionai package from PyPI

<div class=termy>
```console
$ pip install visionai
---> 100%
```
</div>

- Test the scenario from your local web-cam

<div class=termy>

```console
$ visionai scenario test confined-spaces-monitoring

Downloading models for scenario: confied-spaces-monitoring
Model: confined-spaces-monitoring: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
---> 100%

Starting scenario: confined-spaces-monitoring..

```
</div>

- TODO: Add images from your local web-cam here showing people detection & dwell time tracking.

- You should be able to see the events generated on your console window if the same person is detected for more than 30 seconds within the camera field of view.

### In an actual confined space

To use this scenario in an actual confined space, you can use the following steps:

- Install the visionai package from PyPI

<div class=termy>
```console
$ pip install visionai
---> 100%
```
</div>

- Download the scenario

<div class=termy>

```console
$ visionai scenario download confined-spaces-monitoring

Downloading models for scenario: confied-spaces-monitoring
Model: confined-spaces-monitoring: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
---> 100%
```

</div>

- Add the camera feed to the scenario

<div class=termy>

```console
$ visionai camera add OFFICE-01 --url rtsp://192.168.0.1/stream1
$ visionai camera OFFICE-01 add-scenario confined-spaces-monitoring
$ visionai run

Starting scenario: confined-spaces-monitoring..

```

</div>

- You should be able to see the events generated on your console window if the same person is detected for more than 30 seconds within the camera field of view.

### Through VisionAI Web-Application

You can also use the VisionAI web-application to manage your cameras & scenarios. You can use the following steps:

- Install the visionai package from PyPI

<div class=termy>

```console
pip install visionai
---> 100%
```

</div>


- Run the VisionAI web-application

<div class=termy>

```console
$ visionai web start

Starting VisionAI web-application..

```

</div>

- This opens up a web-app that you can use to manage your cameras & scenarios. First add the camera feed to the system and check if it is working.

TODO: Add image for the showing how to add camera

- Once the camera is added, you can add the scenario to the system. Search for "confined spaces monitoring" and add it to the camera.

TODO: Show image for adding scenario to a camera.

- Click start to start the scenario. You should be able to see the events generated on your console window if the same person is detected for more than 30 seconds within the camera field of view.

TODO: Show image for starting the scenario & seeing the feed from the scenario

### Using Azure Managed Service App

TODO: Add instructions for using Azure Managed Service App

## Events Supported

This scenario supports the following events:

- **Person detected**: This event is generated when a person is detected in the camera feed.
- **Person left**: This event is generated when a person is no longer detected in the camera feed.
- **Person duration exceeded**: This event is generated when a person is detected for more than the specified duration in the camera feed. The duration amount is configurable through the web-app.


## Training with custom data

The scenario is provided as part of our GPL-v3 Open-Source package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please (contact us)[contact.md].


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).
