# **Shipping Activity Detection**

> Stay vigilant even after hours with our advanced suspicious shipping activity solution.

<figure markdown>
  ![Shipping activity detection](https://visionai.azureedge.net/docs-images/docs-visionify-version1.0-23March23/suspicious-shipping.png "Suspicious shipping activity detection at workplace!"){ width="350" }<figcaption>Detection of suspicious shipping activity event</figcaption>
</figure>

## Overview

Shipping activity detection refers to the use of technology to identify and monitor shipping activity that may be indicative of illicit activity. Shipping activity detection technologies may include sensors, cameras, and other monitoring systems that can detect and track shipping activity. Some of these technologies can be integrated with machine learning and artificial intelligence (AI) algorithms to analyze data and identify patterns of behavior that may be indicative of suspicious shipping activity.

Shipping activity detection technologies can be used in a variety of settings, including ports, harbors, and other areas where shipping activity may occur. These technologies can help identify potential security threats, such as vessels that may be carrying weapons or engaging in suspicious activities.

The Suspicious shipping activity detected from non-designated area and during after-hours model is an important tool to identify potential threats and take appropriate action to mitigate risks.

## Vision AI based monitoring

VisionAI's shipping activity detection solutions can be used to for the detection of suspicious shipping activity events by providing real-time video feeds of the shipping area. The cameras scan every frame and raise an event when a suspicious entry detected from an usually closed location or during off-hours and/or for extended duration of time.

Suspicious Shipping Activity Detection model is an important tool for helping to prevent fraudulent or criminal activity in the shipping industry, and it works in real time to help ensure that potentially suspicious activity is identified and addressed as quickly as possible.


## Model Details

### Dataset
The dataset of Suspicious shipping activity detected from non-designated area and during after-hours is a collection of data points that provide insights into potential illicit activities taking place in the shipping industry. 
One key feature of this dataset is the inclusion of information on shipping activity outside of designated areas and during after-hours. These factors are often indicators of suspicious behavior, as they suggest that the vessel is attempting to avoid detection and operate outside of normal shipping patterns. By analyzing this data, security personnel can identify potential threats and take appropriate action to prevent harm.

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
            <td>4126</td>
            <td>v5</td>
            <td>Both(Ceiling and Straight)</td>
            <td>84.0%</td>
            <td>87.5%</td>
            <td>81.4%</td>
        </tr>
        </tbody>
    </table>
</div>

### Scenario details

Our VisionAI solution for Suspicious shipping activity detection works in different scenarios.

- The model works by continuously monitoring shipping data from various sources and then analyzes the data to identify patterns and anomalies that may be indicative of suspicious activity.

- The model may flag a shipment as suspicious if it originates from a non-designated area or if it is being shipped during after-hours.

- Once the model identifies a potentially suspicious shipment, it can trigger an alert to notify relevant personnel or authorities, who can then 
investigate further and take appropriate action as needed.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test shipping-activity-detection

        Downloading models for scenario: shipping-activity-detection
        Model: shipping-activity-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-shipping-activity-detection/yolov5s-shipping-activity-detection-0.0.1.zip
        

        Starting scenario: shipping-activity-detection..

        ```
    - You should be able to see the information generated on your console window with suspicious shipping activity detection events within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)

## Features

- Real-time monitoring: The solution is designed to monitor shipping data in real-time, allowing for rapid detection and response to suspicious shipping activity. 

- Alert system: The model is programmed to send alerts or notify the security personnel in case of any suspicious shipping activity.

- Easy to deploy: The solution can be deployed easily with minimal effort and can be integrated with the existing camera infrastructure.

- Customizable: The solution can be customized to meet the specific requirements of the organization.


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact-us/).
