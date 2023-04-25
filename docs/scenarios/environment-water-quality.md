# Water Quality Monitoring

>Advanced Technologies for Effective Water Management and Conservation with Vision AI.



## Overview

Water quality monitoring is the process of testing and analyzing water samples to determine if the water meets certain quality standards or if it contains harmful substances that could pose a risk to human health or the environment. Water quality monitoring is important for ensuring that water is safe to drink, swim in, or use for other purposes.

There are many different factors that can affect water quality, including the presence of bacteria, viruses, heavy metals, pesticides, and other pollutants. Water quality monitoring typically involves collecting water samples from various locations, such as rivers, lakes, and groundwater sources, and testing them for various contaminants.

Overall, water quality monitoring is a critical part of ensuring that our water resources remain safe and healthy for both people and the environment.

## Vision AI based monitoring

Water quality monitoring by VisionAI's camera based approach involves using cameras to capture images or videos of water bodies and then analyzing them to determine the water quality. This approach can provide a cost-effective and efficient way to monitor water quality over a large area, as cameras can cover a wide range of locations and can operate continuously.

There are several ways in which *cameras* can be used for water quality monitoring. For example, cameras can be used to capture images of water bodies to detect changes in color or turbidity, which can indicate the presence of pollutants. They can also be used to monitor the growth of algae or other organisms, which can affect the water quality.

In addition, cameras can be equipped with *sensors* to measure various water quality parameters such as *pH, temperature, dissolved oxygen, and conductivity*. These sensors can provide real-time data on water quality, which can be used to identify trends and to alert authorities to potential problems.

 

## Events

VisionAI model's generated events would be:

- Water quality level exceeds limit

It is recommended that any instance of water quality level's exceeding should be reported.  

Event data for water quality management refers to information collected during specific events or incidents that can impact the water quality of a particular area. This data can help to identify potential sources of pollution and develop strategies to mitigate their effects.


## Model Details

### Dataset
The dataset for this scenario is based on real-world water quality management detection events.
The dataset consists of images and videos collected from various sources. 

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
            <td>95% </td>
            <td>71% </td>
            <td>71% </td>
        </tr>
        </tbody>
    </table>
</div>


### Scenario details

The business logic for this scenario is as follows:

- We use existing camera feeds from the premises for raising water management events.
- VisionAI system is able to run on edge devices. It uses camera feeds for processing.
- From the camera feed we identify opportunities for water leaks, reduce water waste, and comply with environmental regulations.
- If water quality below threshold level event is detected, an alert is raised.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:
     
     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test water-quality-detection

        Downloading models for scenario: water-quality-detection
        

        Starting scenario: water-quality-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of water management within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features


The VisionAI solution is the most efficient way of implementing this scenario, as evidenced by the following features:

- Water quality monitoring by camera can provide a valuable tool for managing and protecting water resources. However, it is important to ensure that the cameras are installed and operated in a way that does not harm the environment or interfere with wildlife.

- Cameras can be used to monitor water quality over a wide area, which can be useful for identifying areas that are prone to flooding or other water-related problems.

- Cameras can be equipped with sensors to measure various water quality parameters, which can provide real-time data on water quality. This data can be used to identify trends and to alert authorities to potential problems.


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).