# **Gas Sensors for Leakage and Air Quality Monitoring**

> Monitor CO, CO2, VOCs, NOx, SOx, O2, and Particulate matters in real-time 

## Overview

Gas leakage, equipment damage, and low air quality are significant challenges for businesses across industries. Therefore, you need advanced gas sensing devices to ensure desired air quality and minimum leakage in your facility. 

Go easy knowing that you can track and monitor the air quality in your surroundings with our wide range of gas monitoring solutions. Get yourself covered with our specialized indoor and outdoor air quality monitoring solution, including breakouts for projects detecting indoor carbon monoxide, Volatile Organic Compounds (VOCs), SO2, NOX, O2, and particulate matter.


## Vision AI based monitoring

VisionAI's sensor-powered gas detection solutions can identify CO, CO2, VOCs, NOx, SOx, O2, and particulate matter in real time. In addition, our models integrated with advanced sensors can sense gas and dust particles in the air as soon as their percentage level increases or falls below a threshold value. With a high response rate and accuracy, these solutions are your best companion for dealing with leakage and poor air quality. 

## Model Details

### Dataset

The dataset comprises relevant, high-quality, labeled images and videos from diverse sources. It is evenly distributed and balanced with equal examples from each category to deliver accurate results.

- Measure safe gas values: The dataset includes safe gas, voltage, and current output values. Based on the gas levels, you can monitor sensor pumps directly for diagnostic purposes.

- Permissible gas temperature: The dataset includes permissible gas temperature under various conditions. This temperature range varies from gas to gas and sensor to sensor.

- Indoor vs. Outdoor environments: The dataset includes images and videos of indoor and outdoor environments. The gas sensors can differentiate between the two settings and share permissible gas levels for each surrounding.

- Different types of clothing: The dataset includes images and videos of workers in different clothing with/without safety necessities like PPE kits and safety helmets.

- Flow rate: Checkout the gas flow rate and make proactive adjustments to fix it. The dataset can help you figure out what’s the best flow rate the gas should have in a particular condition.

- Various lighting conditions: The dataset contains images and videos under different lighting conditions. The model may need to adjust its settings to continue detecting leakage accurately.

- Multiple camera angles and resolutions The dataset includes images taken from different angles, such as top-down, side view, or angled view, and available in varied resolutions.



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
            <td>32,20</td>
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

- When the gas or particulate percentage of a gas surpasses or falls a threshold value, the model triggers an alarm.
- The model can be used to detect sources of leakage, fire, or elevated levels of gas within a vicinity. 
- When the equipment is faulty, and there is a high risk of an accident, the camera sensors can ring an alarm or mark safe exits with the help of VisionAI capabilities integrated with your existing setup.
- The model allows you to upload the most recent version of the baseline image onto your camera before the inspection.
- The solution can also be used to measure toxic gas concentration, smoke, and fire, and to check air quality.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test air-quality-monitoring

        Downloading models for scenario: air-quality-monitoring
        Model: air-quality-monitoring: https://workplaceos.blob.core.windows.net/models/yolov5s-air-quality-monitoring/yolov5s-air-quality-monitoring-0.0.1.zip
        

        Starting scenario: air-quality-monitoring..

        ```
    - You should be able to see the information generated on your console window with the air quality events within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)



## Features

- Real-time reporting: The model can provide real-time reporting of air quality data, so that people can take immediate action to reduce exposure to pollutants.

- Integration with other systems: The model is able to integrate with other systems, such as weather monitoring systems or emergency response systems, to provide a more comprehensive view of air quality and its impact on public health.

- Historical data tracking: To identify long-term air quality trends and patterns, air quality monitoring models may track and store historical data over extended periods of time. This can provide valuable insights into the effectiveness of environmental policies and initiatives, as well as the impact of climate change on air quality.

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).
