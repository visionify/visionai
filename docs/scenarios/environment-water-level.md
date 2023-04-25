# Water Level Monitoring

>Advanced Technologies for Effective Water Management and Conservation with Vision AI.


## Overview

Water level monitoring is the process of measuring and tracking the water levels in rivers, lakes, reservoirs, and other bodies of water. It is an important aspect of water resource management, as it provides information about water availability, flood risk, and water quality.

## Vision AI based monitoring

Vision AI based monitors can be used to for the detection of water level management events by providing real-time video feeds of the factory area. The cameras scan every frame and help identify water leaks, reduce water waste, and comply with environmental regulations.

## Events

VisionAI model's generated events would be:

- Water level exceeds limit

It is recommended that any instance of water level's exceeding should be reported. This is because it is a sign of inefficiency and can be used to optimize processes and reduce water costs. 

An event data for this may include the following information:

- Date and time of the event: This is important for tracking the duration and frequency of the event, which can help in identifying patterns and potential causes.

- Location of the event: This refers to the area or facility where the water levels exceeded the normal range. This information helps in identifying areas that are prone to flooding or other water-related problems.

- Type of water source: This refers to the type of water body or source, such as a river, lake, reservoir, or groundwater. 

- Level of water exceeding normal range: This refers to the degree to which the water level exceeded the normal range, which can help in assessing the severity of the event and the potential damage caused.

- Water level: This refers to the actual water level at the time of the event. This information can be used to determine the cause of the event and the extent of the damage caused.


!!! Note

    By collecting and analyzing this event data, water management organizations can develop effective waste management strategies, reduce waste generation, and promote recycling and sustainable waste management practices.


## Model Details

### Dataset
The dataset for this scenario is based on real-world water management detection events.
The dataset consists of images and videos collected from various sources. 

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
            <td>3326</td>
            <td>v2</td>
            <td>Ceiling</td>
            <td>65% </td>
            <td>71% </td>
            <td>71% </td>
        </tr>
        </tbody>
    </table>
</div>


### Scenario details

The business logic for this scenario is as follows:

- We use existing camera feeds from the premises for raising water management events.
- VisionAI system is able to run on edge devices. It uses camera feeds for processing.
- From the camera feed we identify opportunities for water leaks, reduce water waste, and comply with environmental regulations.
- If water management event is detected, an alert is raised.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:
     
     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test water-level-detection

        Downloading models for scenario: water-level-detection
        

        Starting scenario: water-level-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of water management within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features


The VisionAI solution is the most efficient way of implementing this scenario, as evidenced by the following features:

- Accurate measurement: VisionAI's Water level monitoring solution is designed to provide accurate measurements of water levels. This helps to provide reliable data for various applications.

- Real-time monitoring: VisionAI can provide real-time monitoring of water levels. 

- Data logging: Our solution helps to track water level changes over time and analyze the data.

- Remote monitoring: Our solution helps to access data from anywhere, allowing for remote monitoring and management.



- Integration with other systems: Our solution can be integrated with other systems such as weather stations, irrigation systems, and flood warning systems. This helps to improve the overall efficiency and effectiveness of the systems.


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).