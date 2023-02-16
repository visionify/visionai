# **Mobile Phone Usage Detection** 

> Enabling businesses to overcome digital distractions and misuse of mobile phones at workplaces.

Mobile phones at workplaces are proving to be an insidious way to execute malicious purposes. Prevent industrial espionage and reinforce security measures with the most reliable mobile phone usage detection models powered by AI and Deep Learning. 
Visionify's computer vision solutions are more accurate than the conventional methods, can safely detect mobile phone usage (people taking pictures, recording videos/audios, sending texts in prohibited areas). We offer instant integration with your existing camera infrastructure, and quick results. 


## Vision AI based monitoring


Vision AI-based system can be used to detect mobile phone usage by providing real-time video feeds at workplaces. This system can be used to detect an event of workers using mobile phones aganist compliance policies.


Enforce any company policies on mobile-usage in the workplace.
These camera based detection processes should be supplimented by strong compliance practices. If workers are prohibited from mobile usage, ensure that they are aware of the policy and the consequences of violating it. So, if an employee is found to be using mobile phone, an appropriate action needs to be taken.


## Model Details

### Dataset
Model training is carried out with Microsoft COCO: Common Objects in Context dataset. Person class is considered for model building. 

Basically, COCO is a  large-scale dataset and it provides real-world data representation including:

- Indoor vs Outdoor environments
- Male vs Female
- Day vs Night
- Different types of clothing
- Different distances from the camera
- Various lighting conditions
- Various camera angles and resolutions
- Using seurity camera feeds


### Model
The model is built using Yolov5 pre-trained model for person and mobile classes. The yolov5 model is used to identify the human body landmarks of the subject. 

The Yolov5 model provides the following metrics:


|Acccuracy|	Recall	|mAP	|
|---------|---------|-------|
|84%  |85.12%    |81.51%  |

and landmark detection model gives the following metrics:

|Acccuracy|Recall	|Precision|
|---------|---------|-------|
|84%|72.8%|84.9%  |
The model is light-weight enough to be run on any edge devices.

### Scenario details

The business logic for this scenario is as follows:
- We use existing camera feeds from the premises to detect mobile phone usage by employees.
- VisionAI system is able to run on edge devices. It uses camera feeds for processing. 
- We detect the mobile phone usage event and an alert is raised.



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
$ visionai scenario test mobile-usage-detection

Downloading models for scenario: mobile-usage-detection
Model: mobile-usage-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
---> 100%

Starting scenario: mobile-usage-detection..

```
</div>


- You should be able to see the events generated on your console window with phone usage being detected within the camera field of view.

### In an actual environment

To use this scenario in an actual environment, you can follow these steps:

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
$ visionai scenario download mobile-usage-detection

Downloading models for scenario: mobile-usage-detection
Model: mobile-usage-detection
https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
---> 100%
```

</div>

- Add the camera feed to the scenario

<div class=termy>

```console
$ visionai camera add OFFICE-01 --url rtsp://192.168.0.1/stream1
$ visionai camera OFFICE-01 add-scenario mobile-usage-detection
$ visionai run

Starting scenario: mobile-usage-detection..

```

</div>

- You should be able to see the events generated on your console window with phone usage being detected within the camera field of view.

For more details visit VisionAI [web application](https://visionify.ai/).


## Features

- Unparalleled Accuracy and faster detection: Our models, not only trained to detect the presence of a mobile device but detect its usage, are equipped to achieve an outstanding accuracy of up to 92%.   
- Seamless integration and Scalability: An end-to-end solution, integrates seamlessly with your existing camera network and is ready to detect. Easily expandable by adding more IP cameras to the network. 
- Integrated Solution: It is an integrated system combining surveillance and mobile phone detection in one system.
- Absolute Privacy: We understand your concerns about data privacy and take a proactive approach to preserve it. Our models are privacy oriented by design.
- Automate and Grow: Leverage the precision and power of the groundbreaking computer vision technology, automate complex tasks and detect flaws sooner to achieve better performance and reduced costs.   
- Versatile Framework: We offer flexibility in deployment; the model can operate at the Edge, in the cloud, or any self-hosted environment. 



## Training with custom data

The scenario is provided as part of our GPL-v3 Open-Source package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please (contact us)[contact.md].


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).