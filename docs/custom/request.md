# Custom Integration

> Documentation for **VisionAI** customization

## Overview

VisionAI Toolkit provides end-to-end data customization and analytics services. We provide extensive analytics expertise, as well as domain expertise, to assist clients in transforming their businesses.

## Process

We can assist you in optimising business use-cases so that you can focus on activities that generate true business value. 

![custom integration features](https://github.com/visionify/visionai-images/raw/main/visionai-images/custom-features.PNG) 

This includes:

- *Continous Monitoring*:
We use the ease of a single web console to conveniently monitor your whole work place. We assist you in avoiding problems before they affect or are noticed by users. Using our monitoring service, learn more about:

    1. Event logs
    2. Root Cause Analysis
    3. Traffic monitoring

- *Alerts*:
Quick alerts and notifications for events (eg. accidents/non-compliance) can be send through emails/messages.


- *Reporting*:
Detailed reports can be generated for daily/monthly basis. Frequency of reports can be customized to accomodate user preferences.
Granularity depends on user's business perspective.

For example, 

1. Ensuring true compliance for Personal protective equipment(PPE) by generating instant alerts

2. Providing daily and summary reports to give in-depth insights

3. Providing flexibility by customizing different options 

Current, real-time web applications pose unique horizontal scalability challenges. 
Therefore, our current architecture uses pub/sub messaging mechanism to push events notifications to Redis/ Graffana. These can be integrated through Azure Event Grid to Azure IoT hub. An architecture to support this would be:

![Architecture](https://github.com/visionify/visionai-images/raw/main/visionai-images/architecture-custom.png) 






