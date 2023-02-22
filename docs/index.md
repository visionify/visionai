# **VisionAI**

Documentation for **VisionAI** toolkit.

## Overview

**VisionAI** provides a set of command line utilities for you to manage different Vision AI scenarios that have been pre-developed and pre-tested. VisionAI focuses on workplace health and safety models and the majority of the models you see here have been developed with that keeping in mind.

These are *production-ready* models trained from open-source and academic datasets. We are continuously working on new scenarios - and our current scenario repo consists of over 60 scenarios that are listed [here](scenarios/index.md). They are developed with the intent of being easy-to-use for businesses. The framework also supports a whole bunch of [custom scenarios](scenarios/custom-scenarios.md).


VisionAI focuses on workplace health and safety which includes PPE detection, smoke-and-fire detection, rust-and-corrosion,smoking-and-vaping, phone usage detection, and slip-and-fall detection etc..,


Majorly focuses on the following areas:

![](img/WorkPlaceSafety_FocusAreas.png)


## Install **VisionAI**

Install **VisionAI** application through `PyPI`. There are other options available for install - including a Docker container option. These are detailed in [installation](install.md) section.

<div class="termy">

```console
$ pip install visionai

---> 100%

Successfully installed visionai

✨ You are all set to use visionai toolkit ✨
```

</div>



## Deploy to **Azure**

Deploy a fully configured and tested solution directly from Azure Marketplace. **VisionAI** runs computer vision models, most of which run orders of magnitude faster if executed on a GPU machine. Our Azure Marketplace offer **VisionAI Community Edition** is available through Azure Marketplace [here](https://azure.microsoft.com). The community edition deploys a fully configured Virtual Machine with the recommended hardware and software options. Get more details [here](azure/installation.md).

![Deploy to Azure](https://aka.ms/deploytoazurebutton)

- TODO: Point to ARM template that needs to be deployed (using these [instructions](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-to-azure-button) and here is an example [JSON file](https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.storage/storage-account-create/azuredeploy.json)).

## List available **Scenarios**

**VisionAI** is organized in terms of scenarios. Consider each scenario as being a business use-case, that is solved by a combination of Machine Learning models and an inference algorithm. For example *Warn me when max occupancy of this area exceeds 80 people* is a business scenario, where as the *People detection* is an ML model.

**VisionAI** supports 60 scenarios currently and more are being added continuously. Our current focus is on Workplace Safety scenarios. Please [contact us](company/contact.md) if a scenario you need is not present in our repo and we will look into it.

<div class="termy">

```console
$ visionai scenario list

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

</div>



## Get details for a **Scenario**

You can get details about a scenario using `visionai scenario details` command. Specify the scenario you want additional details for. The details of a scenario include the dataset size, model accuracy metrics.

<div class="termy">

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

</div>

## Run a **Scenario**

Use `visionai scenario test` command to run a scenario. In its simplest sense, you can run a single scenario on your web-cam. In a more complex use-case, you can specify a pipeline of scenarios, configure notification logic for each scenario, timings for each scenario etc.

![](img/Scenario_Flow.png)

<div class="termy">

```console
$ visionai scenario test smoke-and-fire-detection

Starting early-smoke-and-fire-detection
...


```

</div>



## Get **help** on commands

You can get more help on any command by adding --help at the end of the command. For example, if you want to get details about pipeline commands, you can run the following commands.

<div class="termy">

```console

$ visionai pipeline --help

 Usage: visionai pipeline [OPTIONS] COMMAND [ARGS]...

 Manage pipelines
 Pipeline is a sequence of preprocess routines and
 scenarios to be run on a given set of cameras. Each
 pipeline can be configured to run specific scenarios -
 each scenario with their own customizations for event
 notifications. This module provides robust methods for
 managing pipelines, showing their details, adding/remove
 cameras from pipelines and running a pipeline.

╭─ Options ────────────────────────────────────────────────╮
│ --help          Show this message and exit.              │
╰──────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────╮
│ add-camera      Add a camera to a pipeline               │
│ add-preprocess  Add a preprocess routine to a pipeline   │
│ add-scenario    Add a scenario to a pipeline             │
│ create          Create a named pipeline                  │
│ remove-camera   Remove a camera from a pipeline          │
│ reset           Reset the pipeline to original state.    │
│ run             Run a pipeline of scenarios on given     │
│                 cameras                                  │
│ show            Show details of a pipeline               │
╰──────────────────────────────────────────────────────────╯


```

</div>


## Why **VISIONAI** ?

VisionAI toolkit provides solutions in the form of production-ready models for various use cases focused on  workplace health and safety.

![](img/KD_WorkplaceSafety_v2.png)


## Next **steps**

Congratulations! You have successfully run the first scenario. Now go through [Tutorials](tutorials/index.md) to learn about how to run multiple scnearios, how to configure each scenario for the events you need, how to set up the dependencies etc.

Or you can also go through our [scenarios](scenarios/index.md) page to explore the different scenarios available and their model details. If you have a need for a scenario to be implemented, do not hesitate to submit a [request](https://github.com/visionify/visionai/issues). For consulting projects and custom licenses - find the details [here](custom/index.md)

