# **Station Occupancy**

> Revolutionize your workspace with our Smart Desk Occupancy Tracker.

# Overview
Tracking Workplace Metrics is key for identifying problems and driving growth. One such metric that organizations need to keep tabs on is desk occupancy. Tracking Desk Occupancy provides multiple valuable insights like worker productivity, worker behavioral analysis, floor planning, and utilization of space, all of which are required for workspace optimization and efficient resource management.

Despite the increasing adoption of desk occupancy measurement across industries, present systems utilized to measure desk occupancy are fraught with several limitations, exhibit limited accuracy, lack the ability to provide multiple metrics, and can incur substantial installation costs.

## Vision AI based monitoring

Introducing our fully automated Vision AI system for monitoring Desk Occupancy. Our next-gen AI models detect and count the presence of people within a specific area, whether they are performing a particular task or not, their dwell time, occupancy density and many more metrics. 

Our robust occupancy monitoring systems offer higher accuracy compared to current solutions, are cost-effective, and are capable of seamlessly integrating with existing cameras and infrastructure. With our system, there's no need to install multiple sensors or measurement devices, as a single camera can cover a wide area and enable users to easily leverage our AI-based real-time detection with minimal effort.


<figure markdown>
  ![](https://github.com/visionify/visionai-images/raw/main/visionai-images/desk-occupancy.png "Desk occupancy monitoring at a work-place!"){ width="350" }
  <figcaption>monitoring desk occupancy</figcaption>
</figure>

## Events

VisionAI model's generated events would be:

- Daily summary of occupancy metrics on a per desk/station basis

It is recommended that any instance of an absence of a person from his/her desk be reported to the appropriate authority.
An event data for desk occupancy scenario may include information such as:

- Date and time of the event
- Location of the event

## Model Details

### Dataset


The dataset consists of images and videos collected from diverse sources and is designed to reflect real-world scenarios. It is evenly distributed with:


- *Positive images*: The dataset includes images that contain people sitting at desks. These images should show a clear view of the desk and the person occupying it.

- *Negative images*: The dataset includes images that do not contain people sitting at desks. They could show empty desks or other objects in the workspace.

- *Images with occlusions*: The dataset includes images where the view of the person occupying the desk is partially obstructed, for example, by another object or person.

- *Images with different lighting conditions*: The dataset includes images that are taken under different lighting conditions, such as bright daylight, low-light, or artificial light.

- *Images with different camera angles*: The dataset includes images that are taken from different camera angles, such as top-down, side view, or angled view.

- *Images with different desk layouts*: The dataset includes images that show different types of desks, such as standing desks, shared desks, or cubicles.


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
            <td>1280</td>
            <td>v1</td>
            <td>Ceiling</td>
            <td>95.0% </td>
            <td>91.6% </td>
            <td>88.0% </td>
        </tr>
        </tbody>
    </table>
</div>

### Scenario details
Real-time detection and alerts for different scenarios includes but are not limited to:

- When a person sits down at a desk that was previously unoccupied, the model can detect the change in occupancy.
- When a person gets up from a desk, the model can detect that the desk is now unoccupied.
- If the model detects an object on the desk that obstructs the view of the person occupying it, it may not be able to detect occupancy until the obstruction is removed.
- If the lighting conditions in the room change, the model may need to adjust its settings to continue accurately detecting occupancy.
- The model can also detect occupancy in real-time as people move around the workspace, allowing it to track changes in occupancy throughout the day.


=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test desk-occupancy
        ```

        Downloading models for scenario: desk-occupancy
        Model: miss-fire-exting-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
        

        Starting scenario: desk-occupancy..

        ```
    - You should be able to see the events generated on your console window with the detections of desk occupancy within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)



## Features

Some potential features of VisionAI for monitoring desk occupancy could include:

 - *Object Detection*: This feature can help to monitor the occupancy of the desks and alert if a desk is occupied or not.

    - *Heat Map*: This feature can help to optimize the usage of the workspace and identify hotspots where there may be congestion.

    - *Occupancy Monitoring*: This feature can help to optimize the usage of the workspace and ensure that all desks are being used efficiently.

    - *Desk Usage Patterns*: This feature can help to optimize the usage of the workspace and identify areas that need improvement.

    - *Desk Reservation*: This feature can help to optimize the usage of the workspace and ensure that all desks are being used efficiently.


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).