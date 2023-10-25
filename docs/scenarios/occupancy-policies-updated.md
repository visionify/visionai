# Occupancy Policies

Ensuring security and controlled access at the workplace is vital for organizations, but conventional surveillance and crowd management techniques are complex, expensive, and heavily reliant on human intervention. Furthermore, these systems are often unable to provide desired, foolproof results due to limitations, inaccuracies, and the inability to provide multiple metrics. One of the significant challenges with current systems for workplace crowd management is the constantly evolving workplace dynamics.

 
## Visionify’s Workplace Safety Suite for Occupancy Policies

Our Crowd Management suite offers a complete solution set that helps you regulate access, enforce security policy adherence and deter intruders effectively. Our fully automated and ready-to-deploy models enable real-time monitoring for the detection of unauthorized access attempts, ensuring that your facility is guarded 24/7. Instant alerts are sent to prevent security breaches before they happen. Our system guarantees reliable detection and can be seamlessly integrated with your existing camera infrastructure, making it easy to scale your system with just a few clicks.

What’s included in this suite:

- No food or drinks
- No phone, text, pictures
- No Smoking zones
- No children/visitors
- Waste Management
- Energy Conservation
- Restricted Areas





# **Occupancy Metrics**

> Track workplace Occupancy Metrics effortlessly.

