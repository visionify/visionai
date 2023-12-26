# **Aggressive Behavior**

> Create a safer and more productive work environment with our real-time Aggressive behaviour detection system.

<figure markdown>
  ![Aggressive Behavior](https://visionai.azureedge.net/docs-images/docs-visionify-version1.0-23March23/aggressive-behavior-detection.png "Aggressive behavior detection at work-place!"){ width="350" }
  <figcaption>Detection of Aggressive Behavior</figcaption>
</figure>


## Overview

A workplace that is free from bullying, fighting, and aggressive behavior can help to improve employee well-being and overall job satisfaction. This can result in higher levels of productivity, better employee retention rates, and a more positive work environment. Aggressive behavior is a serious problem at workplaces. It can lead to serious injuries and even death. It is important to detect these behaviors early on, and preventive measures can be taken to address the issue before it escalates.

These models are an important tool for promoting a safe and respectful environment at workplaces and other settings, and they have the potential to make a real difference in the lives of those who may be vulnerable to bullying or aggression.

## Vision AI based monitoring

VisionAI's agressive behaviour detection model is designed to promote a safe, healthy, and productive workplace environment for all employees. The model is able to provide real-time alerts when it detects aggressive behavior. This will enable management to intervene and prevent escalation of the situation.


## Model Details

### Dataset

The dataset for this scenario is based on real-world data from different workplaces. The dataset consists of images and videos collected from various sources.

### Model

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
            <td>32,20</td>
            <td>v1</td>
            <td>Ceiling</td>
            <td>95% </td>
            <td>93% </td>
            <td>85% </td>
        </tr>
        </tbody>
    </table>
</div>

### Scenario details


The business logic for this scenario is as follows: 

- We use existing camera feeds from the premises to monitor the presence of people and analyse their behaviour.

- VisionAI system is able to run on edge devices. It uses camera feeds for processing. 

- An alarming system is in place as part of an aggressive behavior detection solution.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test aggressive-behavior-detection

        Downloading models for scenario: aggressive-behavior-detection
        Model: aggressive-behavior-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-aggressive-behavior-detection/yolov5s-aggressive-behavior-detection-0.0.1.zip
        

        Starting scenario: aggressive-behavior-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of aggressive behavior within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)





## Features

- Easy to use: The model is easy to use and can be deployed in a variety of settings, including workplaces and other public spaces.

- Alert system: The model is able to generate alerts when it detects signs of bullying, fighting, or aggressive behavior, allowing management to take appropriate action to address the issue.

- Real-time monitoring: The detection model is be able to monitor and analyze interactions among employees in real-time to identify any signs of bullying, fighting, or aggressive behavior.



## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact-us/).

