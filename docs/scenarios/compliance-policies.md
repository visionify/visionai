# **Compliance policies** 

> Compliance policies are put in place by companies to ensure the safety of employees, customers, and the general public. To send real-time alerts to employees, managers, and other stakeholders if there is a potential violation or deviation from established policies and procedures.



## Overview
Company compliance policies are a set of rules and regulations that a company creates and enforces to ensure that it operates in accordance with applicable laws, regulations, and ethical standards. 

The purpose of compliance policies is to help companies prevent legal and ethical violations, promote responsible conduct, and maintain their reputation and public trust. Some of these are  No pictures and no mobile phones in certain areas etc.
There are many events that could trigger an alert for non-adherence to a compliance policy. Here are a few use cases:

# Equipment monitoring

Equipment monitoring is the process of monitoring the performance, health, and status of  various types of equipment, such as machinery, vehicles, or electronic devices, to ensure that they are functioning properly and to identify any potential issues or failures before they cause major problems.

## Vision AI based monitoring

Vision AI based monitors can be used to monitor  spaces by providing real-time video feeds of the area. These cameras can be used to monitor the presence of workers in the space and to generate events for different activities carried out by them.
 


### Dataset
The datasets for this scenario is based off of people detection and tracking algorithms that are used in the industry. It consists of images and videos.
 

### Model

The model is based off of the YOLOv5 algorithm. The model is trained on the above dataset. The model provides the following metrics:- 
<div class="table">
    <table class="fl-table">
        <thead>
        <tr><th>Model Name</th>
            <th>Precision</th>
            <th>Recall</th>
            <th>mAP</th>
        </thead>
        <tbody>
        <tr>
            <td>RUST AND CORROSION DETECTION</td>
            <td>79.5%</td>
            <td>49.0%</td>
            <td>56.2%</td>
        </tr>
        </tbody>
    </table>
</div>



The model is adaptable enough to run on any edge computing device.

### Scenario details

The business logic for this scenario is as follows: 

- We use existing camera feeds from the premises to monitor the equipments in the workplace. 
- VisionAI system is able to run on edge devices. It uses camera feeds for processing. 
- We detect instances of rust/corrosion if any in machine parts, manufacturing equipments.

# Space monitoring

Space monitoring refers to the process of monitoring and managing the use of physical spaces, such as offices, warehouses, and other facilities. The goal of spaces monitoring is to optimize the use of the space, improve employee productivity, and ensure the safety and security of the space and its occupants.

Several key components of space monitoring are occupancy tracking, confined space monitoring etc.


# Vision AI based monitoring

Vision AI based monitors can be used to safely detect these events by providing real-time video feeds of the area. These cameras can be used to detect an events pertaining for different cases including maximum occupancy in certain space etc.

## Dataset
The datasets for this scenario is based off of people detection and tracking algorithms that are used in the industry. The dataset is a combination of images and videos from various sources. The dataset is curated to ensure that it is representative of the real world. 

### Model
The model is based off of the YOLOv5 algorithm. The model is trained on a custom dataset of images and videos. The model is trained based on the above dataset curated by our team.

The model provides the following metrics:

<div class="table">
    <table class="fl-table">
        <thead>
        <tr><th>Model Name</th>
            <th>Precision</th>
            <th>Recall</th>
            <th>mAP</th>
        </thead>
        <tbody>
        <tr>
            <td>CONFINED SPACE MONITORING</td>
            <td>94.5%</td>
            <td>96.4%</td>
            <td>94.2%</td>
        </tr>
        </tbody>
    </table>
</div>


The model is light-weight enough to be run on any edge devices.

### Scenario details

The business logic for this scenario is as follows:
- We use existing camera feeds from the premises to monitor the presence of workers in the confined space.
- VisionAI system is run at the edge. It uses the camera feeds for processing.
- We detect and track people identified in this camera feed.
- We monitor the total duration of stay of these people in the confined space.
- If the duration of stay exceeds the compliance policy, an alert is raised.

- Unauthorized actions monitoring:

Unauthorized actions monitoring is the process of detecting and preventing unauthorized access or use of a system or a device. It involves monitoring user activity and detecting any suspicious behavior or activity that may indicate a security breach or unauthorized access.

Unauthorized actions monitoring can involve various events, including mobile phone usage, pictures clicked, food served and visitors and children at a work place.


# Vision AI based monitoring

Vision AI based monitors can be used to safely detect these events by providing real-time video feeds of the area. These cameras can be used to detect an unauthorized events.


These camera based detection processes should be supplimented by strong compliance practices. If workers are prohibited from such events and they found to be guilty of any of these, appropriate action can be taken.

## Model Details

### Dataset
To detect these events, model is trained for a  COCO :Common Objects in Context dataset. Basically, COCO is a  large-scale dataset and it provides real-world data representation.

### Model
The model is built using Yolov5 pre-trained model for different classes depends on an event. For example, to detect people clicking pictures at work place. Person and Mobile classes would be considered. The custom logic to identify body part movement is developed and an event is triggered if any such activity takes place.

In a similar way, other events like unauthorized mobile usage, visitors entry, food served and children found at work place would be handled.

The Yolov5 model provides the following metrics:
<div class="table">
    <table class="fl-table">
        <thead>
        <tr><th>Model Name</th>
            <th>Precision</th>
            <th>Recall</th>
            <th>mAP</th>
        </thead>
        <tbody>
        <tr>
            <td>PERSON DETECTION</td>
            <td>84%</td>
            <td>85.12%</td>
            <td>81.51%</td>
        </tr>
        </tbody>
    </table>
</div>


and landmark detection model gives the following metrics:

<div class="table">
    <table class="fl-table">
        <thead>
        <tr><th>Model Name</th>
            <th>Precision</th>
            <th>Recall</th>
            <th>mAP</th>
        </thead>
        <tbody>
        <tr>
            <td>LANDMARK DETECTION</td>
            <td>84.0%</td>
            <td>72.8%</td>
            <td>84.9%</td>
        </tr>
        </tbody>
    </table>
</div>

|Acccuracy|Recall	|Precision|
|---------|---------|-------|
|84%|72.8%|84.9%  |

### Scenario details

The business logic for these events would be as follows:
- We use existing camera feeds from the premises to detect unauthorized event
- We detect such events and an alert is raised.
- VisionAI system is run at the edge. It uses the camera feeds for processing.
