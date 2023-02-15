<p align="center">
  <a href="https://docs.visionify.ai"><img src="https://visionify.ai/wp-content/uploads/2020/04/Logo-03-e1617318295317.png" alt="VisionAI Platform"></a>
</p>
<p align="center">
    <em>Ready to deploy Vision AI scenarios. Open source. Try our CLI now. </em>
</p>
<p align="center">
<a href="https://github.com/visionify/visionai/actions/workflows/codeql.yml" target="_blank">
    <img src="https://github.com/visionify/visionai/actions/workflows/codeql.yml/badge.svg" alt="CodeQL">
</a>
<a href="https://github.com/visionify/visionai/blob/main/.github/workflows/docs.yaml" target="_blank">
    <img src="https://github.com/visionify/visionai/actions/workflows/docs.yaml/badge.svg" alt="Documentation">
</a>
<a href="https://dev.azure.com/visionify/workplace-safety/_build/latest?definitionId=5&branchName=main" target="_blank">
    <img src="https://dev.azure.com/visionify/workplace-safety/_apis/build/status/visionify.visionai?branchName=main" alt="Build">
<a href="https://pypi.org/project/visionai" target="_blank">
    <img src="https://img.shields.io/pypi/v/visionai?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
</p>

---

**Documentation**: <a href="https://docs.visionify.ai" target="_blank">https://docs.visionify.ai</a>

**Source Code**: <a href="https://github.com/visionify/visionai" target="_blank">https://github.com/visionify/visionai</a>

---

# VisionAI

**VisionAI** provides a set of command line utilities for you to manage different Vision AI scenarios that have been pre-developed and pre-tested. **VisionAI** focuses on workplace health and safety models - and majority of the models you see here have been developed with that in mind.

These are *production-ready* model trained from open-source and academic datasets. We are continuously working on new scenarios - and our current scenario repo consists of over 60 scenarios that are listed [here](scenarios/index.md). They are developed with the intent of being easy-to-use for business. The framework also supports a whole bunch of [custom scenarios](TODO/custom-scenarios.md).

## Install **VisionAI**

Install **VisionAI** application through `PyPI`. There are other options available for install - including a Docker container option. These are detailed in [installation](TODO/install.md) section.

```console
$ pip install visionai
---> 100%
Successfully installed visionai

✨ You are all set to use visionai toolkit ✨
```

## Deploy to **Azure**

Deploy a fully configured and tested solution directly from Azure Marketplace. **VisionAI** runs computer vision models, most of which run orders of magnitude faster if executed on a GPU machine. Our Azure Marketplace offer **VisionAI Community Edition** is available through Azure Marketplace [here](https://azure.microsoft.com) (TODO). The community edition deploys a fully configured Virtual Machine with the recommended hardware and software options. Get more details [here](azure/installation.md).

![Deploy to Azure](https://aka.ms/deploytoazurebutton)

- TODO: Point to ARM template that needs to be deployed (using these [instructions](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-to-azure-button) and here is an example [JSON file](https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.storage/storage-account-create/azuredeploy.json)).

## List available **Scenarios**

**VisionAI** is organized in terms of scenarios. Consider each scenario as being a business use-case, that is solved by a combination of Machine Learning models and an inference algorithm. For example *Warn me when max occupancy of this area exceeds 80 people* is a business scenario, where as the *People detection* is an ML model.

**VisionAI** supports 60 scenarios currently and more are being added continuously. Our current focus is on Workplace Safety scenarios. Please [contact us](contact.md) if a scenario you need is not present in our repo and we will look into it.

```console
$ visionai scenarios list

------------------------------------------------
Privacy Suite
blur-faces
blur-text

Fire safety
early-smoke-and-fire-detection
smoking-and-vaping-detection

Personnel safety
ppe-detection
pfas-system-detection
railings-detection

Suspicious activity
shipping-activity-detection
agressive-behaivior


Compliance Policies
max-occupancy

Equipment
rust-and-corrosion-detection

IR Camera
temperature-monitoring
------------------------------------------------

✨ More scenarios are added regularly ✨
```


## Get details for a **Scenario**

You can get details about a scenario using `visionai scenario details` command. Specify the scenario you want additional details for. The details of a scenario include the dataset size, model accuracy metrics,

```console
$ visionai scenario --name early-smoke-and-fire-detection details

------------------------------------------------
Category: Fire safety
Scenario: early-smoke-and-fire-detection
This scenario has been trained on open-source datasets consisting of 126,293 images. The datasets images are primarily outdoors (70%), but do contain a good number of indoor images (30%). There is a ~50-50% mix of day vs night images. You can find more details about this scenario at visionify.ai/early-smoke-and-fire-detection.


Model: smoke-and-fire-detection-1.0.1.pt
Model size: 127MB
Model type: Object Detection
Framework: PyTorch

Model performance:
Dataset size: 126,293 images
Accuracy: 94.1%
Recall: 93%
F1-Score: 93.5%

Events:
smoke-detected  | Immediate
fire-detected   | Immediate

Event examples:
{
    "scenario": "smoke-and-fire-detection",
    "event_name": "smoke-detected",
    "event_details": {
        "camera": "camera-01",
        "date": "2023-01-04 11:05:02",
        "confidence": 0.92
    }
}
------------------------------------------------

```

## Run a **Scenario**

Use `visionai run` command to run a scenario. In its simplest sense, you can run a single scenario on your web-cam. In a more complex use-case, you can specify a pipeline of scenarios, configure notification logic for each scenario, timings for each scenario etc.

```console
$ visionai run --scenario early-smoke-and-fire-detection --camera OFFICE-01

Starting early-smoke-and-fire-detection
...

```

## Install **Web App**
Use `visionai install web` command to install webapp. It will clone latest docker image from docker hub `visionify/visionaiweb`. Use `visionai web --help` for to get insigt about webapp.



## Next **steps**

Congratulations! You have successfully run the first scenario. Now go through [Tutorials](tutorials/index.md) to learn about how to run multiple scnearios, how to configure each scenario for the events you need, how to set up the dependencies etc.

Or you can also go through our [scenarios](scenarios/index.md) page to explore the different scenarios available and their model details. If you have a need for a scenario to be implemented, do not hesitate to submit a [request](https://github.com/visionify/visionai/issues).

