# **Signs/Text blur** 

> Ensure the privacy of individuals by obscuring documents and other signs in camera feeds

<figure markdown>
  ![text blur](https://docsvisionify.blob.core.windows.net/docs-images/docs-visionify-version1.0-23March23/document-blur.png){width="400"}
  <figcaption>Text blur as part of preprocessing</figcaption>
</figure>

## Overview

Blurring documents and other signs is a common technique used to protect the privacy of individuals in images and videos.
A computer vision-based model is used in the process to make the characters unreadable.

Blurring documents can be an effective way to protect sensitive information and preserve privacy. By blurring or obscuring sensitive information on a document, you can help prevent others from accessing confidential information or using the information for malicious purposes.

There are many use cases for document blurring, where blurring or obscuring sensitive information can help protect privacy and prevent unauthorized access to sensitive data. Here are some of them:

- *Redacting personal information in legal documents*: Legal documents often contain sensitive information, such as social security numbers, addresses, and birth dates. By blurring or redacting this information, legal professionals can help protect their clients' privacy and prevent identity theft.

- *Blurring confidential business information in corporate documents*: Corporate documents, such as financial reports and contracts, often contain confidential business information. Blurring or redacting this information can help protect the company's intellectual property.

- *Blurring identifying information in online images*: Online images, including social media posts and blog articles, often include identifiable information. By blurring this information, content creators can help protect the privacy of individuals.

- *Blurring confidential information in government documents*: Government documents, including classified information and sensitive documents, often require blurring or redaction to prevent unauthorized access to confidential information.

## Vision AI-based monitoring 

Vision AI-based model for signs/document blurring can be particularly useful when sharing documents containing personally identifiable information (PII), such as social security numbers, driver's license numbers, and financial account numbers. It can also be useful when sharing documents that contain trade secrets, confidential business information, or other sensitive data that could be used to harm individuals or organizations.

The model uses a detection algorithm followed by computer vision techniques to obscure texts in images and videos. The model works in a way that it ensures that documents and signs are fully and effectively obscured so that it cannot be read or easily recovered by others.



### Dataset 

The dataset for this scenario consists of images and videos with different types of signs and documents.
It is constructed in a manner to reflect real-world intricacies.
The dataset has documents with:

- Variations in the environment
- Different types of documents
- Different types of signs
- Different distances from the camera
- Different lighting conditions
- Various camera angles and resolutions
- Using security camera feeds

### Model 

The model is based on the YOLOv5 algorithm to detect documents. Document/signs blurring is performed using computer vision-based blurring algorithms. The model is developed in a way that it generalizes well for different environments and situations.

Currently, we have document blurring model and it is based on Yolov5.

### Model card

 <div class="table">
    <table class="fl-table">
        <thead>
        <tr><th>Dataset size</th>
            <th>Version</th>
            <th>Precision</th>
            <th>Recall</th>
            <th> mAP  </th>  
        </thead>
        <tbody>
        <tr>
            <td>10k</td>
            <td>v2</td>
            <td>97% </td>
            <td>97% </td>
            <td>99% </td>
        </tr>
        </tbody>
    </table>
</div>

The model is adaptable enough to run on any edge computing device.

### Scenario details

The business logic for this scenario is as follows: 

- We use existing camera feeds from the premises to ensure the privacy of individuals.
- VisionAI system is able to run on edge devices. It uses camera feeds for processing. 
- We detect and blur the documents/signs identified in this camera feed.

=== "Test now with online Web-Cam"
     To test this model & scenario, you can use the following steps:

     - Install the visionai package from PyPI
     
        ```console
        $ pip install visionai
        
        ```
     
     - Test the scenario from your local web-cam
     

        ```console
        $ visionai scenario test text-blur

        Downloading models for scenario: text-blur
        Model: text-blur: https://workplaceos.blob.core.windows.net/models/yolov5s-licence-blur/yolov5s-text-blur-0.0.1.zip
        

        Starting scenario: text-blur..

        ```
    - You should be able to see faces being blurred as part of preprocessing.

=== "With RTSP Camera - Pipelines"
     [TODO]
 
=== "With Azure Setup"
     VisionAI app is available at a Azure Market place, one can download and use it by following steps mentioned [here](../overview/azure-managed-app.md)


For more details visit VisionAI [web application](https://visionify.ai/)

## Training with custom data

The scenario is provided as part of our GPL-v3 package for VisionAI. If you wish to train this with custom datasets, please contact us and we can provide you with the training code. You can do custom training with your own datasets for free, as long as it complies with the GPLv3 license (you give back the code to the community). If you are interested in a custom license, please (contact us)[contact.md].

## Contact Us

- For technical issues, you can open a Github issue [here](https://github.com/visionify/visionai).
- For business inquiries, you can contact us through [our website](https://visionify.ai/contact-us/).


