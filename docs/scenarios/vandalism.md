# **Vandalism and property destruction**

> Safeguard your assets with our advanced vandalism detection model.

<figure markdown>
  ![Vandalism detection](https://github.com/visionify/visionai-images/raw/main/visionai-images/VANDALISM_GRAFFITI-04.jpg "Vandalism at workplace!"){ width="350" }<figcaption>Vandalism/Graffiti detection event</figcaption>
</figure>

## Overview
Vandalism and property destruction can have serious consequences, both for individuals and for society as a whole. For example, it can lead to physical harm, emotional distress, financial losses, and damage to public infrastructure. By developing a model that can accurately detect and predict incidents of vandalism and property destruction, we can take proactive measures to prevent them from occurring or minimize their impact if they do occur. This can include increasing surveillance, enhancing security measures, and improving emergency response protocols. Ultimately, a vandalism and property destruction model can help protect people and property, reduce costs associated with damage, and promote a safer and more secure society. We need a vandalism and property destruction model to help prevent and mitigate damage caused by these types of incidents. 

Technically, vandalism is described as a video event that is instantiated by a video object that inflicts temporally consistent static changes (such as damage) inside a preset restricted region that is purportedly left unaltered by normal (i.e., legal) interaction with video objects.

## VisionAI Based Monitoring

### **Vandalism**
VisionAI based Monitoring is an effective approach to investigate if the site has temporally  consistent and significant static changes, indicative of damage, when an object is detected departing such a place. A vandalism event is declared and the vandals are located if there are such changes and given that the site is typically unaltered following legal use. The proposed method has a 96% detection rate when applied to video clips of actual and simulated vandalism in action. It recognises several types of vandalism, including theft and graffiti, and it can deal with abrupt illumination changes, occlusions, and segmentation mistakes. The frame rate of the suggested approach is 13 frames per second.
#### Constraints
The automatic detection of vandalism in video surveillance is a challenging task because of:
- The complex and unpredictable nature of a vandalism act and the speed at which it may occur
- The underlying difficulty of finding a unique definition for vandalism which may vary based on social contexts and applications
- The difficulty in distinguishing between normal and vandal interaction between persons and vandalism-prone objects or sites and
- The lack of real vandalism test video sequences publicly available for training or testing.
#### Proposed Method for detection of vandalism

A video object refers to a temporally consistent region (over a short period)in a video sequence. Video objects have spatio-temporal features such as contour,area, motion, and trajectory. For example, a video object has a unique identifier (ID) maintained by the tracking algorithm during the life-time of an object in the videosequence. A video event is an interpreted spatio-temporal relationship associating one or multiple objects (e.g., moving, staying long and is inside). Video events have information associated with them such as the IDs of the video objects involved in the event, the time at which it is detected, and its duration which is the number of consecutive frames the event is detected.We only consider rigid vandalism-prone objects that do not change over time.This includes pay-phones, vending machines, and paying stations in parking lots.

For example, vandalism of electronic street signs switching content periodically is not considered. Also, we expect that the vandalism act alters the normal appearance of objects. Meaning, after the site is vandalized, there is visible damage (i.e., change) to the site. We use **video object segmentation** and **ID** tracking.
### **Graffiti**
Graffiti can have a negative effect on a community's property value and tourism. Moreover, it may cause a decline in retail sales and an increase in public dread, both of which might drain tax funds intended for prevention. 

The Graffiti Image classifier can help law enforcement more effectively recognise Graffiti Images on the streets in order to lessen damage.

**VisionAI based solution** is focused on improving the performance of Graffiti “classifier” using the **ResNet50** neural network by tuning parameters like Learning Rate, Batch Size and identifying the best freezing layer.


## Model Details

### Dataset

The dataset consists of images and videos collected from various sources. 

### Model
The model to perform graffiti-detection is in progress and it will be released soon.

### Scenario details

The business logic for this scenario is as follows:

- We use existing camera feeds from the premises to monitor an area or property in real-time, detecting any instances of vandalism or destruction as they occur.

- VisionAI system is able to run on edge devices. It uses camera feeds for processing.

- When instances of vandalism or destruction is detected, an alert will be raised.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test vandalism-graffiti-detection

        Downloading models for scenario: vandalism-graffiti-detection
        Model: vandalism-graffiti-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-vandalism-graffiti-detection/yolov5s-vandalism-graffiti-detection-0.0.1.zip
        

        Starting scenario: vandalism-graffiti-detection..

        ```
    - You should be able to see the events generated on your console window with graffiti vandalism being detected within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features

The VisionAI solution is the most efficient way of implementing this scenario, as evidenced by the following features:

- Prediction: Our vandalism graffiti detection model uses data and historical patterns to predict when and where vandalism and destruction might occur. For example, it can analyze patterns of past vandalism incidents to predict where future incidents might occur.

- Real-time monitoring: Vandalism graffiti detection model can continuously monitor an area or property in real-time, detecting any instances of vandalism or destruction as they occur. This allows for a rapid response and intervention.

- Automated alerts: Alerts can automatically be generated to authorities or property owners when incidents of vandalism or destruction are detected. This can help to improve response times and prevent further damage.


## Training with custom data
The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).

## Contact Us
- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai)

- For business inquiries, you can contact us through our [website](https://visionify.ai/contact)
