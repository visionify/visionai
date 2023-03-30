# Equipment temperature monitoring

> Monitor equipment temperature. Get an alert when temperature exceeds a limit or below a threshold.


# Overview
Industry equipment works best under a fixed temperature range. However, these are susceptible to malfunction or failure if equipment temperature exceeds or falls a threshold value. It could halt service for more extended periods and cause fatal accidents.

Organizations need a sensor-based temperature monitoring device to ensure smooth equipment functioning, safe exits, and quick preventive maintenance. VisionAI-powered solutions monitor equipment temperature in real-time and alert signals if temperature surpasses threshold values.

## IR camera based monitoring for a temperature of an equipment

Visionify’s thermal monitoring solution integrated with an IR camera monitors equipment temperature and functioning under various conditions and surroundings. Our solution detects equipment temperature and performance by processing real-time images and videos from different sources. In addition, it can trigger an alarm (as soon as the temperature reaches the threshold margins or faulty equipment is detected) and identify areas where exits are present. 

By installing this in your facility, you can ensure the following:

- Long-term equipment health
- Quick equipment maintenance 
- Safe evacuation in case of an emergency

<figure markdown>
  ![Equipment temperature Monitoring]( https://github.com/visionify/visionai-images/raw/main/visionai-images/equipment%20temperature%20monitoring.jpeg"Detection of equipment temperature!"){ width="350" }
  <figcaption>Detection of Equipment temperature crossing limits event</figcaption>
</figure>

    
## Events

VisionAI model's generated events would be:

- Temperature exceeds limit
- Temperature subceeds limit


It is recommended that any instance of equipment temperature not maintaining its limit should be reported, especially if it is related to a fire safety system.

An event data for a temperature not maintaining its limit may include the following information:

- *Date and time*: The date and time when the temperature reading was taken and when the issue was first detected.

- *Location*: The specific location where the temperature reading was taken, such as a room or area within a factory.

- *Threshold limits*: The threshold limits for temperature, which can help to determine whether the temperature is outside of the acceptable range.

Having this information recorded in an event data can help to identify the cause of the temperature issue, determine the appropriate response and follow-up actions, and track the status of the issue over time.




## Configuration

Setting up IR Camera sensors in critical areas such as electrical rooms, server rooms, storage areas and kitchens is especially important, as these areas are often more prone to fire hazards due to the presence of heat-generating equipment or flammable materials. 

Regularly monitoring temperature variations can help to identify potential fire hazards before they escalate into a full-blown fire, allowing for prompt corrective action to be taken to prevent damage to property and ensure the safety of occupants.

In addition to installing temperature sensors, it's also important to ensure that the sensors are *calibrated* properly and that their readings are regularly checked and maintained. This can help to ensure that the temperature sensors are accurately detecting any temperature variations and triggering appropriate fire safety measures when necessary.



## Model Details

The model to detect temperature exceeds or subceeds event is in progress and it will be released soon.
### Scenario details

When equipment temperature changes rapidly, the model can detect heat or cooling loss.
If equipment temperature crosses a threshold value (both high and low), an alarm can be triggered for preventive maintenance. 
When the equipment is overheated, and there is a high risk of an accident, the IR camera sensors can mark safe exits.
The model allows you to upload the most recent version of the baseline image onto your camera before the inspection.



=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test temp-detection

        Downloading models for scenario: temp-detection
        Model: temp-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
        

        Starting scenario: temp-detection..

        ```
    - You should be able to see the information generated on your console window with the detections of smoking/vaping event within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features

VisionAI's thermal camera based solution is suitable for equipment monitoring as they can provide real-time temperature readings and help detect temperature variations that may indicate potential issues or problems with the equipment.


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).