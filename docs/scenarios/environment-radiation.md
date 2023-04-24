# **Radiation Monitoring**

> Keeping Radiation Under Control: Innovations in Radiation Monitoring and Safety Detection with Vision AI.

<figure markdown>
  ![Environment Radiation Monitoring](https://github.com/visionify/visionai-images/raw/main/visionai-images/radiation-monitoring.png "Radiation monitoring at work-place!"){ width="350" }
  <figcaption>Radiation monitoring event</figcaption>
</figure>

## Overview

Radiation monitoring refers to the process of measuring and analyzing levels of ionizing radiation in a particular area, in order to ensure safety and compliance with regulatory standards. Ionizing radiation is a type of energy that can cause damage to living cells and genetic material, and can potentially cause cancer and other health problems if exposure levels are too high.

Radiation monitoring is essential in a variety of settings, including nuclear power plants, medical facilities, industrial sites, and areas affected by natural disasters or other environmental hazards. Monitoring radiation levels can help identify potential sources of radiation exposure, track changes in radiation levels over time, and inform decisions about safety procedures and protective measures.

There are several different types of radiation monitoring devices and techniques, including:

1. Geiger counters and other handheld radiation detectors, which measure levels of radiation in a specific area.

2. Personal dosimeters, which are worn by workers in radiation-exposed environments to monitor their exposure levels over time.

3. Environmental radiation monitors, which are used to monitor radiation levels in the surrounding environment and track changes over time.

4. Remote sensing technologies, such as satellite-based sensors and unmanned aerial vehicles (UAVs), which can provide real-time data on radiation levels in hard-to-reach areas.

Advanced technologies, such as artificial intelligence (AI), machine learning, and big data analytics, are increasingly being used to support radiation monitoring efforts. These technologies can help process and analyze large amounts of radiation data, identify potential sources of radiation exposure, and inform decisions about safety procedures and protective measures.

Overall, radiation monitoring is essential for ensuring safety and compliance with regulatory standards in a variety of settings, and can play a critical role in protecting public health and the environment.

## Vision AI based monitoring

Vision AI based monitors can be used for the detection of radiation monitoring events by providing real-time video feeds of the factory area. The cameras scan every frame and raise an event whenever radiation level is detected to be above configured limit.

## Model Details

### Dataset
The dataset for this scenario is based on real-world radiation monitoring detection events. The dataset consists of images and videos collected from various sources. 

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
            <td>3220</td>
            <td>v1</td>
            <td>Both(Ceiling and Straight)</td>
            <td>65.0% </td>
            <td>71.6% </td>
            <td>71.0% </td>
        </tr>
        </tbody>
    </table>
</div>


### Scenario details

The business logic for this scenario is as follows:

- We use existing camera feeds from the premises for raising radiation monitoring detection events.
- VisionAI system is able to run on edge devices. It uses camera feeds for processing.
- We use geiger counter sensors and analyse the camera feed and monitor the radiation level.
- If radiation level is detected to be above configured limit, an alert is raised.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:
     
     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test radiation-monitoring-detection

        Downloading models for scenario: radiation-monitoring-detection
        

        Starting scenario: radiation-monitoring-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of radiation monitoring within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features


The VisionAI solution is the most efficient way of implementing this scenario, as evidenced by the following features:

-  Unmatched accuracy: Trained and Tested to give the best results. Our systems are trained to detect radiation monitoring events with an accuracy of 99%

- Lightning Fast and Response Time: Our Ultra-fast Processing provides real-time inference results and feedback (~30 frames per second processing). 

- Minimizing false-positives/negatives: Our systems create a fail-proof system by ensuring there are no false-positives or false-negatives. 

- Scalability and Deployment: Our pre-trained/custom models can be deployed instantly and are camera independent which means they can be pre-installed with existing cameras on site. We also offer cameras, IoT sensors and edge devices with strategic placement that helps scale a large workplace area with minimum installations. 

- Custom Integrations: Our detection system can be integrated with other safety systems, such as building management systems or alarm systems, allowing for a coordinated response to emergencies.

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).