# Gas Leak Detection 

> Gas leaks detection through VisionAI.

## Overview
Gas leak detection is important in industries to ensure the safety of workers, prevent damage to equipment, and minimize the risk of fires and explosions. There are several methods for gas leak detection in industries.

VisionAI Infrared Camera (IR) based solution can be used to detect gas leaks in industrial settings. They can detect gases that are invisible to the naked eye and provide real-time images of gas leaks. They can be used for leak detection in large areas, such as pipelines and storage tanks.

## Vision AI based monitoring using IR Camera

Manual inspections based on installation of fixed gas detectors and portable gas detectors can be time-consuming and labor-intensive, which can make them impractical for large or complex industrial facilities.

VisionAI's Infrared cameras detect the infrared radiation emitted by objects and can be used to visualize gas leaks that are invisible to the naked eye. The cameras can be used for leak detection in large areas, such as pipelines and storage tanks.
    



Gas leak Example            |  Gas leak Example
    :-------------------------:|:-------------------------:
    ![Gas leak](https://github.com/visionify/visionai-images/raw/main/visionai-images/gas-leak1.jpg "Detection of gas!"){ width="200" }  |  ![Gas leak](https://github.com/visionify/visionai-images/raw/main/visionai-images/gas-leak2.jpg "Detection of gas!"){ width="200" }

### Gas leak Detection using IR cameras 

![type:video](https://www.youtube.com/watch?v=GGJyRyaE6y4)
    
## Events

VisionAI model's generated events would be:
- gas leak event detected


## Configuration
It is recommended to set up Infrared cameras for gas leak detection. 
In addition, high success rate is possible if the camera is operated during periods of low wind, warm weather, clear skies and leaks are imaged from distances of about 30 feet.

## Model Details

### Dataset

IR Image dataset for gas leak detection is in progress.


### Model

The model to detect gas leak event is in progress and it will be released soon.

### Scenario details

The business logic for this scenario is as follows: 

- We use IR camera feeds from the premises to monitor the signs of leakage, spills in the workplace to ensure the safety of human lives in the workplace. 
- VisionAI system is able to run on edge devices. It uses camera feeds for processing. 
- We detect any kind of leakage in the camera feed.
- An alarming system is inplace as part of solution.



=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test gas-leak-detection

        Downloading models for scenario: gas-leak-detection
        Model: gas-leak-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
        

        Starting scenario: gas-leak-detection..

        ```
    - You should be able to see the events generated on your console window with the detections of spills and leak event within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features
Salient features of IR based gas leak detection are:
- Non-contact imaging is possible with VisionAI's infrared spectral imaging technology for gas leak detection. 

-  It can visualize the distribution of gas in addition to obtaining its spectral information. 

- The type of gas can also be determined with the aid of information. 

!!! Note

    Different gases have varying infrared absorption properties, passive infrared detection equipment can detect a range of gases. As a result, it is very important to analyse gas leaks using passive infrared imaging.

## Training with custom data
If you wish to train this scenario with custom datasets, please contact us and we can provide you with the training code. If you are interested in a custom license, please (contact us)[contact.md].


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).