# Authorized Personnel


> An intelligent way to enhance security and prevent unauthorized access to restricted areas.

# Overview

Unauthorized entry or access refers to any member of the public other than employees entering areas of the restricted business premises or a warehouse. This could be done by an individual, a group of people, visitors or children/pets wrongly entering a restricted area. There can be different ways in which a security breach can happen and an unauthorized access can pose various risks;

- Safety risk
- Security risk
- Risk of non-compliance
- Risk of injury

It is important for organizations to maintain security and controlled access at the workplace. However, conventional surveillance methods are often complex, human-oriented, expensive and challenging to automate. In addition, the existing solutions cannot detect intrusion after an unauthorized entry has taken place.


## Vision AI based monitoring

Make your workplace safer and smarter with our VisionAI monitoring, a complete solution that helps you enforce security policy adherence and deter intruders effectively. Now, you can easily detect any attempts to gain unauthorized access with our fully automated system that guards your facility 24/7 and sends instant alerts to help you prevent a security breach before it occurs. 

Our system offers reliable detection and is easy to integrate with your existing camera infrastructure, allowing you to scale your system with a few simple clicks.

## Events

VisionAI model's generated events would be:

- Children detected in area
- Visitors detected in area
- Person without uniform detected
- Person without badge detected

It is recommended that any instance of above detected events be reported to the appropriate authority.
An event data for this scenario has information such as:

- Date and time of the event
- Location of the event
- Type of personnel identified


## Model Details

### Dataset

The dataset comprises relevant, high-quality, labeled videos and images from diverse sources.
The dataset is evenly distributed and balanced with an equal number of examples for each category to avoid bias toward one class.
It contains variations with different real-world scenarios to render effective and efficient results.


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
Our VisionAI solution for access control protects against unauthorized access and physical security incidents before they occur. Different scenarios of unauthorized access have been taken into account for real-time detection and alerts which include;

- Visitors detected in the area
- Employees without uniform trying to gain access 
- Employees without badges trying to enter the premise 
- Children/pets wrongly entering restricted areas



=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test auth-personnel-detection

        Downloading models for scenario: auth-personnel-detection
        Model: miss-fire-exting-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
        

        Starting scenario: auth-personnel-detection..

        ```
    - You should be able to see the events generated on your console window with authorized personnel identified within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)



## Features

Some potential features of VisionAI for identifying authorized personnel could include:
- Improved safety and security
- Enhanced visual monitoring of each entry and exit point across all locations
- Remotely monitor and instantly investigate any security concerns taking place even after working hours
- Immediately get notified of potential physical security breaches, address them quickly and operate effectively.


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact-us/).