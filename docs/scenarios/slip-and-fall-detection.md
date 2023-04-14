# **Slip and Fall Detection** 

> Ensure the safety of employees by inspecting slip and fall instances. Get real-time alerts when such kind of accidents occur at the workplace. 



## Overview

Slip and Falls are among the leading causes of occupational fatalities. Timely action in the event of a Fall/Slip accident can minimize damage and save lives. However, working alone or in a noisy environment hinders timely assistance.  

Here are some situations where a slip-fall detection system would be useful. 

- Construction sites: Detect slips and falls among workers and alert supervisors to potential hazards. Potential deployment zones include ladders, ramps, and scaffolds.  

- Working at heights: Falls from higher to lower levels are the most common cause of fatalities in Slip and Fall accidents, making Slip and Fall detection for workers at height vital. 


- Working Alone: Slip and Fall detection is crucial for specific job settings where employees are required to work alone, particularly during off-hours. Deployment areas could be for the following category of workers. 

- Construction Sites: Electricians, plumbers, and HVAC (Heating, ventilation, and air conditioning) technicians work alone on specific tasks where slip and fall would be useful. 

- Oil and gas: The system will be useful for remote location workers such as drill operators, pipeline inspectors, and pump operators working in oil and gas mining regions. 

- Telecommunications: Workers such as tower climbers and cable technicians often work alone at high-rise towers and other elevated locations and their safety can be ensured by slip and detection system. 

- Mining Industry: Workers such as underground miners and drill operators often work alone in remote and confined spaces. 

- Maintenance: Building engineers, window cleaners, painters, facility maintenance workers, etc., often work alone during the night shift and in isolated places at heights.
 

- Noisy Environments: Like working alone, a noisy environment can hinder the process of quick response. Deployment areas could be for the following category of workers.  
 
- Construction: Heavy equipment operators like jackhammer operators at construction sites work in extremely noisy environments. 

 

- Manufacturing: Workers in factories and assembly lines are exposed to a lot of noise due to the machinery and equipment used. 

 

- Airports: Workers at airports, such as ground crew and baggage handlers, are often exposed to high noise levels from aircraft engines and other airport equipment. 


- Elderly care facilities and Smart Homes: Detect slip and fall hazards in elderly care facilities. Such systems can also be deployed in homes to monitor the elderly or disabled, alerting caregivers or family members. 

## Vision AI based monitoring 

Vision AI-based system can be used to detect slip and fall with high accuracy. Additionally, our model trained on real-world images minimizes false-positives or false-negatives.  

The cameras scan every frame to ensure there are no accidents related to slip and fall cases. 

To ensure accuracy and reliability for the model, these camera-based monitoring services should be supplemented by strong compliance processes. Furthermore, workers working in different factory units should always be made aware of these accidents and how to safeguard them. 

## Camera Configuration

Recommended to set up ceiling-mounted cameras to detect and identify children, visitors, person without uniform and badges.

### Camera Placement

- Install cameras at entry and exit points, especially where people walk in wet conditions, such as near entrances, ramps, and stairways.
- Place cameras in high-traffic areas, especially those prone to slips, such as aisles, hallways, and corridors.

### Camera Height

- Cameras should be installed at a height of 7-8 feet above the floor level.

- Place the camera 10-12 feet from the focal point.

### Camera Angle Mounting Ranges

- Place the camera at a downward angle of 45-60 degrees to capture footage of the floor surface.

Find more details about camera placement [here](../overview/cameras.md).

## Model Details 

### Dataset 

Model training is carried out with Microsoft COCO: Common Objects in Context dataset. Only person class is considered for model building. COCO is a  large-scale dataset that addresses three core research problems in scene understanding: detecting non-iconic views (or non-canonical perspectives of objects), contextual reasoning between objects and the precise 2D localization of objects. 

COCO dataset has an even distribution of: 

- Different(indoor/outdoor) environments 

- Male vs Female  

- Different light settings 

- Variations in camera orientations 

- Using security camera feeds 

### Model 

The model is built using Yolov5 pre-trained model for detecting a person followed by a media pipe library used to estimate the pose of the person. The following performance metrics are recorded: 



<div class="table">
    <table class="fl-table">
        <thead>
        <tr><th>Model Name</th>
            <th>Precision</th>
            <th>Recall</th>
            <th> mAP  </th>  
        </thead>
        <tbody>
        <tr>
            <td>SLIP AND FALL DETECTION</td>
            <td>65.0% </td>
            <td>71.6% </td>
            <td>71.0% </td>
        </tr>
        </tbody>
    </table>
</div>



The model is adaptable enough to run on any edge computing device. 


### Scenario details


The business logic for this scenario is as follows: 

- We use existing camera feeds from the premises to monitor and detect occurrences of slip and fall incidents. 

- VisionAI system is able to run on edge devices. It uses camera feeds for processing. 

- We detect human poses to identify slip and fall accidents in the camera feed.  
- If either slip or fall is detected, an alert is raised.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test slip-and-fall-detection

        Downloading models for scenario: slip-and-fall-detection
        Model: slip-and-fall-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-slip-and-fall-detection/yolov5s-slip-and-fall-detection-0.0.1.zip
        

        Starting scenario: slip-and-fall-detection..

        ```
    - You should be able to see the events generated on your console window with slip and fall being detected within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please (contact us)[contact.md].


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).