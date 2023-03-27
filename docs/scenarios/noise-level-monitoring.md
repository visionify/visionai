# **Noise Level Monitoring**
> Measure the sound level in the environment and identify a noise source

## Overview

Environmental noise around work facilities can be a pain to the ears. Traffic, factories, construction, and recreational activities can generate these harmful and unwanted noises. Airports, power plants, shooting ranges, rock crushing, etc., are some other noise sources that can be heard from many kilometers away. 

Identifying the source is one of the biggest challenges in dealing with environment noise. Firstly, single-point noise measurement is insufficient to accurately locate the source or measure noise levels. Secondly, this requires a considerable amount of resources as one needs to record noise levels for extended time periods. Therefore, noise measuring instruments with advanced technology sensors can be a great tool for accurate noise identification and monitoring.


## Vision AI based monitoring

VisionAI's noise monitoring solution is integrated with sensors that can automatically validate sound sources from a distance. Our model can classify noise sources using a classification algorithm capable of learning a sophisticated noise source classifier for an arbitrary scenario just by using relevant annotated recordings as training material. 

All the extracted sound measurements are transmitted from the smart sensor to the cloud service for detailed analysis. The cloud service stores the data in the measurement database, and audio segments marked for later inspection are stored in your disk server. End-users can access the measurement data and analysis of the measurements through a web-based portal. Implement this solution to identify noise sources and prevent noise levels from exceeding a threshold value.


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).

## Model Details

### Dataset

The dataset contains crucial data collected from various sources over a considerable period. Here are some of the critical dataset items:

- Source classification: The dataset contains audio of sound sources. These data items will help you classify noise sources faster.

- Distance from the source: The sensors will be installed at multiple places from the source. This is crucial to verify the accuracy of the source and measure the noise level.

- Sound pressure level: Measure the loudest and distortion-free sound level (SPL) with the help of a vast dataset and by setting threshold values.

- Data visualization: The measurement data can be visualized in multiple ways: calendar heat-maps, graphs, and report tables are just a few of the types. 

### Model

We would be releasing the model to monitor noise level events in *Q2-2023*.

## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).
