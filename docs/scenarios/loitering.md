# **Loitering Detection**

> Keeping Public Spaces Safe: Innovations in Loitering Detection and Prevention with Vision AI.

<figure markdown>
  ![Loitering Detection](https://github.com/visionify/visionai-images/raw/main/visionai-images/loitering-detection.png "Loitering Detection at work-place!"){ width="350" }
  <figcaption>Loitering detection event</figcaption>
</figure>

## Overview

Loitering detection refers to the use of technology to identify and monitor individuals who are loitering in public spaces, with the aim of preventing crime, reducing security risks, and maintaining public safety. Loitering is typically defined as lingering or remaining in a particular location for an extended period of time, without a legitimate reason to be there.

Loitering detection technologies may include sensors, cameras, and other monitoring systems that can detect and track individuals in public spaces. Some of these technologies can be integrated with machine learning and artificial intelligence (AI) algorithms to analyze data and identify patterns of behavior that may be indicative of loitering.

Loitering detection technologies can be used in a variety of settings, including transportation hubs, shopping centers, and other public areas where large groups of people may congregate. These technologies can help identify potential security threats, such as individuals who may be carrying weapons or engaging in suspicious activities.

However, there are also concerns about privacy and civil liberties when it comes to the use of loitering detection technologies. Critics argue that these technologies can be used to target marginalized communities, and may contribute to a climate of suspicion and discrimination.

Overall, the use of loitering detection technologies is a complex issue that requires careful consideration of both security and privacy concerns. While these technologies can play an important role in maintaining public safety, it is important to ensure that their use is balanced with respect for individual rights and freedoms.

## Vision AI based monitoring

Vision AI based monitors can be used to for the detection of loitering events by providing real-time video feeds of the factory area. The cameras scan every frame and raise an event when a person enters from an usually closed location, person detected during off-hours, person detected for extended duration of time.

## Model Details

### Dataset
The dataset for this scenario is based on real-world loitering detection events. The dataset consists of images and videos collected from various sources. 

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
            <td>8280</td>
            <td>v1</td>
            <td>Both(Ceiling and Straight)</td>
            <td>85.0% </td>
            <td>81.7% </td>
            <td>79.0% </td>
        </tr>
        </tbody>
    </table>
</div>

### Scenario details

The business logic for this scenario is as follows:

- We use existing camera feeds from the premises for raising loitering events.
- VisionAI system is able to run on edge devices. It uses camera feeds for processing.
- From the camera feed we monitor if a person enters from an usually closed location, person detected during off-hours, person detected for extended duration of time.
- If loitering event is detected, an alert is raised.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:
     
     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test loitering-detection

        Downloading models for scenario: loitering-detection
        

        Starting scenario: loitering-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of loitering within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features


The VisionAI solution is the most efficient way of implementing this scenario, as evidenced by the following features:

- Customization: Our systems are customizable to fit your needs. We can train our models with your own data and provide you with a custom solution. We also provide a custom license for our software if you wish to use it in a closed environment.

-  Unmatched accuracy: Trained and Tested to give the best results. Our systems are trained to detect loitering events with an accuracy of 99%

- Lightning Fast and Response Time: Our Ultra-fast Processing provides real-time inference results and feedback (~30 frames per second processing). 

- Scalability and Deployment: Our pre-trained/custom models can be deployed instantly and are camera independent which means they can be pre-installed with existing cameras on site. We also offer cameras, IoT sensors and edge devices with strategic placement that helps scale a large workplace area with minimum installations. 



## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).