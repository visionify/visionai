# Missing Fire Extinguisher

> Strengthen your smoke & fire detection compliance - through adding custom logic for checking for missing fire extinguisher from required places.

# Overview
Fire Extinguishers prove to be a crucial preventive measure against unexpected fires. These are essential components of safety features that can help contain early fires before they escalate into large ones. Adequately installed fire extinguishers in the building offer round-the-clock protection against unexpected fires, and a majority of fires can be put out using handy fire extinguishers.

However, if a fire breaks out, missing fire extinguishers can increase the risk of injury and damage and can also have legal and regulatory obligations. Failure to comply with regulations can incur fines or legal issues. It also raises a question about the business’s reputation and leads to a loss of trust from customers. The existing fire warning and safety systems also cannot identify early fire signs, and none of them offer detection of missing fire extinguishers.


## Vision AI based monitoring

Make your workplace safer with our VisionAI monitoring, a computer vision and deep learning-based solution that helps you detect missing fire extinguishers by analyzing visual data, making it easier for businesses to ensure that they have the necessary safety equipment in place.

Our fully automated system guards your facility 24/7. It sends instant alerts whenever a missing fire extinguisher is detected, allowing businesses to achieve improved fire safety, compliance with regulations, cost savings, and peace of mind. 

Missing Fire extinguisher at office            |  Missing Fire extinguisher at factory  
    :-------------------------:|:-------------------------:
    ![Fire extinguisher](https://github.com/visionify/visionai-images/raw/main/visionai-images/missing-fire-exting.jpg "Detection of missing fire extinguisher!"){ width="300" }  |  ![Fire extinguisher](https://github.com/visionify/visionai-images/raw/main/visionai-images/missing-fire-exting2.jpg "Detection of missing fire extinguisher!"){ width="300" }

## Events

VisionAI model's generated events would be:

- Missing fire extinguisher

It is recommended that any instance of a missing fire extinguisher be reported to the appropriate authority.
An event data for a missing fire extinguisher may include information such as:

- Date and time the missing fire extinguisher was discovered
- Location of the missing fire extinguisher, including the building, floor, and room number
- Type of fire extinguisher that is missing


## Configuration

It is recommended to set up camera in ceiling view to detect missing fire extinguisher event. Cameras can see an area, mark areas where a fire extinguisher should be present. Any time it is removed or used or not seen, we will generate this event.


## Model Details

### Dataset

The dataset consists of images and videos collected from diverse sources and is designed to reflect real-world scenarios. It is evenly distributed with;
 
- Different locations: Different locations within an industrial setting where fire extinguishers are usually installed, like emergency exits, heavy machinery, near combustible material etc., all have been considered within the dataset.
 
- Different angles and perspectives: The dataset includes images captured from different angles and perspectives, such as from above, below, or from the side, in a crowded space or fire extinguishers obscured behind other objects in different locations.
 
- Different lighting conditions: The dataset includes images in different lighting conditions, like where the fire extinguisher is clearly visible, partially visible or obstructed.

- Different classes: The dataset is balanced between the two classes, present and missing fire extinguishers, to avoid bias in the model.  


### Model

The model to detect missing fire extinguisher event is in progress and it will be released soon.

### Scenario details

Our VisionAI solution detects missing fire extinguishers in different scenarios within an industrial setting where the presence of fire extinguishers is expected. These scenarios can be;

- Fire extinguishers are generally wall or pillar mounted. Our model is trained to detect the missing fire extinguishers in these locations.

- Our state-of-the-art models can detect missing fire extinguishers near hazardous/combustible material inside a manufacturing plant.

- There are specific equipment or machinery that require the availability of fire extinguishers in close proximity for safety reasons. Our model can identify any such space if a fire extinguisher is missing.

- Also, the model can detect missing fire extinguishers near emergency exits, where they are installed for quick access in case of fire.  
 


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
    - You should be able to see the events generated on your console window with the detections of smoking/vaping event within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)



## Features

Some potential features of VisionAI for detecting missing fire extinguishers could include:

- *Continuous monitoring*: An system could continuously monitor fire extinguisher locations and track any changes in real-time, enabling prompt detection of missing fire extinguishers.

- *Location tracking*: The system could use sensors or other location tracking devices to monitor the precise location of fire extinguishers and track any movements or changes in their location.

- *Alerts and notifications*: When a missing fire extinguisher is detected, the system could automatically generate an alert or notification to the appropriate personnel or authorities, enabling prompt corrective action.

- *Historical data analysis*: Over time, the system could collect and analyze historical data on fire extinguisher locations, enabling identification of trends or patterns that may indicate underlying fire safety issues.

!!! Note

    Overall, an AI-based system for detecting missing fire extinguishers could enable more proactive and efficient fire safety monitoring and management, helping to prevent fires and ensure the safety of occupants and property.

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).