# **Spills & Leaks detection**

> Spills and Leaks detection through Vision AI.

## Overview
Spills and leaks in industries can have significant health impacts on both humans and wildlife. The severity of the health impact depends on the type of substance that is spilled or leaked, the duration and extent of the exposure, and the vulnerability of the exposed population. Some potential health impacts of spills and leaks are Respiratory problems, skin irritation, Neurological effects, Cancer, Reproductive problems and Environmental impact.

Preventing and mitigating spills and leaks is crucial for protecting the environment and human health. Existing solitions could be regular inspections and maintenance of equipment. Manual inspection is not foolproof and can be prone to errors and oversights. Human inspectors may miss small leaks or spills that may go undetected until they become larger and more severe.



## Vision AI based monitoring
Manual inspections can be time-consuming and labor-intensive, which can make them impractical for large or complex industrial facilities.


Vision AI-based model is designed to detect spills and leaks including water puddles, water leaks and slippery surfaces. The model can analyze images and video footage to identify visual anomalies, such as the appearance of a spill or leak, which can be missed by human inspectors.

  Oil leak            |  Water leak in pipes
    :-------------------------:|:-------------------------:
    ![oil leak](https://visionai.azureedge.net/docs-images/docs-visionify-version1.0-23March23/oil-leakage.png)  |  ![water leak](https://visionai.azureedge.net/docs-images/docs-visionify-version1.0-23March23/Water-Leak.png)

## Events
  
  VisionAI model's generated events would be:

  - Water puddle detected
  -  Water leak from equipment detected
  - Spill event detected
  -  Slippery sign detected

## Model Details

### Dataset
Dataset for spills/leakages is properly curated and validated to ensure that the models are accurate and reliable. 

Some of the sources used to take images are:

- CAMEO Chemicals dataset
- The NOAA Hazardous Material Incident database
- The Oil Spill Dataset

- The Pipeline and Hazardous Materials Safety Administration (PHMSA) dataset

- The Spill Impact Mitigation Assessment (SIMA) dataset


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
            <td>4170</td>
            <td>v1</td>
            <td>Both(Ceiling and Straight)</td>
            <td>85.0% </td>
            <td>91.6% </td>
            <td>87.0% </td>
        </tr>
        </tbody>
    </table>
</div>

### Scenario details

The business logic for this scenario is as follows: 

- We use existing camera feeds from the premises to monitor the signs of leakage, spills in the workplace to ensure the safety of human lives in the workplace. 
- VisionAI system is able to run on edge devices. It uses camera feeds for processing. 
- We detect any kind of leakage in the camera feed.
- An alarming system is inplace as part of solution.



=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test no-leak-detection

        Downloading models for scenario: no-smoking-detection
        Model: no-leak-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
        

        Starting scenario: no-leak-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of spills and leak within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)



## Features

VisionAI's Spill and leak detection  identifies and classifies spills and leaks in real-time. Here are some features of spill and leak detection:

- *Real-time monitoring*: AI-based spill and leak detection systems can continuously monitor facilities and pipelines in real-time, allowing for quick detection and response times.

- *Automated detection and alerts*: AI-based systems can detect spills and leaks automatically and issue alerts to relevant personnel or systems, allowing for quick response and mitigation of the issue.

- *Increased accuracy and reliability*: VisionAI models can analyze large amounts of data quickly and accurately, allowing for the identification of even small leaks or spills that may be missed by human inspectors.

- *Integration with other systems*: VisionAI solution can be integrated with other systems such as alarm systems and spill response plans, allowing for a more comprehensive and effective response to spills and leaks.

- *Predictive analytics*: VisionAI models  can analyze historical data and patterns to identify potential risks and prevent future spills and leaks.

- *Remote monitoring*:  The system allows continuous monitoring of facilities and pipelines in remote or hard-to-reach areas.

!!! Note

    Overall, spill and leak detection using our VisionAI's solution provides a powerful tool for industries to improve the accuracy, speed, and efficiency of spill and leak detection and response. The use of AI can also help to reduce the risk of human exposure to hazardous materials and prevent environmental damage caused by spills and leaks.


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please (contact us)[contact.md].


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact-us/).