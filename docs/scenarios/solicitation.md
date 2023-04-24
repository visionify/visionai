# **Solicitation Detection**

> A smarter way to unveil solicitation

<figure markdown>
  ![Solicitation detection](https://github.com/visionify/visionai-images/raw/main/visionai-images/solicitation-detection.png "Solicitation detection at a work-place!"){ width="350" }
  <figcaption>Detection of Solicitation detection event</figcaption>
</figure>


## Overview

Solicitation is the act of requesting or offering something in return for a favor, service, or product. In industries, Solicitation can take various forms, for example, employees soliciting other employees for money in exchange for job-related favors, any outsiders approaching factory employees or workers for different purposes like obtaining confidential information, for employment etc. Solicitation can also occur in public places, including malls, hotels, casinos, public transportation, clubs, etc. However, solicitation is often prohibited in these areas due to some specific rules and regulations depending upon the location and jurisdiction. 
 
To maintain a safe work environment, sustain an organization’s values and prevent unethical behaviors within the companies and in public spaces, it is important to detect solicitation, take appropriate measures to address such behaviors and prevent it from happening. Computer Vision solutions can help effectively detect acts of solicitation before they occur.


## Vision AI based monitoring

Implement VisionAI solution to address the problems associated with Solicitation by timely detection of any unethical behaviors in public spaces or companies. Our AI and deep learning-based solution can identify behavioral anomalies that may indicate solicitation.    
 
Our smart solution seamlessly integrates with the existing camera infrastructure and analyzes the real-time video feed. It can help in different ways and offers a comprehensive solution for Solicitation;
 
- Facial recognition technology can help identify individuals involved in solicitation activities
- The algorithm can also analyze patterns of behaviors associated with solicitation, such as loitering or approaching strangers
- The algorithm also detects objects generally related to solicitation, like signs, posters, and flyers
- The algorithm can identify any unusual or suspicious behaviors in public spaces that indicate solicitation and help security and law enforcement personnel to respond more quickly to potential issues 

## Model Details

### Dataset

The dataset consists of images and videos in large numbers collected from diverse sources and is designed to reflect real-world scenarios. The dataset is representative of all types of people from different ages, genders and backgrounds engaging in solicitation behavior. Also, it includes all settings, situations and different types of solicitation behavior, such as advertising or sales pitches. It is evenly distributed with;
 
- Different locations - in public places, there are various locations where solicitation can take place, like walkways, public parks, parking lots, public transportation hubs, malls, clubs, hotels, casinos, and retail environments.
 
- Different angles and perspectives - The dataset includes images or videos captured from different angles and lighting conditions to ensure that the model can detect solicitation behavior in various real-world scenarios.
 
- Different versions - The dataset undertakes different types of solicitation to ensure the model is robust enough and can generalize well to any new situation.

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
            <td>4810</td>
            <td>v1</td>
            <td>Both(Ceiling and Straight)</td>
            <td>92.0% </td>
            <td>91.6% </td>
            <td>88.0% </td>
        </tr>
        </tbody>
    </table>
</div>


### Scenario details

Our VisionAI solution for solicitation detection works in different scenarios to detect any unethical behavior indicating solicitation within an industrial setting or in public spaces. The model is equipped to detect the following;

- Identify through facial recognition: known solicitors
- Identify a single person going and talking to multiple people
- Identify and track scantily clad persons and whether they are talking to people
- Identify similar patterns like one person repeating the same type of behavior

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test solicitation-detection

        Downloading models for scenario: solicitation-detection
        Model: solicitation-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-solicitation-detection/yolov5s-solicitation-detection-0.0.1.zip
        

        Starting scenario: solicitation-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of light sensor monitoring within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features

- Real-time monitoring: The model can be deployed in real-time to monitor the public spaces and industrial settings for any unethical behavior indicating solicitation.

- Easy to deploy: The solution can be deployed easily with minimal effort and can be integrated with the existing camera infrastructure.

- Customizable: The solution can be customized to meet the specific requirements of the organization.

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).
