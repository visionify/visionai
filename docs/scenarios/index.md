# Scenarios

Scenarios form the building blocks of VisionAI platform. They consolidate the business logic into a deployable Vision AI model. You can pick and choose different scenarios based on your use-case.

## Supported Scenarios
Below list provides our roadmap support for the scenarios we support for workplace safety industry. We are continuing to add new scenarios to our platform. If you have a specific scenario in mind - please let us know [here](custom/new-scenario-request.md).


- [x] Hazard Warnings
    * [x] Smoke and Fire Detection [[link]( scenarios/smoke-and-fire-detection.md)]
    * [x] In scelerisque nibh non dolor mollis congue sed et metus
    * [ ] Praesent sed risus massa
- [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque

- :
  - Smoke and Fire Detection: scenarios/smoke-and-fire-detection.md
  - No smoking/no vaping: scenarios/no-smoking.md
  - Spills & leaks detection: scenarios/spills-and-leaks.md
  - Gask leak detection: scenarios/gas-leak-detection.md
  - Missing fire extinguisher: scenarios/missing-fire-extinguisher.md
  - Blocked exit monitoring: scenarios/blocked-exit.md
  - Equipment temperature monitoring: scenarios/equipment-temperature.md
  - Equipment rust and corrosion: scenarios/rust-and-corrosion.md

- Worker health & safety:
  - Overview: scenarios/worker-health-and-safety.md
  - PPE Detection: scenarios/ppe-detection.md
  - Working at heights: scenarios/working-at-heights.md
  - Environment monitoring: scenarios/environment-monitoring.md
  - Slip, trip and fall detection: scenarios/fall-and-accident-detection.md
  - Posture & Ergonomics: scenarios/ergonomics.md
  - Empty pallets: scenarios/empty-pallets.md
  - Spills & Leaks detection (Liquids): scenarios/spills-and-leaks.md
  - Hand sanitizer/hand-wash: scenarios/hand-wash.md
  - Worker fatigue detection: scenarios/worker-fatigue-detection.md
  - Worker skin tempreature monitoring: scenarios/skin-temperature.md
  - Confined spaces monitoring: scenarios/confined-spaces-monitoring.md

- Occupancy Policies:
  - Overview: scenarios/occupancy-policies.md
  - Max occupancy: scenarios/max-occupancy-count.md
  - Restricted areas/times: scenarios/exclusion-zones.md
  - Dwell time: scenarios/dwell-time.md
  - Social distancing: scenarios/social-distance.md
  - Station occupancy: scenarios/station-occupancy.md
  - Occupancy metrics: scenarios/occupancy-metrics.md
  - Authorized personnel: scenarios/authorized-personnel.md
  - Tailgating: scenarios/unauthorized-entry.md
  - Perimeter control: scenarios/perimeter-control.md

- Company Policies:
  - Overview: scenarios/compliance-policies.md
  - No food or drinks: scenarios/no-food-or-drinks.md
  - No phone, text, pictures: scenarios/cell-phone-usage.md
  - No Smoking zones: scenarios/no-smoking.md
  - No children/visitors: scenarios/authorized-personnel.md
  - Waste Management: scenarios/waste-management.md
  - Energy Conservation: scenarios/energy-conservation.md
  - Restricted Areas: scenarios/restricted-areas.md

- Equipment monitoring:
  - Overview: scenarios/equipment-monitoring.md
  - Equipment temperature monitoring: scenarios/equipment-temperature.md
  - Equipment rust and corrosion: scenarios/rust-and-corrosion.md
  - Equipment vibration monitoring: scenarios/equipment-vibration.md
  - Equipment noise monitoring: scenarios/equipment-noise.md
  - Read analog dials: scenarios/analog-dials.md
  - Tools check-in/out: scenarios/tools-check-in-out.md
  - Spill & leak: scenarios/equipment-spills-and-leaks.md


- Environment monitoring:
  - Temperature monitoring: scenarios/environment-temperature.md
  - Humidity monitoring: scenarios/environment-humidity.md
  - Air quality monitoring: scenarios/environment-air-quality.md
  - Noise monitoring: scenarios/environment-noise.md
  - Pressure monitoring: scenarios/environment-pressure.md
  - Water leak detection: scenarios/environment-water-leak.md
  - Volatile organic compounds (VOCs): scenarios/environment-voc.md
  - Carbon monoxide (CO): scenarios/environment-co.md
  - Ambient light: scenarios/environment-light.md
  - Dust monitoring: scenarios/environment-dust.md
  - Water quality monitoring: scenarios/environment-water-quality.md
  - Energy usage monitoring: scenarios/environment-energy-usage.md
  - Waste management: scenarios/environment-waste-management.md
  - Water usage monitoring: scenarios/environment-water-usage.md
  - Water level monitoring: scenarios/environment-water-level.md
  - Radiation monitoring: scenarios/environment-radiation.md


- Suspicious Activity:
  - Overview: scenarios/suspicious-activity.md
  - Loitering: scenarios/loitering.md
  - Unattended packages: scenarios/unattended-package.md
  - Aggressive behavior: scenarios/aggressive-behavior.md
  - Vandalism & property destruction: scenarios/vandalism.md
  - Firearms & knives: scenarios/firearms-and-knives.md
  - Sexual harassments: scenarios/sexual-harassment.md
  - Solicitation: scenarios/solicitation.md
  - Theft: scenarios/theft.md
  - Shipping activity: scenarios/shipping-activity.md
  - Intrusion detection: scenarios/intrusion-detection.md

- Vehicle Activity:
  - Overview: scenarios/vehicle-activity.md
  - Vehicle usage: scenarios/vehicle-usage.md
  - Vehicle policies: scenarios/vehicle-policies.md
  - Forklift zone breach: scenarios/forklift-zone-breach.md
  - Vehicle license plate: scenarios/vehicle-license-plate.md
  - Vehicle speed: scenarios/vehicle-speed.md
  - Vehicle cargo: scenarios/vehicle-cargo.md

- Employee Privacy:
  - Overview: scenarios/employee-privacy.md
  - Blur faces: preprocess/blur-faces.md
  - Blur signs/text: preprocess/blur-signs.md
  - Blur screens: preprocess/blur-screens.md
  - Blur license plates: preprocess/blur-license-plates.md
  - Obstructed camera view: preprocess/obstructed-camera-view.md


!!! note "VisionAI Suites"
    VisionAI suites are a collection of scenarios that are commonly used together. For example, the Hazard Warning suite includes scenarios such as smoke and fire detection, no-smoking/no-vaping zones, spills-and-leak detection, gas leak detection, missing fire extinguisher, blocked exit monitoring etc.



=== "Material for MkDocs"

    ``` yaml
    name: ci # (1)!
    on:
      push:
        branches:
          - master # (2)!
          - main
    permissions:
      contents: write
    jobs:
      deploy:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v3
          - uses: actions/setup-python@v4
            with:
              python-version: 3.x
          - uses: actions/cache@v2
            with:
              key: ${{ github.ref }}
              path: .cache
          - run: pip install mkdocs-material # (3)!
          - run: mkdocs gh-deploy --force
    ```

    1.  You can change the name to your liking.

    2.  At some point, GitHub renamed `master` to `main`. If your default branch
        is named `master`, you can safely remove `main`, vice versa.

    3.  This is the place to install further [MkDocs plugins] or Markdown
        extensions with `pip` to be used during the build:

        ``` sh
        pip install \
          mkdocs-material \
          mkdocs-awesome-pages-plugin \
          ...
        ```

=== "Insiders"

    ``` yaml
    name: ci
    on:
      push:
        branches:
          - master
          - main
    permissions:
      contents: write
    jobs:
      deploy:
        runs-on: ubuntu-latest
        if: github.event.repository.fork == false
        steps:
          - uses: actions/checkout@v3
          - uses: actions/setup-python@v4
            with:
              python-version: 3.x
          - uses: actions/cache@v2
            with:
              key: ${{ github.ref }}
              path: .cache
          - run: apt-get install pngquant # (1)!
          - run: pip install git+https://${GH_TOKEN}@github.com/squidfunk/mkdocs-material-insiders.git
          - run: mkdocs gh-deploy --force
    env:
      GH_TOKEN: ${{ secrets.GH_TOKEN }} # (2)!
    ```


Common workplace health and safety scenarios include hazardous materials, ergonomic hazards, workplace compliance violations, and suspicious activities. Hazardous materials may include flammable materials, biological agents, and hazardous chemicals. Employees should understand the risks associated with these materials and the need for proper handling and storage. Ergonomic hazards refer to the physical and environmental conditions of a workplace that may cause injuries or illnesses due to repetitive motions, awkward postures, or heavy lifting. Employers need to assess the environment and take steps to reduce or eliminate these hazards. Employers should create a safe and supportive environment and provide resources to help employees understrand the workplace compliances.


# VisionAI Scenarios

VisionAI can help to streamline safety processes, detect hazards, monitor job site conditions, and improve communication between workers. VisionAI can help to identify risks that may have been previously overlooked and alert workers and managers to potential hazards.

Most of the VisionAI Scenarios fall under:

- Personnel Health
- Compliance Policies
- Privacy Suite



This section lists down all the scenarios that are supported by the VisionAI platform. There are more scenarios added daily - please [send a request](https://github.com/visionify/visionai/issues/new) to us about any additional scenarios you need.


## Personnel Health & Safety
Workplace Personnel Health & Safety is important because it ensures that employees are safe and healthy in their work environment. This includes providing a safe and healthy work environment, proper safety training, and regular safety inspections. Additionally, it also includes enforcing safety policies to ensure that all employees are aware of and follow safety procedures, as well as encouraging a culture of safety within the workplace.

For Personnel health we have the following scenarios available:
### PPE Detection
- Ensures that employees are following safety protocols and wearing the proper PPE at all times.
- An alert will be sent when a person/employee detected without proper PPE and then the employeer may be required to take further steps such as putting on protective equipment.
- Find more details about these scenarios [here](ppe-detection.md).

### Working at heights

- Working at heights, such as on a roof or in a tall building, requires specialized safety equipment and training to ensure the safety of the workers. Depending on the job, you may need to wear a safety harness or other protective gear.
- Find more details about these scenarios [here](working-at-heights.md).


### Slip and Fall Detection
- Ensure the safety of employees by inspecting slip and fall instances.
- It can help alert employees to potential hazards and help them take the necessary steps to avoid accidents.
- Find more details about these scenarios [here](slip-and-fall-detection.md).

### Confined spaces
- Confined space monitoring is done to ensure the safety of workers who are entering the space and to ensure that the space is suitable for the task at hand.
- Find more details about these scenarios [here](confined-spaces-monitoring.md).


### Hazard warning
Early detection of fire signs is important in preventing major fire incidents. Our ready-to-integrate solution provides reliable detection and continuous 24/7 monitoring. As a result, you can achieve quick response time, safer workplaces, minimized costs, and successfully avoid inessential business interruptions.
- Smoke and fire detection systems provide early warning of potential hazards, allowing people to take action and evacuate the premises before the fire can spread.
- Find more details about these scenarios [here](smoke-and-fire-detection.md).


### Ergonomics

- Ergonomics is important because it helps to improve productivity, reduce the risk of work-related injuries, and increase comfort and morale.
- Find more details about these scenarios [here](ergonomics.md).

## Compliance Policies
Compliance policies are important at the workplace because they set clear expectations for employee behavior and ensure that all employees understand the rules of the workplace.

They cover a wide range of issues, from data protection to health and safety, and exist to protect both the company and its workers. These policies help to ensure that the company is in compliance with all relevant regulations, as well as providing a safe and productive working environment for employees.

Compliance policies help promote a safe and secure work environment.

Find more details about these scenarios [here](compliance-policies.md).

As part of **compliance policies**, we provide the following scenarios:
### Equipment monitoring

- Our equipment monitoring systems helps to identify areas where corrosion and erosion may have already begun, allowing for early remedial action. This can help to extend the life of the material and prevent costly repairs or replacements later on. Additionally, rust and corrosion can weaken the strength of a material, so early detection can help to avoid catastrophic failure in the event of a structural load.
- Find more details about these scenarios [here](rust-and-corrosion.md).

###  Max occupancy

- Ensures the safety and well-being of all the occupants at workplace by limiting the number of people in a particular space or area. This helps to prevent overcrowding, which can lead to accidents and fire hazards.
- Find more details about these scenarios [here](max-occupancy-count.md).


### Confined spaces monitoring
- Confined space monitoring is done to ensure the safety of workers who are entering the space and to ensure that the space is suitable for the task at hand.
- Find more details about these scenarios [here](confined-spaces-monitoring.md).

### Shipping activity

- Shipping activity is  critical part of the supply chain process and keeps the flow of goods and services moving.
- These activities help to reduce costs and improve efficiency by providing a consistent and reliable way to track and manage shipments.
- Find more details about these scenarios [here](shipping-activity.md).

### Unauthorized entry

- With unauthorized entry detection system employers will be able to ensure the security of their premises, equipment, and personnel.
- Help to  ensure the safety and security of employees, visitors, and the company's assets.
- Find more details about these scenarios [here](unauthorized-entry.md).


### No mobile usage

- Mobile phone usage detection system can help to prevent and address potential problems that can arise from the improper use of mobile devices.
- Find more details about these scenarios [here](no-phone-usage.md).

### No visitors

- No visitors policy reduces the risk of potential theft or other criminal activity in the workplace. It also helps to maintain the privacy of employees and their work related information.
- Find more details about these scenarios [here](no-visitors.md).

### No pictures

- Having a no pictures policy at work can help maintain a respectful, productive, and professional work environment.
- Find more details about these scenarios [here](no-taking-pictures.md).

### No food allowed

- No food policies help to maintain a clean and safe work environment and promote a professional work atmosphere, as food and eating can be seen as a distraction from work.
- Find more details about these scenarios [here](no-food-allowed.md).

### No children

- To ensure a safe and distraction-free environment for employees it is important to follow no children policy and it can also be dangerous as children may be exposed to hazardous materials or machinery.
- Find more details about these scenarios [here](no-children.md).



## Privacy Suite

We came up with these scenarios in order to protect the user's privacy. For example, it can be used to blur out faces in videos or images. AI can identify features in a video or image and then apply a blur effect to those features. This can be used to blur out faces, license plates, and other identifying features that a user may not want to be seen by others.

As part of **VisionAI preprocessing** we provide the following options:

### Blur faces
- Ensure the privacy of individuals in public spaces by blurring the faces.
- Find more details about these scenarios [here](blur-faces.md).

### Blur signs
- Our algorithms can help to blur the signs (eg. licence plates) by using image recognition algorithms to identify the area of the image that contains the sign and then applying a blurring effect to that area.
- Find more details about these scenarios [here](blur-licence-plates.md).


### Blur documents
- Ensure the privacy of individuals and organizations by blurring out sensitive information
- Find more details about these scenarios [here](blur-documents.md).

### Blur screens
- Identify screens in a video or image and then apply a blur effect to prevent sensitive information from being seen.
- Find more details about these scenarios [here](blur-screens.md).




