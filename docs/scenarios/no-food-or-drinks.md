# **No Food, No Drinks**

> An easier, smarter way to enforce policies with VisionAI

<figure markdown>
  ![Image title](https://github.com/visionify/visionai-images/raw/main/visionai-images/no-food-or-drinks.jpg "Detection of food and drinks at work-place!"){ width="350" }
  <figcaption>Event: No food, No drinks</figcaption>
</figure>

## Overview

Implementing a ‘No Food, No Drinks’ policy can be challenging. However, for some industries like healthcare, manufacturing, textiles, laboratories and pharmaceuticals, it is imperative to have an effective ‘no food, no drinks’ policy to maintain strict hygiene and safety standards essential to prevent product contamination. Unfortunately, the current mechanisms rely on manual inspections, are highly human-oriented, and are difficult to automate, depending on enforcement by supervisors and security personnel.

Manual inspections can be inconsistent and subjective. Also, humans are prone to errors; they may miss food or drink items that are not easily visible. Furthermore, manual inspections may not be able to cover all areas of the workplace, and they can create privacy concerns for employees. All these factors can compromise the effectiveness of the policy and may lead to non-compliance.

## Vision AI based monitoring

Implement VisionAI solution to address these problems by providing consistent, objective, and cost-effective enforcement while minimizing privacy concerns. Our smart solution seamlessly integrates with your existing camera infrastructure to capture all areas where food and drinks may be present. The model works by detecting and identifying individuals carrying or consuming foods or beverages. In addition, the model is trained to recognize different types of foods and drinks and the actions associated with consuming them, such as holding a cup or bottle and lifting it to the mouth, chewing, swallowing etc.

The model analyzes the video feed in real-time and works with the greatest accuracy. It instantly alerts the appropriate personnel to take action and proves to be an effective tool for enforcing a ‘no food and drinks’ policy in an organizational setting, improving hygiene and safety measures, and ensuring compliance with regulations.


## Model Details

### Dataset

The dataset consists of images and videos collected from diverse sources and is designed to reflect real-world scenarios. The dataset is representative of the types of people, settings, and situations where the policy will be enforced. It is evenly distributed with:
 
- Different locations: Different locations within an industrial setting where food and drinks are not allowed, like production areas, offices or workstations, and storage areas, have been considered within the dataset.
 
- Different angles and perspectives: The dataset includes images captured from different angles and perspectives, such as a front-facing view to have a clear view of the person for any food item they may be carrying, a top-down view for when the person is seated or when food or drinks are on a table, side view, low/high angle view and oblique view to detect from a diagonal or slanted perspective. An oblique view is useful when carrying food or drinks in a bag or container.
 
- Different lighting conditions: The dataset includes images of lighting conditions, like where the food items are partially visible or obstructed.
 
- Different versions: The images in the dataset have variations in the appearance of people, food, and drinks, so the model can learn to recognize them in different contexts.

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
            <td>3220</td>
            <td>v1</td>
            <td>Both(Ceiling and Straight)</td>
            <td>75.0% </td>
            <td>81.6% </td>
            <td>84.0% </td>
        </tr>
        </tbody>
    </table>
</div>


### Scenario details

Our VisionAI solution for detecting food items and drinks works in different scenarios within an industrial setting. Our model can be deployed at the entrance/exit points or inside to monitor and see whether employees or visitors carry food items or beverages. The model is equipped to detect the following:
- Person carrying a food item
- Person carrying any beverage
- Any spill event taking place within the specified area

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test no-food-or-drinks

        Downloading models for scenario: no-food-or-drinks
        Model: no-food-or-drinks: https://workplaceos.blob.core.windows.net/models/yolov5s-no-food-or-drinks/yolov5s-no-food-or-drinks-0.0.1.zip
        

        Starting scenario: no-food-or-drinks..

        ```
    - You should be able to see the events generated on your console window with detection of food items and drinks within the camera field of view.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


## Features

- Real-time monitoring: The model analyzes the video feed in real-time and works with the greatest accuracy. It is an effective tool for enforcing a ‘no food and drinks’ policy in an organizational setting, improving hygiene and safety measures, and ensuring compliance with regulations.

- Cost-effective: The model is cost-effective and does not require any additional hardware or software. It can be deployed with existing camera infrastructure.

- Privacy: The model is designed to protect the privacy of employees and visitors. It does not capture or store any personal information, and it does not require any personal information to be provided by the user.

- Customizable: The model can be customized to suit the needs of the user. It can be trained with custom data to detect and recognize different types of food items and drinks.



## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with GPLv3 license (you give back the code to the community). If you are interested in a custom license, please [contact us](../company/contact.md).


## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact).
