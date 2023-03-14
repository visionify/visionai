
# **Working at Heights** 

> Ensure the safety of employees at workplace.

![Detection of slip and fall while working at heights](../img/workingatheights_collage.png)

Working at heights is a hazardous activity and has the potential to cause serious injuries or fatalities. It is important for employers to ensure that the work place is set up to prevent employees from falling off of elevated surfaces. Employers must provide proper training and equipment to employees who work at heights and must ensure that safety regulations are followed. Employers should also provide periodic reviews to ensure that employees are following safety protocols and that the work environment is safe and secure.

Working at heights, such as on a roof or in a tall building, requires specialized safety equipment and training to ensure the safety of the workers. Depending on the job, you may need to wear a safety harness or other protective gear.

Falling from heights is a serious hazard, and can result in serious injury or even death. Timely action in the event of a Fall/Slip accident can minimize damage and save lives.



## Vision AI based monitoring 

Vision AI-based system can be used to detect slip and fall with high accuracy. Additionally, our model trained on real-world images minimizes false-positives or false-negatives.  

The cameras scan every frame to ensure there are no accidents related to slip and fall cases. 

To ensure accuracy and reliability for the model, these camera-based monitoring services should be supplemented by strong compliance processes. Furthermore, workers working in different factory units should always be made aware of these accidents and how to safeguard them. 

## Model Details 

### Dataset 

Model training is carried out with Microsoft COCO: Common Objects in Context dataset. Only person class is considered for model building. COCO is a  large-scale dataset that addresses three core research problems in scene understanding: detecting non-iconic views (or non-canonical perspectives of objects), contextual reasoning between objects and the precise 2D localization of objects. 

COCO dataset has an even distribution of: 

- Different(indoor/outdoor) environments 

- Male vs Female  

- Different light settings 

- Variations in camera orientations 

- Using security camera feeds 

### Model 

The model is built using Yolov5 pre-trained model for detecting a person followed by a media pipe library used to estimate the pose of the person. The following performance metrics are recorded: 


<div class="table">
    <table class="fl-table">
        <thead>
        <tr><th>Model Name</th>
            <th>Precision</th>
            <th>Recall</th>
            <th> mAP  </th>  
        </thead>
        <tbody>
        <tr>
            <td>SLIP AND FALL DETECTION</td>
            <td>65.0% </td>
            <td>71.6% </td>
            <td>71.0% </td>
        </tr>
        </tbody>
    </table>
</div>



The model is adaptable enough to run on any edge computing device.


### Scenario details


The business logic for this scenario is as follows: 

- We use existing camera feeds from the premises to monitor and detect occurrences of slip and fall incidents. 

- VisionAI s able to run on edge devices. It uses camera feeds for processing. 

- We detect human poses to identify slip and fall accidents in the camera feed.  
- If either slip or fall is detected, an alert is raised.

## Try it now 

### Quick method - using your local web-cam

To test this model & scenario, you can use the following steps:

- Install the visionai package from PyPI

<div class=termy>

```console
$ pip install visionai
---> 100%
```
</div>

- Test the scenario from your local web-cam

<div class=termy>

```console
$ visionai scenario test slip-and-fall-detection

Downloading models for scenario: slip-and-fall-detection
Model: slip-and-fall-detection: https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
---> 100%

Starting scenario: slip-and-fall-detection..

```
</div>


- You should be able to see the events generated on your console window with slip and fall being detected within the camera field of view.

### In an actual environment

To use this scenario in an actual environment, you can follow these steps:

- Install the visionai package from PyPI

<div class=termy>

```console
$ pip install visionai
---> 100%
```
</div>

- Download the scenario

<div class=termy>

```console
$ visionai scenario download slip-and-fall-detection

Downloading models for scenario: slip-and-fall-detection
Model: slip-and-fall-detection
https://workplaceos.blob.core.windows.net/models/yolov5s-people/yolov5s-people-0.0.4.zip
---> 100%
```

</div>

- Add the camera feed to the scenario

<div class=termy>

```console
$ visionai camera add OFFICE-01 --url rtsp://192.168.0.1/stream1
$ visionai camera OFFICE-01 add-scenario slip-and-fall-detection
$ visionai run

Starting scenario: slip-and-fall-detection..

```

</div>

- You should be able to see the events generated on your console window with slip and fall being detected within the camera field of view.

For more details visit VisionAI [web application](https://visionify.ai/).


## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please (contact us)[contact.md].


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).