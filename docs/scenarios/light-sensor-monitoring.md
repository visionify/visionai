# **Light Sensor Monitoring**

> Monitor ambient light in real-time with our light-sensing solution

<figure markdown>
  ![Light Sensor Monitoring](https://visionai.azureedge.net/docs-images/docs-visionify-version1.0-23March23/light monitoring.webp "Detection of ambient lights!"){ width="350" }
  <figcaption>Detection of ambient lights event</figcaption>
</figure>

## Overview

Energy is valuable, hence efforts should be made for optimum energy usage. As carbon footprints increase, enterprises must adopt innovative methods to optimize energy consumption and reduce spendings. Innovative lighting solutions can help minimize service disruption, allow prompt servicing, and ensure centralized governance.

Light monitoring solutions are an innovation that is benefiting organizations across industries. These solutions use sensors to regulate and optimize lighting in the workplace and homes. There are various types of light sensors, namely ambient light sensors, infrared light sensor, sunlight sensors, and ultraviolet light sensors. Ambient light sensors are the most common sensing devices used in smartphones, tablets, smartwatches, LCDs, room lights, conference rooms, etc.


## Vision AI Sensor-Based Solution for Ambient Light Monitoring

Ambient light sensors can sense the surrounding light conditions and tell the processing chip to automatically adjust the display's brightness to reduce the product's power consumption. When the ambient illumination is high, the device using the ambient light sensor will automatically adjust to high brightness. When the external environment is dark, the display will be adjusted to low brightness to achieve automatic brightness adjustment.

Visionify’s light monitoring solution can monitor the ambient light of your electronic devices in real-time. When the ambient light of your equipment/devices sub-seeds a specific limit, it can be increased to the desired level. You can regulate illumination with our solution to cut bills and make best energy use. 



## Model Details

### Dataset

- Outdoor environments: The dataset contains images and videos of the outside environment. The lighting devices can be turned off (lights, for instance) in sunlight with the dataset's help and turned on in the evening.

- Daylighting conditions: The dataset contains images and videos under different lighting conditions. The model may need to adjust its settings as per the lighting needs.

- Distance from light source: The dataset contains images of ambient light sources captured from different distances. 

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
            <td>2326</td>
            <td>v5</td>
            <td>Ceiling</td>
            <td>65% </td>
            <td>71% </td>
            <td>71% </td>
        </tr>
        </tbody>
    </table>
</div>

### Scenario details

- The model automatically resets the brightness when the ambient light subseeds a threshold limit.
- The model allows you to automatically turn on/off light sources at particular times of the day or for a specific period. 
- When the equipment is faulty, and there is a high risk of an accident, the camera sensors can ring an alarm.
- Best suited for offices, factories, and homes with multiple intelligent appliances.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test light-sensor-monitoring

        Downloading models for scenario: light-sensor-monitoring
        Model: light-sensor-monitoring: https://workplaceos.blob.core.windows.net/models/yolov5s-light-sensor-monitoring/yolov5s-light-sensor-monitoring-0.0.1.zip
        

        Starting scenario: light-sensor-monitoring..

        ```
    - You should be able to see the events generated on your console window with the detections of light sensor monitoring events within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)




## Features

- Alert system: The model is programmed to send alerts when the light levels fall outside of a predetermined range.

- Integration with other systems: The model can be integrated with other systems, such as HVAC or lighting systems, to automatically adjust the environment based on the light levels.

- Remote monitoring: The model can be remotely monitored, allowing users to check the light levels from anywhere at any time.

- Energy efficiency: The model can help to promote energy efficiency by ensuring that lighting systems are only used when necessary, based on the detected light levels.


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).
