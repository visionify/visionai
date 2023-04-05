# Scenarios

Scenarios form the building blocks of VisionAI platform. These scenarios are organized into `Suites`. Below we talk about different suites and the scenarios that are part of them.

- All scenarios are available as pick-n-choose scenarios. You can pick the scenarios you want based on your business needs. Each scenario is independently tested.
- Events provided by these scenarios are given below. Events are sent to Redis & Azure EventHub pubsub systems for [further integration](custom/events-integration.md).
- There are a few common events supported by all scenarios (daily summary, weekly summary etc.)
- Currently supported scenarios are highlighted by a ✅. Roadmap scenarios are highlighted by a 📅.
- Each of the scenarios can be quickly tested through `visionai run <scenario-name>` command. For example:

``` bash
visionai run smoke-and-fire-detection
```

---

!!! note "New scenario request"
    This section lists down all the scenarios that are supported by the VisionAI platform. There are more scenarios added daily - please [send a request](https://github.com/visionify/visionai/issues/new) to us about any additional scenarios you need.

---

## Privacy Suite

For a majority of organizations - employee privacy is a top concern. Along with employee privacy, the organization needs to make sure that any data does not leave the premises. Any faces detected through Vision AI system need to be blurred, along with text, signage, computer screens and other sensitive information.

Before any other scenarios are run, or before we store or process the images - the images are pre-processed through this privacy suite. As such, privacy suite is treated differently from other scenarios. Below examples provide a high-level overview of the privacy suite.

---

| Status | Scenario name | Details | Additional considerations |
| :----: | :------------ | :--------------- | :------------------------ |
| ✅ | `face-blurring` | Blur any faces detected | [More details](../privacy/blur-faces.md){:target="_blank"} |
| ✅ | `text-blurring` | Blue any text detected (paper, computer screens etc) | [More details](../privacy/blur-signs.md){:target="_blank"} |
| ✅ | `license-plate-blurring` | Blur any license plates detected | [More details](../privacy/blur-license-plates.md){:target="_blank"} |
| 📅 | `signs-blurring` | Blur any signs detected | [More details](../privacy/blur-signs.md){:target="_blank"} |
| 📅 | `obstructed-camera` | If camera feed is obstructed, send an alert | [More details](../scenarios/obstructed-camera-view.md){:target="_blank"} |

---


## Hazard Warnings Suite

Following scenarios provide hazard warning examples supported by VisionAI suite. Currently supported scenarios are highlighted by a ✅. You can run these through VisionAI CLI, for example, you can run the following command for smoke-and-fire-detection. Once the scenario has started - you can use a lighter or a match to generate the events. The events can be viewed on CLI window.

``` bash
visionai run smoke-and-fire-detection
```

!!! warning "TODO"
    - TODO: For scenarios requiring IR camera and/or IoT Sensor, point to the exact device this has been tested with.


| Status | Scenario name | Supported Events | Additional considerations |
| :----: | :------------ | :--------------- | :------------------------ |
| ✅ | `smoke-and-fire-detection`       | `Smoke event detected` <br> `Fire event detected` <br> `Sparks detected` <br> `Open flames detection` | [More details](smoke-and-fire-detection.md){:target="_blank"} |
| ✅ | `no-smoking-zone`                | `Smoking event detected` <br> `Vaping event detected` | [More details](no-smoking-hazard.md){:target="_blank"} |
| 📅 | `spills-and-leak-detection`      | `Water puddle detected` <br> `Water leak from equipment detected` <br> `Spill event detected` <br> `Slippery sign detected` |
| 📅 | `gas-leak-detection`             | `Gas leak event detected` | IR Camera Required |
| 📅 | `missing-fire-extinguisher`      | `Fire extinguisher missing` |
| 📅 | `blocked-exit-monitoring`        | `Blocked exit detected` |
| 📅 | `equipment-temperature-ir-camera`| `Temperature exceeds limit` <br> `Temperature subceeds limit` | IR Camera Required |
| ✅ | `rust-and-corrosion-detection`   | `Rust or corrosion event detected` | [More details](rust-and-corrosion-hazard.md){:target="_blank"} |







---

## Worker Health & Safety Suite

Following scenarios provide Worker Health and Safety examples supported by VisionAI suite. (Also referred to as Personnel Health and Safety).

Workplace Personnel Health & Safety is important because it ensures that employees are safe and healthy in their work environment. This includes providing a safe and healthy work environment, proper safety training, and regular safety inspections. Additionally, it also includes enforcing safety policies to ensure that all employees are aware of and follow safety procedures, as well as encouraging a culture of safety within the workplace.

Currently supported scenarios are highlighted by a ✅. You can run these through VisionAI CLI, for example:

``` bash
visionai run ppe-detection
```

You can see real-time events generated as soon as person is detected without PPE (helmets, gloves, safety boots etc.). There are options to configure what PPE's are required for your scenario. This can be done through the VisionAI web-application which can be accessed on through http://localhost:3001.

| Status | Scenario name | Supported Events | Additional considerations |
| :----: | :------------ | :--------------- | :------------------------ |
| ✅ | `ppe-detection` | `Person detected without helmet` <br> `Person detected without gloves` <br> `Person detected without safety boots` <br> `Person detected without safety goggles` <br> `Person detected without face mask` <br> `Person detected without vest` <br> `Person detected without full-body suit` <br> `Person detected without PFAS` <br> `Person detected without ear protection` | [More details](ppe-detection.md){:target="_blank"}
| ✅ | `working-at-heights` | `Person detected without PFAS` <br> `Steps detected without railings` <br> `Person detected at height without parapets` <br> `Ladder detected not in compliance` | [More details](working-at-heights.md){:target="_blank"}

| 📅 | `environment-monitoring` | `CO out of range` <br> `CO2 out of range` <br> `CH4 out of range` <br> `VOCs out of range` <br> `Temperature out of range` <br> `Pressure out of range` <br> `Humidity out of range` |
| ✅ | `fall-and-accident-detection` | `Person slip & fall detected` <br> `Potential collision/accident detected` <br> `Wet floor detected` <br> `Debris detected on floor` <br> `Wet/slippery sign detected` |
| ✅ | `worker-fatigue-detection` | `Drowsy worker detected` | Straight camera angle |
| ✅ | `posture-and-ergonomics` | `Bend count per individual ` | Straight camera angle <br> [More details](ergonomics.md){:target="_blank"} |
| 📅 | `empty-pallets-detection` | `Empty pallets detected` <br> `Partially empty pallets detected` |
| 📅 | `spills-and-leaks-detection` | `Water puddle detected` <br> `Water leak from equipment detected` <br> `Wet floor detected` <br> `Spill event detected` <br> `Slippery sign detected` |
| 📅 | `hand-wash-compliance` | `Missed hand wash` |

| 📅 | `person-temperature-monitoring` | `Person temperature exceeds threshold` | IR Camera required |
| ✅ | `confined-spaces-monitoring` | `Person detected` <br> `Person left` <br> `Person dwell time exceeds limit` <br> `Person detected without motion` <br> `Person fall detected` | [More details](confined-spaces-monitoring.md){:target="_blank"} |



---

## Occupancy Policies

Occupancy Policies relate to counting and tracking employees and/or other personnel in the room. These could include people-counting and enforcing max-occupancy policies, or tracking people's dwell time in a confined space.

Currently supported scenarios are highlighted by a ✅. You can run these through VisionAI CLI, for example:

``` bash
visionai run max-occupancy
```

!!! note "Occupancy Metrics"
    - Occupancy metrics is similar in structure to max-occupancy, or restricted areas scenarios.
    - However it sends out a summary event is structured like this. This will give a granular summary event at the end of the day.
    - Users can start with occupancy-metrics and then move to max-occupancy or restricted areas if they need to enforce policies.
    ``` json
    {
      "date": "2023-02-23",
      "stations": [{
        "id": "station_1",
        "hours": [
            {
              "start_time": "2023-02-23T14:00:01",
              "end_time": "2023-02-23T15:00:00",
              "occupancy_cnt": 14
            }
            ...
        ]
      }...]
    }
    ```

Also need to specify that the camera needs to be configured to have a good view of the stations where occupancy metrics need to be checked.

| Status | Scenario name | Supported Events | Additional considerations |
| :----: | :------------ | :--------------- | :------------------------ |
| ✅ | `max-occupancy`              | `Person count exceeds max limit` | [More details](max-occupancy-count.md) |
| ✅ | `restricted-areas`           | `Person detected in restricted area` <br> `Movement detected in restricted area` <br> `Person detected after hours` <br> `Movement detected after hours` | [More details](exclusion-zones.md){:target="_blank"} |
| ✅ | `dwell-time`                 | `Person detected` <br> `Person left` <br> `Person dwell time exceeds limit` <br> `Person detected without motion` <br> `Person fall detected` | [More details](confined-spaces-monitoring.md){:target="_blank"} |
| 📅 | `social-distancing`          | `Person detected` <br> `Person left` <br> `Person distance event` |
| ✅ | `station-occupancy`          | `Daily summary event` | [More details](station-occupancy.md){:target="_blank"} |
| 📅 | `occupancy-metrics`          | `Daily summary event` |
| 📅 | `authorized-personnel-only`  | `Unauthorized person detected` |

| ✅ | `badge-tailgating`         | `Multi-entry (tailgating) event detected` <br> `Unauthorized entry event detected` | [More details](unauthorized-entry.md){:target="_blank"} |
| ✅ | `perimeter-control`          | `Person detected near fence/perimeter` <br> `Movement detected near fence/perimeter` | IR camera required<br>[More details](perimeter-control.md){:target="_blank"} |




[^1]: This works by detecting a person's uniform and comparing it to a list of authorized personnel. This is a more advanced scenario and requires a custom model to be trained for your specific use-case.

---

## Company Policies

Company policies include specific scenarios that are relevant to your company. These could include scenarios like no-smoking/no-vaping zones, no food or drinks in certain areas, or no cell phones/pictures in certain areas. Some of these scenarios overlap with [occupancy policies](#occupancy-policies), but they are still useful to have here as separate scenarios.

| Status | Scenario name | Supported Events | Additional considerations |
| :----: | :------------ | :--------------- | :------------------------ |


| 📅 | `no-food-or-drinks-allowed`  | `Person with food detected` <br> `Person with drinks detected` <br> `Spill event detected` |
| ✅ | `no-phone-text-pictures`     | `Cellphone usage detected` <br> `Person detected taking pictures` | [More details](no-phone-usage.md){:target="_blank"} |
| ✅ | `no-smoking-or-vaping`       | `Smoking event detected` <br> `Vaping event detected` | [More details](no-smoking.md){:target="_blank"} |
| ✅ | `no-children-pets-visitors`  | `Children detected` <br> `Pets detected` <br> `Visitors detected` | [More details](authorized-personnel.md){:target="_blank"} |
| 📅 | `waste-management`           | `Spill event detected` <br> `Waste bin full` <br> `Debris detected in Field of View` |
| 📅 | `energy-conservation`        | `Occupancy pattern daily summary` <br> `Light usage daily summary` |
| 📅 | `restricted-areas`           | `Person detected in restricted area` <br> `Movement detected in restricted area` <br> `Person detected after hours` <br> `Movement detected after hours` |



---

## Equipment Monitoring

Equipment policies include specific scenarios that are relevant monitoring heavy machinaries. These could be through monitoring the temperature of the equipment, or through IoT sensors that are attached to the equipment that allow to monitor vibration, noise, or other parameters for the equipment.

| Status | Scenario name | Supported Events | Additional considerations |
| :----: | :------------ | :--------------- | :------------------------ |
| 📅 | `equipment-temperature`        | `Equipment temperature exceeds limit` <br> `Equipment temperature subsceeds limit` |
| ✅ | `rust-and-corrosion-detection` | `Rust or corrosion event detected` | [More details](rust-and-corrosion.md){:target="_blank"} |
| 📅 | `equipment-vibration`          | `Equipment vibration exceeds limit` | [^2] |
| 📅 | `equipment-noise`              | `Equipment noise exceeds limit` |  [^3]|
| 📅 | `reading-analog-dials`         | `Analog meter reading event`    |
| 📅 | `tools-check-in-check-out`     | `Person left without checkout`  |
| 📅 | `equipment-water-leak-puddle`  | `Water leak detected from equipment` |

[^2]: Vibration sensor needed to implement this scenario.
[^3]: Noise sensor needed to implement this scenario.

---

## Environment Monitoring
Monitoring the environment like current temperature, humidity, or air quality is important to ensure that the workplace is safe and comfortable for employees. These scenarios are implemented through IoT sensors that are completely integrated into Vision AI suite.


| Status | Scenario name | Supported Events | Additional considerations |
| :----: | :------------ | :--------------- | :------------------------ |
| 📅 | `temperature-monitoring` | `Temperature excceds limit` <br> `Temperature subsceeds limit` | [More details](temperature-moniotring.md){:target="_blank"} |
| 📅 | `humidity-monitoring` | `Humidity excceds limit` <br> `Humidity subsceeds limit` | [More details](environment-humidity.md){:target="_blank"} |
| 📅 | `air-quality` | `CO exceeds limit` <br> `CO2 exceeds limit` <br> `NO2 Exceeds limit` <br> `SO2 exceeds limit` <br> `VOCs exceeds limit` <br> `Excessive dust detected` <br> `Excessive dust detected` | [More details](air-quality.md){:target="_blank"} |
| 📅 | `noise-level-monitoring` | `Noise level exceeds limit` | [More details](environment-noise.md){:target="_blank"} |
| 📅 | `pressure-monitoring` | `Pressure excceds limit` <br> `Pressure subsceeds limit` | [More details](environment-pressure.md){:target="_blank"} |
| 📅 | `water leak-monitoring` | `water leakage exceeds limit` | [More details](environment-water-leak.md){:target="_blank"} |
| 📅 | `environment-voc-monitoring` | `VOC execeds limit` | [More details](environment-voc.md){:target="_blank"} |
| 📅 | `environment-co-monitoring` | `CO exceds limit` | [More details](environment-co.md){:target="_blank"} |
| 📅 | `light-sensor-monitoring` | `Light intensity exceeds limit` <br> `Light intensity subsceeds limit` | [More details](light-sensor-monitoring.md){:target="_blank"} |
| 📅 | `dust-monitoring` | `dust exceeds limit` | [More details](environment-dust.md){:target="_blank"} |
| 📅 | `water quality -monitoring` | `Water quality level exceeds limit` | [More details](environment-water-quality.md){:target="_blank"} |
| 📅 | `energy-usage-monitoring` | `Energy usage hourly smmary` | [More details](energy-usage-monitoring.md){:target="_blank"} |
| 📅 | `waste-management` | `TODO` | [More details](environment-waste-management.md){:target="_blank"} |
| 📅 | `water-usage-monitoring` | `Water usage monitoring` | [More details](environment-water-usage.md){:target="_blank"} |
| 📅 | `water-level-monitoring` | `Water level monitoring` | [More details](environment-water-level.md){:target="_blank"} |
| 📅 | `radiation-monitoring` | `Radiation level exceeds limit` <br> `Radiation level subsceeds limit` | [More details](radiation-monitoring.md){:target="_blank"} |

---

## Suspicious Activity detection

Suspicious activity detection suite relies on a combination of activity detection models and object detection models. These models are trained to detect suspicious activity in a variety of scenarios.


| Status | Scenario name | Supported Events | Additional considerations |
| :----: | :------------ | :--------------- | :------------------------ |
| 📅 | `loitering-detection` | `Person detected in closed space` <br> `Person detected during off hours` <br> `Person dwell time exceeds limit` | [More details](loitering.md){:target="_blank"} |
| 📅 | `suspicious-package-detection` | `Suspicious package detected` <br> `Package abandoned` | [More details](suspicious-package-detection.md){:target="_blank"} |
| 📅 | `bullying-fighting-aggressive-behavior` | `Bullying/fighting/aggressive event detected` | [More details](aggressive-behavior.md){:target="_blank"} |
| 📅 | `vandalism-graffiti-company-property-destruction` | `Motion detected in area (gross event)` <br> `People detected in area (more granular event)` <br> `Non-uniformed personnel detected in area` <br> `Non badged personnel detected in area` <br> `Vandalism detected in area (before & after)` <br> `Paint/graffiti detected in area (before & after changes)` <br> `Behavior analysis event showing company property destruction.` | [More details](vandalism.md){:target="_blank"} |
| ✅ | `firearms-knives-detection` | `Person brandishing firearm` <br> `Person brandishing knives` | [More details](firearms-and-knives.md){:target="_blank"} |
| 📅 | `sexual-harassment-detection` | `Potential  event detected` | [More details](sexual-harassment.md){:target="_blank"} |
| 📅 | `solictation-detection` | `Potential solicitation event detected` | [More details](solictation.md){:target="_blank"} |
| 📅 | `theft-and-or-shoplifting` | `Potential theft detected` <br> `Potential shoplifting activity detected` | [More details](theft.md){:target="_blank"} |
| 📅 | `shipping-activity-detection` | `Shipping activity detected during after-hours` <br> `Shipping activity detected from non-designated areas` | [More details](shipping-activity.md){:target="_blank"} |
| 📅 | `intrusion-detection` | `Intrusion event detected` | [More details](intrusion-detection.md){:target="_blank"} |

---

## Vehicle Activity

The below scenarios are designed to detect vehicle activity in and around the factory.

| Status | Scenario name | Supported Events | Additional considerations |
| :----: | :------------ | :--------------- | :------------------------ |
| 📅 | `vehicle-policies` | `Vehicle activity detected in non-designtated areas` <br> `Vehicle activity detected during after-hours` <br> `Collision event detected` <br> `Near collision event detected` | [More details](vehicle-policies.md){:target="_blank"} |
| 📅 | `vehicle-usage`  | `Daily summary event of vehicle usage` <br> `Path-map of vehicle usage` | [More details](vehicle-usage.md){:target="_blank"} |
| 📅 | `forklift-zone-breach` | `Forklift observed outside of configured zone` <br> `Pedestrian observed in forklift zone` | [More details](forklift-zone-breach.md){:target="_blank"} |
| 📅 | `vehicle-license-plate-detection` | `Vehicle detected with license plate number` | [More details](vehicle-license-plate.md){:target="_blank"} |
| 📅 | `vehicle-speed-monitoring` | `Vehicle speed exceeds limit` | [More details](vehicle-speed.md){:target="_blank"} |
| 📅 | `vehicle-cargo-volume-limit` | `Vehicle cargo volume exceeds limit` | [More details](vehicle-cargo.md){:target="_blank"} |

---

## Next Steps

Now that you have a better understanding of the scenarios that are available, you can start to think about how you can organize these scenarios into a solution that meets your needs. You can also go to the individual scenario page to learn more about it. We can customize each of these models for your use-cases and provide you with a solution that is tailored to your needs. You can contact us through [this page](contact.md)