<figure markdown>
  ![Image title](https://visionai.azureedge.net/docs-images/docs-visionify-version1.0-23March23/Occupancy-Metrics.jpeg "Real-time occupancy metrics!"){ width="350" }<figcaption>Occupancy metrics</figcaption>
</figure>

## Overview

Measuring occupancy metrics is crucial for businesses because of the valuable insights it offers. By accurately measuring and analyzing occupancy metrics, businesses can make data-driven decisions to improve other aspects of their business, like optimizing the physical layout and resource management.

## Vision AI based monitoring

Track workplace Occupancy Metrics effortlessly with Vision AI monitoring ready-to-deploy model that provides real-time insights and analysis with valuable insights such as:

- Occupancy count: This measures the number of people or objects within a given space, such as a room or a parking lot.

- Dwell time: This measures the amount of time that people spend in a particular location, such as a store or a workspace.

- Traffic flow: This tracks the movement of people or objects through a space, enabling businesses to optimize their layouts for maximum efficiency.

- Occupancy density: This measures the number of people or objects per unit of space, indicating whether a particular area is overcrowded or underutilized.

- Heatmaps: These visualizations show the most crowded areas in a building or a room, helping businesses to optimize their layouts and improve customer flow.

- Social distancing compliance: This monitors and enforces social distancing guidelines by identifying people who are too close to each other and triggering an alert.

- Foot traffic: This tracks the number of people entering and exiting a building, store, or event, providing insights into customer behavior and trends.

- Queue management: This analyzes the length of lines and identifies bottlenecks, optimizing customer flow and reducing wait times in places like retail stores and theme parks.

- Occupancy rate: This measures the percentage of space that is occupied at a given time, providing insights into space utilization and capacity planning.

- Crowd density: This measures the number of people per unit of space, providing insights into areas that may be overcrowded or unsafe.

- Occupancy behavior: This tracks how people move and interact within a space, providing insights into how spaces are being used and how they can be optimized.

- Occupancy trends: This analyzes occupancy data over time, identifying patterns and trends that can inform business decisions such as staffing, marketing, and capacity planning.

- Occupancy alerts: This triggers alerts when occupancy levels exceed predetermined thresholds, enabling businesses to take proactive measures to manage crowds and ensure safety.

## Model Details

### Dataset

The dataset consists of images and videos collected from diverse sources and is designed to reflect real-world scenarios. It is evenly distributed with:

- Images with different subjects
- Images with different lighting conditions
- Images captured at different times of the day
- Images with different camera angles
- Images with different camera 
- Images with a variety of occlusions, such as people partially hidden behind obstacles or objects.
- Variation in subjects
- Images with different environments

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
            <td>4726</td>
            <td>v1</td>
            <td>Ceiling</td>
            <td>91.0% </td>
            <td>89.6% </td>
            <td>84.0% </td>
        </tr>
        </tbody>
    </table>
</div>

### Scenario and Potential Deployment Area Details

- Retail stores: Retail stores can use occupancy metrics to optimize store layouts, improve customer flow, and reduce wait times.

- Office buildings: Office buildings can use occupancy metrics to optimize workspace layouts, improve traffic flow, and identify underutilized areas.

- Transportation hubs: Transportation hubs, such as airports and train stations, can use occupancy metrics to optimize passenger flow, reduce wait times, and improve safety.

- Stadiums and event venues: Stadiums and event venues can use occupancy metrics to optimize seating arrangements, improve traffic flow, and enhance the overall visitor experience.

- Healthcare facilities: Healthcare facilities can use occupancy metrics to optimize waiting areas, improve patient flow, and ensure compliance with social distancing guidelines.

- Public spaces: Public spaces, such as parks and city centers, can use occupancy metrics to optimize traffic flow, identify overcrowding, and improve safety.

- Manufacturing plants: Manufacturing plants can use occupancy metrics to optimize production lines, improve traffic flow, and identify bottlenecks.

- Parking lots: Parking lots can use occupancy metrics to optimize parking arrangements, reduce wait times, and improve safety.


=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test occupancy-metrics

        Downloading models for scenario: occupancy-metrics
        Model: occupancy-metrics: https://workplaceos.blob.core.windows.net/models/yolov5s-occupancy-metrics/yolov5s-occupancy-metrics-0.0.1.zip
        

        Starting scenario: occupancy-metrics..

        ```
    - You should be able to see the events generated on your console window with events of occupancy metrics within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features

- Lightning Fast and Response Time: Ultra-fast Processing for real-time inference results and feedback (~30 frames per second processing) with customizable telemetry and inference results for your requirements.

- Scalability and Instant Deployment: Our pre-trained/custom models can be deployed instantly and are camera independent which means they can be pre-installed with existing cameras on site. 

- Custom Integrations: Our custom smart dashboards and real-time alert/notification systems can be tailored to fit your specific needs be it simple dashboards or complex ERP integrations.

- Multiple channels for notifications: Employee Role-based notifications and alerts through different omni channels like emails, messages, custom alert systems, etc.

- Pre-Processing and Privacy by design: Our Pre-processing enhances Image quality before further analysis  While  maintaining data privacy by blurring out faces and other sensitive information present in a frame.

- Intelligent Insights: Our Active Continuous Learning creates by-products in the form of intelligent insights, analytics and insightful data that helps you optimize processes and increase efficiency..

- Hassle-free Data Access: Clients can access and manage data/insights/analytics from anywhere using Cloud services. Further, we create role-based authentication systems for access to data.


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).

# **Restricted areas/times**

> Secure restricted areas with our powerful AI-based monitoring system that detects and prevents unauthorized access in real-time

# Overview
Unauthorized access to restricted zones at the workplace can lead to theft, accidents, and other security breaches. Be it valuable assets, sensitive information or providing employee safety, maintaining high-security and controlled access for restricted zones at the workplace is essential for all organizations. 

Another major problem with existing systems cannot detect intrusion after an unauthorized access has been made.This renders biometric, sensors and security personnels ineffective after an unauthorized access has been already made.



## Vision AI based monitoring

With our Vision AI monitoring you can authorize access as well as continuous monitor live feeds inside a restricted area for real-time detection of unauthorized personnel. Our fully automated detection models are not only more powerful and accurate than existing systems but also more affordable and easy to integrate into existing infrastructure allowing users to scale the power of i-based real-time detection with a few simple clicks.

<figure markdown>
  ![Image title](https://visionai.azureedge.net/docs-images/docs-visionify-version1.0-23March23/restricted-areas.png "Unauthorized entry!"){ width="350" }
  <figcaption>Detection of unauthorized entry event</figcaption>
</figure>

## Events

VisionAI model's generated events would be:

- Person detected in restricted area
- Movement detected in restricted area
- Person detected after hours
- Movement detected after hours"

It is recommended that any instance of unauthorized entry be reported to the appropriate authority.
An event data for a unauthozrized entry in exclusion zones may include information such as:

- Date and time of the event
- Location of the event
- Image of the event


## Model Details

### Dataset

The dataset consists of images and videos collected from diverse sources and is designed to reflect real-world scenarios. It is evenly distributed with:


- *Different environments*: Both indoor and outdoor with varying/contrasting surrounding and infrastructure details

- *Different angles and perspectives*: The dataset includes images captured from different angles and perspectives, such as from above, below, or from the side of subjects

- *Different modes of unauthorized access*: The dataset includes images of individuals attempting to gain unauthorized access in different ways, such as climbing over fences, breaking locks, using counterfeit credentials, or attempting to sneak past security personnel.

- *Diversity of individuals*: The dataset includes images of individuals from different genders, ages, and ethnicities, to ensure that the AI model is able to accurately detect unauthorized access attempts regardless of the individual's appearance.

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
            <td>2326</td>
            <td>v5</td>
            <td>Ceiling</td>
            <td>65% </td>
            <td>71% </td>
            <td>71% </td>
        </tr>
        </tbody>
    </table>
</div>

### Scenario details

Real-time detection and alerts for different kinds unauthorized access which includes but are not limited to:

- When an unauthorized person follows an authorized person through a secure area without proper authorization
- When an individual lingering around restricted areas without proper authorization
- Forceful entry 
- Use of counterfeit access credentials
- Unauthorized access attempts during off-hours



=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test exclusion-detection

        Downloading models for scenario: exclusion-detection
        Model: miss-fire-exting-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
        

        Starting scenario: exclusion-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of unauthorized access or forceful entry within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)



## Features

Some potential features of VisionAI for detecting missing fire extinguishers could include:

- *Lightning Fast and Response Time*: Ultra-fast Processing for real-time inference results and feedback (~30 frames per second processing) with customizable telemetry and inference results for your requirements.

- *Scalability and Instant Deployment*: Our pre-trained/custom models can be deployed instantly and are camera independent which means they can be pre-installed with existing cameras on site. 

- *Custom Integrations*: Our custom smart dashboards and real-time alert/notification systems can be tailored to fit your specific needs be it simple dashboards or complex ERP integrations.

- *Multiple channels for notifications*: Employee Role-based notifications and alerts through different omni channels like emails, messages, custom alert systems, etc.

- *Pre-Processing and Privacy by design*: Our Pre-processing enhances Image quality before further analysis  While  maintaining data privacy by blurring out faces and other sensitive information present in a frame.





## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).