# Blocked Exit monitoring

> Ensure that your organziation is safe & compliant for any emergency evacuations. If any of your exits are blocked - get an event notifications so it can be quickly resolved.

<figure markdown>
  ![Image title](https://visionai.azureedge.net/docs-images/docs-visionify-version1.0-23March23/blocked-exit-monitoring.png "Detection of blocked exit at workplace!"){ width="350" }<figcaption>Detection of blocked exit</figcaption>
</figure>

## Overview

Every second counts in emergency situations such as fires, earthquakes, or other disasters, and people need to evacuate the premises as quickly as possible to avoid being trapped or injured. Therefore, the presence of functional emergency exits and a well-designed escape route plan is of paramount importance. 

Any blockages or obstructions in the exits could prove fatal as they hinder people's ability to evacuate safely and quickly. However, the accumulation of debris, fire flames, and toxic gasses can block exits. Time is of the essence, and wrong escape plans can impede people from escaping quickly and safely. 

Moreover, People may try to force their way through blocked exits, leading to injuries or even fatalities. In addition, blocked exits can hinder the efforts of rescue teams trying to enter the building to help those in need. This makes it critical to preempt operational exits and detect blocked ones before the situation worsens.

## Vision AI based monitoring
VisionAI based emergency rescue solution leverages cutting-edge AI-powered, real-time detection and monitoring of emergency exits with alerts and warnings for safe and secure evacuation in times of crisis. 

With our Blocked Exit Monitoring solution, you can rest assured that your premises are being monitored continuously, providing early warnings in case of any blockages in emergency exits. Our models can be deployed instantly and can augment your existing camera infrastructure with just a few clicks.
    
## Events
VisionAI model's generated events would be:

- Blocked exit detected


## Model Details

### Dataset
The dataset consists of images and videos collected from diverse sources and is designed to reflect real-world scenarios. It is evenly distributed with:


- Images of blocked exits: These images would provide visual examples of what a typical blocked exit looks like.

Images of different types of blockages which includes: 

* Images of debris: Images of different types of debris, such as fallen objects or construction materials, would help the model to recognize obstructions in the path to the exit.

* Images of fire: Providing images of fire, smoke, and flames would help the model to recognize the different visual parameters that indicate a fire hazard.

* Images of toxic gasses: Images of different types of toxic gasses, such as carbon monoxide, would help the model to recognize the signs of gas leaks and other potential hazards.

* Images of overcrowding: Providing images of overcrowded spaces would help the model to recognize the risk of blockages in case of an emergency.

* Images of unobstructed exits: Providing images of exits that are not blocked would help the model to distinguish between blocked and unblocked exits.
   

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
            <td>22,20</td>
            <td>v1</td>
            <td>Both(ceiling and Straight)</td>
            <td>95% </td>
            <td>93% </td>
            <td>85% </td>
        </tr>
        </tbody>
    </table>
</div>

### Scenario details
The business logic for this scenario is as follows:
- We use existing camera feeds from the premises to monitor blocked exits
- VisionAI system is run at the edge. It uses the camera feeds for processing.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test blocked-exit
        ```

        Downloading models for scenario: blocked-exit
        Model: blocked-exit: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
        

        Starting scenario: blocked-exit..

        ```
    - You should be able to see the events generated on your console window with the detections of maximum occupancy event within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)

## Features

Some potential features of VisionAI for monitoring maximum occupancy include:

- Real-time monitoring of maximum occupancy: VisionAI can monitor blocked exits in real-time, providing an automated and seamless approach to crowd management.

- Instant alerts and warnings: VisionAI can send instant alerts and warnings for detected blocked exits

- Easy to deploy: VisionAI can be easily deployed with minimal effort, allowing businesses to leverage our AI-based technology with minimal effort.


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).