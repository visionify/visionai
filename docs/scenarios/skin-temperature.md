# **Temperature monitoring**

> Monitor the temperature of workers at your facility in real-time and alert if the temperature exceeds or falls a threshold value.


# Overview
Temperature monitoring is a vital need for all organizations. From hand-held temperature screening devices to no-contact thermal imaging systems, companies use various tools to monitor the temperature of workers. 

While hand-held screening devices are suitable for one-to-one inspection but unsuitable for real-time monitoring, they don't provide accurate outcomes for long-distances (i.e. 2 to 3 meters). IR-powered thermal imaging systems offer the best solution for quick and precise workplace temperature monitoring.


## IR camera based monitoring for a temperature of an equipment

Visionify's thermal temperature monitoring solution monitors the skin temperature of people within the work premises. It consists of three main components i.e., a thermal camera, a computer, and a temperature reference which is gained through real-time images and videos collected from different sources. 

The IR camera sensors read skin surface temperature and calculate an estimated core-body temperature. Suppose that temperature is above a particular range. In that case, an alarm can be triggered, and the alerts can be shared with the respective personnel for one-to-one inspection with a clinical thermometer.

By installing this in your facility, you can ensure the following:

- Real-time person temperature monitoring
- Restricted access to certain rooms or areas
- Centralized monitoring of all cameras

<figure markdown>
  ![Person skin temperature monitoring](https://visionai.azureedge.net/docs-images/docs-visionify-version1.0-23March23/people temperature monitoring.jpg "Detection of person temperature!"){ width="350" }
  <figcaption>Detection of Person temperature event</figcaption>
</figure>


    
## Events

VisionAI model's generated events would be:

- Person temperature exceeds limit

It is recommended that any instance of person's temperature exceeding should be reported, especially if it is related to a fire safety system.

An event data for a person temperature not maintaining its limit may include the following information:


- Date and Time: The date and time when the temperature reading was taken and when the issue was first detected.

- Location: The specific location where the temperature reading was taken, such as a room or area within a factory.

- Device: The device that detected the temperature issue.      

## Configuration

Here are the basic steps to set up an infrared (IR) camera for person temperature monitoring:

- *Choose a suitable location*: The camera should be installed in a location where there is sufficient space for people to pass through without obstruction. The ideal location is at the entrance of a building or a room where people can be screened before entering.

- *Set up the camera*: The camera should be positioned so that it is at a level that is higher than the heads of the people being screened. The camera should also be angled downwards to capture the forehead region where the temperature is usually measured. 

- *Configure the camera settings*: The camera settings should be adjusted to optimize the temperature measurement accuracy. 

- *Set up a screening process*: A screening process should be established to ensure that everyone passing through the camera is screened. 



!!! Note
    It's important to note that the above steps are general guidelines, and the specific setup and procedures may vary depending on the type of camera and the intended use case. 


## Model Details

The model to detect temperature exceeds or subceeds event is in progress and it will be released soon.
### Scenario details

When a person's temperature crosses the threshold value, the model can trigger an alarm, and the person can be sent for inspection.
Internal email and text notifications in case of negative tests.
Speed up temperature monitoring by leveraging facial recognition capabilities.




=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test person-temp-detection

        Downloading models for scenario: person-temp-detection
        Model: person-temp-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
        

        Starting scenario: person-temp-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of person temperature exceeding event within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features

VisionAI's thermal camera based solution is suitable for person temperature monitoring. Thermal cameras detect infrared radiation emitted from an object or person and convert that radiation into a temperature reading, which can be used to measure a person's body temperature


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).