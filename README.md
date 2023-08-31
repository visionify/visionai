<p align="center">
  <a href="https://docs.visionify.ai"><img src="https://raw.githubusercontent.com/visionify/visionai/main/docs/img/visionai-toolkit-by-visionify.png" alt="VisionAI Toolkit by Visionify"></a>
</p>
<p align="center">
    <em>VisionAI Apps for Workplace Safety. Pretrained & Ready to deploy. </em>
</p>
<p align="center">
<!-- <a href="https://github.com/visionify/visionai/actions/workflows/codeql.yml" target="_blank">
    <img src="https://github.com/visionify/visionai/actions/workflows/codeql.yml/badge.svg" alt="CodeQL">
</a> -->
<a href="https://github.com/visionify/visionai/blob/main/.github/workflows/docs.yaml" target="_blank">
    <img src="https://github.com/visionify/visionai/actions/workflows/docs.yaml/badge.svg" alt="Documentation">
</a>
<a href="https://dev.azure.com/visionify/workplace-safety/_build/latest?definitionId=5&branchName=main" target="_blank">
    <img src="https://dev.azure.com/visionify/workplace-safety/_apis/build/status/visionify.visionai?branchName=main" alt="Test Status">
<a href="https://pypi.org/project/visionai" target="_blank">
    <img src="https://img.shields.io/pypi/v/visionai?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
</p>

---

**Documentation**: <a href="https://docs.visionify.ai" target="_blank">https://docs.visionify.ai</a>

---

## Overview

**VisionAI** offers a collection of pre-trained apps tailored for workplace safety use cases. Developed by **Visionify** as part of the **Workplace Safety** suite, VisionAI is ready for production deployment and accessible through web-based GUI.

### What is VisionAI?
- A Platform to run AI scenarios for CCTV cameras.
- Choose from the list of scenarios [here](scenarios/index.md) for workplace safety & building security.

### How does it work?
- Migrate CCTV feeds to the cloud. Manage cameras, choose AI scenarios and configuring alerting from cloud.

Key features of **VisionAI** include:

- **No hardware installation**: Works with any IP/security cameras using RTSP streams. No need to install any new cameras, sensors, or other hardware.

- **User-friendly**: Easy-to-use web interface for managing cameras and associated apps, catering to both technical and non-technical users.

- **Production-ready**: Apps are trained on diverse, carefully curated datasets from industrial and academic sources, ensuring out-of-the-box functionality.

- **Customizable**: Allows app customization and model fine-tuning with a flexible architecture based on the NVIDIA Triton server. Refer to customization documentation for more details.

- **Integrations**: VisionAI currently integrates with Azure Event hubs, Redis PubSub for reports, alerts and notifications. We have roadmap plans to add support for other message brokers as well.

## VisionAI Apps

VisionAI offers a variety of workplace health and safety scenarios, with continuous development of new use cases. View the complete list of VisionAI Apps [here](scenarios/index.md). If you require a specific scenario not listed here, feel free to [contact us](company/contact.md).

Our primary focus is on workplace health and safety models, but we are expanding our scope to include Quality Inspection, Food Safety/Debris Detection, and more. These additional scenarios are available to customers on a case-by-case basis.


## Quick Start

* Install **VisionAI** through `PyPI`:


```bash
$ pip install visionai
```


* Update to the latest version, if already installed:

``` bash
$ pip install --upgrade --force-reinstall visionai
```

* Initialize VisionAI to download and install dependencies (Docker, Pytorch, NVIDIA Triton, etc.):

``` bash
$ visionai init
```

* Upon successful initialization, you should be able to see the following services running:

---
| Service           | Port                     | Purpose                                         |
| :---------------- | :------------------------| :---------------------------------------------- |
| `Web UI`          | `http://localhost:3001`  | VisionAI Web-app                                |
| `Web API`         | `http://localhost:3002`  | VisionAI API service                            |
| `Triton HTTP`     | `http://localhost:8000`  | Triton Model server (http)                      |
| `Triton GRPC`     | `grpc://localhost:8001`  | Triton Model server (grpc)                      |
| `Triton Metrics`  | `http://localhost:8002`  | Triton Model metrics server (prometheus)        |
| `Redis`           | `redis://localhost:6379` | Redis server, currently supports PUBSUB         |

---



## VisionAI Web-App
- VisionAI also supports a web-based option for managing cameras, scenarios and pipeline. You can run the following command to start the web-based GUI. Once the web-based GUI is started, you can access it at http://localhost:3001.

``` bash
$ visionai web start

Web service API available at: http://localhost:3002
Web app available at: http://localhost:3001
```


- This would show an initial screen similar to this:

![VisionAI Web Application](https://raw.githubusercontent.com/visionify/visionai/main/docs/img/visionai-scenarios-web.jpg "VisionAI Web Application").

- You can manage cameras, scenarios, pipelines, see events etc., directly on the web-app. The web-app is running your own local compute instance. All the data is saved in your machine, and it is persistent as long as VisionAI application is not uninstalled.





## Next steps

Congratulations! You have successfully configured and used VisionAI toolkit. You can also browse through our [scenarios](scenarios/index.md) section to understand different use-cases that are supported currently. If you have a need for a scenario, do not hesitate to submit a [request](https://github.com/visionify/visionai/issues) here.



