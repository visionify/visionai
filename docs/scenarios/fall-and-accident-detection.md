# Fall & Accident detection

> Detect potential collision/accident and wet floor, inspect slip and fall instances with VisionAI.


## Overview

Fall & Accident computer vision based detection system is designed to detect potential safety hazards in a given environment. The system uses video data from cameras placed in the area to identify a range of potential hazards, including person slip & fall, potential collision/accident, wet floor, debris on the floor, and wet/slippery signs.

To detect these hazards, the system uses deep learning-based algorithms to analyze the video data and identify specific patterns and features that correspond to each type of hazard. For example, to detect a person slip & fall, the system may look for sudden changes in movement, unusual body positions, or signs of distress.

Similarly, to detect potential collisions or accidents, the system may analyze the movement of people or objects in the environment and identify situations where there is a high likelihood of a collision or other accident occurring.


## Vision AI based monitoring 

Vision AI-based system can be used to detect slip and fall with high accuracy. Additionally, our model trained on real-world images minimizes false-positives or false-negatives.  

The cameras scan every frame to ensure there are no accidents related to slip and fall cases. 

To detect a wet floor, the system may look for areas where there is a significant change in reflectance or texture, which could indicate the presence of moisture.

To detect debris on the floor, the system may analyze the texture and shape of objects in the environment and identify items that are out of place or could potentially cause a tripping hazard.

Finally, to detect wet/slippery signs, the system may analyze the shape and color of signs in the environment and identify those that indicate a wet or slippery floor.

Overall, the system is designed to help improve safety in a range of environments, from factories and warehouses to retail stores and public spaces. By detecting potential hazards in real-time, the system can alert workers or visitors to potential dangers and help prevent accidents and injuries.

## Model Details

### Dataset

The dataset for this scenario is based on real-world data from different workplaces. The dataset consists of images and videos collected from various sources. 

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
            <td>72,20</td>
            <td>v1</td>
            <td>Both(Ceiling and Straight)</td>
            <td>95% </td>
            <td>93% </td>
            <td>85% </td>
        </tr>
        </tbody>
    </table>
</div>

### Scenario details


The business logic for this scenario is as follows:

- We use existing camera feeds from the premises to detect potential collision/accident and wet floor, monitor and detect occurrences of slip and fall incidents.  

- VisionAI system is able to run on edge devices. It uses camera feeds for processing.

- An alert will be raised, when a potential collision/accident and wet floor is detected and/or occurrence slip and fall instance.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test fall-and-accident-detection

        Downloading models for scenario: fall-and-accident-detection
        Model: fall-and-accident-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-fall-and-accident-detection/yolov5s-fall-and-accident-detection-0.0.1.zip
        

        Starting scenario: fall-and-accident-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of potential collision/accident and wet floor, slip and fall instances within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)




## Features

- Continuous monitoring: The model continuously monitors the user movements to ensure that they are safe and alert the user or emergency services if necessary. This includes monitoring the user's heart rate, breathing, and other vital signs to detect any signs of distress or injury.

- Alerting system: The model is able to alert supervisors or managers and/or emergency services when it identifies a range of potential hazards, including person slip & fall, potential collision/accident, wet floor, debris on the floor, and wet/slippery signs.

- Customization: The model must be customizable to fit the needs of different users. This includes settings for sensitivity, activity recognition, and user-specific parameters such as age, weight, and height.


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).