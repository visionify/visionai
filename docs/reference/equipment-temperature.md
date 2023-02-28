# Equipment Temperature Monitoring

> IR Camera based scenario. For critical machines, which can overheat and cause problems - monitor temperatures continually - and notify when anomalous temperatures are detected. Some times event small durations of high temperatures may indicate that something is wrong - or cause more wear for the machines in the long run

TODO: Provide an overview

## Vision AI based monitoring

!!! Note TODO: Continuous equipment temperature monitoring.
    How Vision AI can help with this
    Set up thresholds what areas we are monitoring.
    Set up event thresholds of how often we should be informed.
    Put some images & diagrams for different machines & industry use-cases here.
    
## Events

!!! Note TODO: Event details
    What type of events are generated.
    What is the frequency of thse events
    What is the event data which is sent out.

## Configuration

!!! Note TODO: Configuration
    How to configure this scenario.
    Cameras can see an area, mark areas where exits are present.


## Model Details

### Dataset

TODO:

- Indoor vs Outdoor environments
- Male vs Female
- Day vs Night
- Different types of clothing
- Different distances from the camera
- Various lighting conditions
- Various camera angles and resolutions
- Using seurity camera feeds


### Model

TODO: mode metrics.

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
            <td>PERSON DETECTION</td>
            <td>84.0% </td>
            <td>85.1% </td>
            <td>81.5% </td>
        </tr>
        </tbody>
    </table>
</div>

and landmark detection model gives the following metrics:


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
            <td>LANDMARK DETECTION</td>
            <td>84.0% </td>
            <td>72.8% </td>
            <td>84.9% </td>
        </tr>
        </tbody>
    </table>
</div>

The model is light-weight enough to be run on any edge devices.

### Scenario details

TODO: Enforcement scenarios. How to configure & use this scenario.

TODO: Implement these as multi-tab content views.
- Test now with online Web-Cam
- With RTSP Camera - Pipelines
- With Azure Setup



## Features

TODO: List of features here. Highlight why this is the most efficient way to implement this.


## Training with custom data

The scenario is provided as part of our GPL-v3 Open-Source package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please (contact us)[contact.md].


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).