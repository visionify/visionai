# **Energy Conservation**

> Going Green: Innovative Solutions for Energy Conservation and Sustainable Living with Vision AI.

<figure markdown>
  ![Energy Conservation](https://visionai.azureedge.net/docs-images/docs-visionify-version1.0-23March23/energy-conservation.png "Energy Conservation at work-place!"){ width="350" }
  <figcaption>Energy conservation event</figcaption>
</figure>

## Overview

Energy conservation refers to the practice of reducing energy consumption and waste, in order to minimize the impact on the environment and lower energy costs. Artificial intelligence (AI) techniques can be used to optimize energy consumption, by analyzing data and identifying patterns that can be used to improve energy efficiency.

One application of AI in energy conservation is in the development of smart grids, which use sensors and other monitoring technologies to collect data on energy consumption and distribution. AI algorithms can then be used to analyze this data and identify ways to optimize energy usage, such as by adjusting power generation and distribution to match demand.

Another application of AI in energy conservation is in the development of smart buildings, which use sensors and other monitoring technologies to optimize energy usage within a building. AI algorithms can analyze data on factors such as temperature, occupancy, and lighting levels, and adjust energy usage accordingly to minimize waste and reduce costs.

Overall, the use of AI techniques in energy conservation is an important area of research and development, with the potential to significantly reduce energy consumption and promote sustainable living. As AI technology continues to evolve, it is likely that we will see even more innovative solutions for energy conservation and environmental sustainability in the years to come.

## Vision AI based monitoring

Vision AI based monitors can be used for the detection of energy conservation events by providing real-time video feeds of the factory area. The cameras scan every frame and monitor energy consumption and identify opportunities for energy conservation. For example, computer vision can analyze building occupancy patterns to optimize heating and cooling systems, identify lighting fixtures that consume excessive energy, or identify appliances and equipment that need to be replaced to improve energy efficiency.

## Events
VisionAI model's generated events would be:

- Occupancy pattern summary & lighting pattern recommendations


## Model Details

### Dataset
The dataset for this scenario is based on real-world detection of energy conservation events.
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
            <td>72,20</td>
            <td>v1</td>
            <td>Ceiling</td>
            <td>95% </td>
            <td>93% </td>
            <td>85% </td>
        </tr>
        </tbody>
    </table>
</div>


### Scenario details

The business logic for this scenario is as follows:

- We use existing camera feeds from the premises for raising energy conservation events.
- VisionAI system is able to run on edge devices. It uses camera feeds for processing.
- From the camera feed monitor energy consumption and identify opportunities for energy conservation. For example, computer vision can analyze building occupancy patterns to optimize heating and cooling systems, identify lighting fixtures that consume excessive energy, or identify appliances and equipment that need to be replaced to improve energy efficiency.
- If energy conservation event is detected, an alert is raised.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:
     
     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test energy-conservation

        Downloading models for scenario: energy-conservation
        

        Starting scenario: energy-conservation..

        ```
    - You should be able to see the events generated on your console window with the detections of energy conservation within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features


The VisionAI solution is the most efficient way of implementing this scenario, as evidenced by the following features:

- **Real-time monitoring** - VisionAI can be used to monitor energy conservation events in real-time, using camera feeds from the premises.

- **Edge computing** - VisionAI can be deployed on edge devices, such as Raspberry Pi, to monitor energy conservation events in real-time, using camera feeds from the premises.

- **Cloud computing** - VisionAI can also be deployed on cloud servers, such as AWS, to monitor energy conservation events in real-time, using camera feeds from the premises.

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please (contact us)[contact.md].


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).