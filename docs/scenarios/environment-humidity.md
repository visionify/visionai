
# **Humidity Monitoring**

> Ideal tool to monitor humidity in the surrounding environment.

<figure markdown>
  ![Humidity Monitoring]( https://github.com/visionify/visionai-images/raw/main/visionai-images/humidity%20monitoring%20.jpeg"Detection of Humidity!"){ width="350" }
  <figcaption>Detection of Humidity event</figcaption>
</figure>

## Overview

Uncontrolled humidity has several implications in day-to-day life. Firstly, high humidity makes the air thicker and the surroundings uncomfortable for people. Secondly, uncontrolled humidity can build up electrostatic charges or cause corrosion. High humidity also leads to throat, eye, and skin irritation. Finally, the manufacturing process also needs to improve due to unmaintained humidity leading to compromised products. 

To understand why monitoring humidity is essential, one should first know what humidity is. It is the amount of water vapor in the air (also called absolute humidity). Relative humidity, however, is the percentage of moisture in the air compared to how much moisture the air can hold at that temperature. Therefore, both AH and RH are essential components in humidity monitoring.

Adopting a humidity monitoring solution can help industries prevent health and monetary losses and ensure seamless workflow. However, this can be challenging, to begin with. Visionify offers a suitable solution to all sorts of humidity challenges.


## Vision AI based monitoring

**Sensor-Based Solution for Humidity Monitoring**

VisionAI’s humidity monitoring solution helps businesses control humidity in various environments. Our sensor-based solution can monitor the humidity level and triggers an alarm/signal when levels break a threshold value. Our solution can be used for storage management, buildings and facilities management, HVAC (Heating Ventilation Air Conditioning), comfort optimization, asset condition tracking, and remote monitoring.

## Model Details

### Dataset

- Custom humidity: The model allows you to set humidity levels (absolute and relative). The alarm can be triggered when humidity in your facility reaches a high/low threshold value.

- Temperature: Temperature data is also required for humidity monitoring. Integrate your temperature monitoring devices with a humidity monitoring solution for a connected experience.

- Different distances from the camera: The dataset contains images and videos captured from different distances from the camera. This will help in capturing humidity from varied areas within the facility.

- Various lighting conditions: The dataset contains images and videos under different lighting conditions. The model may need to adjust its settings to continue detecting temperature accurately.

- Multiple camera angles and resolutions The dataset includes images taken from different angles, such as top-down, side view, or angled view, and available in varied resolutions.

- Using security camera feeds: The dataset includes images and videos collected from your existing security camera installations to make monitoring more accurate.

### Model

The model to monitor humidity in the surrounding environment is in progress and it will be released soon.

### Scenario details

- When the humidity crosses a high/low threshold value, the model can ring an alarm for a manual check.
- Share notifications with detailed insight on humidity data.
- Integrate existing temperature or pressure sensing devices with our humidity sensing solution for centralized data intelligence.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test humidity-monitoring

        Downloading models for scenario: humidity-monitoring
        Model: humidity-monitoring: https://workplaceos.blob.core.windows.net/models/yolov5s-humidity-monitoring/yolov5s-humidity-monitoring-0.0.1.zip
        

        Starting scenario: humidity-monitoring..

        ```
    - You should be able to see the events generated on your console window when humidity crosses a high/low threshold value.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)



## Features

- Easy to use: The model is easy to use and can be deployed in a few minutes.
- Customizable: The model can be customized to suit your needs.
- Real-time: The model can be deployed in real-time to monitor humidity in the surrounding environment.
- Scalable: The model can be scaled to monitor humidity in multiple facilities.



## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).







