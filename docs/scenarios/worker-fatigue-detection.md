
# **Worker Fatigue Detection**

> Stay alert, stay safe with our advanced worker fatigue detection model.

<figure markdown>
  ![Image title](https://visionai.azureedge.net/docs-images/docs-visionify-version1.0-23March23/worker-fatigue-detectoin.jpg "Fatigue detection at workplace!"){ width="350" }<figcaption>Worker fatigue detection event</figcaption>
</figure>

## Overview

Fatigue can have a significant impact on a person's performance, productivity, and safety. Fatigue is a state of physical or mental exhaustion that can result from prolonged periods of work, inadequate rest, or sleep disturbances. When workers are fatigued, they may experience a range of symptoms, such as slower reaction times, decreased alertness and vigilance, impaired decision-making, and reduced coordination and motor skills. These symptoms can increase the risk of accidents, injuries, and errors in the workplace, particularly in high-risk industries such as transportation, aviation, and mining. 


## Vision AI based monitoring

VisionAI based monitoring is an effective approach for fatigue detection because it allows for non-intrusive and continuous monitoring of individuals. These systems can monitor various facial and eye movements, such as eyelid closure, head drooping, yawning, and pupil dilation, to detect changes in behavior that may indicate fatigue. And its ability to provide real-time alerts and warnings to individuals and operators when signs of fatigue are detected. This can help prevent accidents and improve safety in high-risk environments. 

Overall, visionAI based monitoring is an effective and non-intrusive approach for fatigue detection, with potential applications in a range of industries and environments. By using advanced computer vision techniques and machine learning algorithms, visionAI systems can help improve safety, productivity, and overall well-being in the workplace. 

## Model Details

### Dataset

The dataset for this scenario is based on real-world posture, behavior, and movements and also to detect signs of fatigue, such as slouching, yawning, or slowing down in work events. The dataset consists of images and videos collected from various sources. 

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
            <td>1845</td>
            <td>v1</td>
            <td>Straight</td>
            <td>95% </td>
            <td>93% </td>
            <td>85% </td>
        </tr>
        </tbody>
    </table>
</div>

### Scenario details

The business logic for this scenario is as follows: 

- We use existing camera feeds from the premises to monitor the safety of its workers who operate heavy machinery, particularly during long shifts. These systems can monitor various facial and eye movements, such as eyelid closure, head drooping, yawning, and pupil dilation, to detect changes in behavior that may indicate fatigue.

- VisionAI system is able to run on edge devices. It uses camera feeds for processing. 

- We detect signs of fatigue such as slouching, yawning, or slowing down in work and alert the worker to take a break or switch with another worker, in the camera feed. 

- An alarming system is in place as part of an worker fatigue detection solution. 

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test worker-fatigue-detection

        Downloading models for scenario: worker-fatigue-detection
        Model: worker-fatigue-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-worker-fatigue-detection/yolov5s-worker-fatigue-detection-0.0.4.zip
        

        Starting scenario: worker-fatigue-detection..

        ```

    - You should be able to see the events generated on your console window with the detections of worker fatigue event within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)




## Features

- Real-time monitoring: Worker fatigue detection model is capable of real-time monitoring of workers' fatigue levels. This means that it is be able to detect signs of fatigue as they occur, rather than relying on post hoc analysis.

- Alert system: The model is able to alert supervisors or managers when a worker's fatigue level exceeds the threshold. This can be in the form of an automated alert or a visual warning on a dashboard.

- Customization: The model should be customizable to the specific needs of the workplace, including factors such as lighting, noise levels, and work schedules, which can all impact the detection of worker fatigue.

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).
