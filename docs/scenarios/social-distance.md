# **Social Distancing**

> Creating Safe Workplaces: Companies Implement Measures to Ensure Social Distancing in the Workplace with Vision AI.

<figure markdown>
  ![Image title](https://github.com/visionify/visionai-images/raw/main/visionai-images/Social-Distancing.png "Detection of social distancing at a work-place!"){ width="350" }
  <figcaption>Detection of Social distancing event</figcaption>
</figure>

## Overview

Maintaining social distancing in workplaces and industries is crucial to prevent the spread of diseases including COVID-19 and protect the health and safety of employees or workers. 

In workplaces and industries, where employees or workers are often in close proximity to each other for extended periods, social distancing can help to reduce the spread of the virus. By keeping a safe distance from each other, employees or workers can avoid coming into contact with respiratory droplets and reduce the risk of infection.

Overall, maintaining social distancing in workplaces and industries is an important part of a comprehensive approach to controlling the spread of certain diseases. By implementing social distancing measures and other best practices, employers can help to protect the health and safety of their employees or workers and prevent the spread of the virus.

## Vision AI based monitoring

Vision AI based monitors can be used to push out events for different people observed in the frame and the distances between them by providing real-time video feeds of the factory area. The cameras scan every frame to ensure social distancing is well maintained.

## Events

VisionAI model's generated events would be:
- Person distance events detected

### Camera Placement

- Install cameras in high traffic areas, such as entrances, exits, and common areas.
- Place cameras in areas where social distancing violations are most likely to occur, such as checkout lines or waiting areas.

### Camera Height

- Cameras should be installed at a height of 7-8 feet above the floor level.

- Place the camera 10-12 feet from the focal point.

### Camera Angle Mounting Ranges

- Place the camera at an angle that captures a wide area and any social distancing violations.

Find more details about camera placement [here](../overview/cameras.md).

## Model Details

### Dataset
The dataset for this scenario is based on real-world social distancing events.
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
            <td>6580</td>
            <td>v1</td>
            <td>Both(Ceiling and Straight)</td>
            <td>89.0% </td>
            <td>91.6% </td>
            <td>84.0% </td>
        </tr>
        </tbody>
    </table>
</div>


### Scenario details

The business logic for this scenario is as follows:

- We use existing camera feeds from the premises and raise social distancing events.
- VisionAI system is able to run on edge devices. It uses camera feeds for processing.
- We detect people and the distance between them form the camera feed and raise a alert if social distancing is not maintained.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:
     
     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test social-distancing

        Downloading models for scenario: social distancing
    
        

        Starting scenario: social distancing..

        ```
    - You should be able to see the events generated on your console window with the detections of social distancing within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features


The VisionAI solution is the most efficient way of implementing this scenario, as evidenced by the following features:

-  *Unmatched accuracy*

    Trained and Tested to give the best results. Our systems are trained to detect social distancing with an accuracy of 99%

- *Lightning Fast and Response Time*

    Our Ultra-fast Processing provides real-time inference results and feedback (~30 frames per second processing). 

- *Minimizing false-positives/negatives*

    Our systems create a fail-proof system by ensuring there are no false-positives or false-negatives. 

- *Scalability and Deployment* 

    Our pre-trained/custom models can be deployed instantly and are camera independent which means they can be pre-installed with existing cameras on site. We also offer cameras, IoT sensors and edge devices with strategic placement that helps scale a large workplace area with minimum installations. 

- *Custom Integrations*

    Our detection system can be integrated with other safety systems, such as building management systems or alarm systems, allowing for a coordinated response to emergencies.

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).