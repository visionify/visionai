# No Smoking/No Vaping

> No smoking & No vaping zone enforcements with Vision AI.
<figure markdown>
  ![Image title](hhttps://visionai.azureedge.net/docs-images/docs-visionify-version1.0-23March23/no-smoking.png "Detection of smoke at a work-place!"){ width="350" }
  <figcaption>Detection of Smoking event</figcaption>
</figure>


## Overview
Smoking and vaping are typically banned in workplaces like manufacturing plants, construction sites, warehouses, chemical plants, etc., an ideal 100% compliance rate can be challenging to achieve. However, it is imperative for employers to ensure that their workplaces are absolutely smoke-free.

VisionAI makes it possible to avert workplace hazards and help employers maintain 100% compliance through smart AI solutions. Our next-gen real-time detection systems make sure a fire/smoke or any sign of vaping is detected instantly. These systems are also trained to generate alerts and notifications accordingly.

## Vision AI based monitoring

Vision AI based monitors can be used to detect smoking/vaping events by providing real-time video feeds of the factory area. The cameras scan every frame to ensure there is no sign of smoking/vaping.

## Model Details

### Dataset
The dataset for this scenario is based on real-world smoking/vaping events.
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
            <td>1785</td>
            <td>v2</td>
            <td>Both(Ceiling and Straight)</td>
            <td>98%</td>
            <td>95%</td>
            <td>95%</td>
        </tr>
        </tbody>
    </table>
</div>



### Scenario details

The business logic for this scenario is as follows:

- We use existing camera feeds from the premises to detect smoking/vaping events.
- VisionAI system is able to run on edge devices. It uses camera feeds for processing.
- We detect people in the camera feed and we monitor whether the person is involved in any smoking/vaping activity.
- If the person is detected with this event, an alert is raised.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test no-smoking-detection

        Downloading models for scenario: no-smoking-detection
        Model: no-smoking-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
        

        Starting scenario: no-smoking-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of smoking/vaping within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features


The VisionAI solution is the most efficient way of implementing this scenario, as evidenced by the following features:

-  *Unmatched accuracy*

    Trained and Tested to give the best results. Our systems are trained to detect Fire and Smoke at the earliest detection with an accuracy of 99%

- *Lightning Fast and Response Time*

    Our Ultra-fast Processing provides real-time inference results and feedback (~30 frames per second processing). 

- *Minimizing false-positives/negatives*

    Our systems create a fail-proof system by ensuring there are no false-positives or false-negatives. 

- *Scalability and Deployment* 

    Our models can be deployed instantly and are camera independent which means they can be pre-installed with existing cameras on site. We also offer cameras, IoT sensors and edge devices with strategic placement that helps scale a large workplace area with minimum installations. 

- *Custom Integrations*

    Our detection system can be integrated with other safety systems, such as building management systems or alarm systems, allowing for a coordinated response to emergencies.

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please (contact us)[contact.md].


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).