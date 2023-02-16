# How it works

**VisionAI** provides a set of command line utilities and a lot of pre-trained models for Workplace Safety and Compliance policies. It is organized into the following commands:

- **camera**: Create a named instance for a `camera`. A camera can be an IP camera or a USB camera. Once you have addedd a camera to the system, you can can refer to it by its named instance.
- **scenario**: Scenarios are pre-built VisionAI use-cases that include a pre-trained models. You can browse scenarios, look at scenario details and download models necessary for a camera using the `scenario` commands.
- **pipelines**: Pipelines provide a way to orchestrate running multiple scenarios for a camera. A pipeline can contain multiple scenarios and you can also configure the order in which the scenarios are run (sequential or parallel). A pipeline can be applied to a single camera or multiple cameras.
- **models**: Models are pre-trained deep learning models that can be used to detect objects in an image. You can browse models, look at model details and download models using the `models` commands.
- **web**: Web provides a web interface for viewing the results of the scenarios and pipelines. They can also be used to bypass all the CLI commands and just deal with the  You can view the results of the scenarios and pipelines in a web browser. You can also configure the web interface to send alerts to a Slack channel.

