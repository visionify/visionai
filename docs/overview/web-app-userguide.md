#  Visionai Web Application Instructions

The VisionAI  web application is the main interface through which users can interact with the system. 

It supports the following functionality:
1. Onboard any IP cameras onto the VisionAI System.
2. Pick and choose AI scenarios you want to run on these IP cameras.
3. Configure events, notifications (email/text) and video recording settings.
4. Configure video clips recording for different events.

The web-application is available at http://localhost. 





## Basic Usage

1. Please open localhost in the browser.
2. Use your default username/password as master/master.
3. After this, you will be asked to create a new admin user. Please use a strong password and create an admin user.

![Sign-In page](https://visionai.azureedge.net/docs-images/Web-app_Pictures/sign_in.jpg)






## Cameras

Once you are signed in, you will see a blank dashboard page. 
Let’s add an IP camera to the system. In order to do this,
1. Go to the “Cameras” tab on the left menu bar.
2. Then Click on the  + button.
3. If you want to add multiple cameras at a time, then you can click on button, next to the add camera button.

![Add-Camera](https://visionai.azureedge.net/docs-images/Web-app_Pictures/Camera_page_Instructions.jpg
)

A new pop-up window will appear to add cameras. You can enter the camera name, description, and RTSP URI for the camera. The RTSP URI can be obtained from the Camera or NVR documentation. You can ignore the other fields as they are optional. Click on “Add” button.

![Notification-Settings-for-Camera](https://visionai.azureedge.net/docs-images/Web-app_Pictures/Add_Camera_instructions.jpg
)


If you want to add multiple cameras at a time, then you can click on button, next to the add camera button.

![Add-Multiple-Camera](https://visionai.azureedge.net/docs-images/Web-app_Pictures/AddMultipleCamera_instructions.jpg)

Once you have added the camera, it should appear on the Cameras window and should show the initial streaming for the camera. Add any additional cameras in a similar fashion. Once all cameras have been added, the front-screen should look like this:

![](https://visionai.azureedge.net/docs-images/Web-app_Pictures/Added_cameraview.jpg)






## Scenarios

Once you are signed in, you will see a blank dashboard page. 
You may select any scenario from the list of active scenarios.

![](https://visionai.azureedge.net/docs-images/Web-app_Pictures/Scenario_available_page.jpg
)

This shows details about the Scenario, the model version used, events supported and model accuracy, recall and F1 score metrics. You can now click on the “Get this” button again to apply the scenario to cameras.

![](https://visionai.azureedge.net/docs-images/Web-app_Pictures/Add_scenario.jpg)


In the next page, Select the Cameras for which you want to apply this scenario.
Click “Save and Next”

![](https://visionai.azureedge.net/docs-images/Web-app_Pictures/AddScenario_SelectCamera.jpg)

 In the next page, you can specify notification details. 
Click on the Submit button once the details have been entered.

![](https://visionai.azureedge.net/docs-images/Web-app_Pictures/AddScenario_NotificationForm.jpg)


Additionally, we have a list of scenarios that our team is currently working on. It can be viewed under the Upcoming Scenarios section

![](https://visionai.azureedge.net/docs-images/Web-app_Pictures/Upcoming_scenarios.jpg)






## Events

This page will show the list of events that have occurred in the selected time frame.

![](https://visionai.azureedge.net/docs-images/Web-app_Pictures/EventsOccured_page.jpg)






## Graphs

This page summarizes the events that occurred in the form of graphical representation.

![](https://visionai.azureedge.net/docs-images/Web-app_Pictures/Graph-1.jpg)

![](https://visionai.azureedge.net/docs-images/Web-app_Pictures/Graph-2.jpg)






## Settings

1. User

   Click on the User tab and fill in the details as required. Later that user can be selected while setting up the notification details. 

![](https://visionai.azureedge.net/docs-images/Web-app_Pictures/Create_User_form.jpg)




2. Notification Group

   Click on the Notification Group tab and you can make the required changes to the created groups. 

![](https://visionai.azureedge.net/docs-images/Web-app_Pictures/NotificationGroup_mainPage.jpg)


Click on the Create Group  button and you will be able to create a group of users. 

Enter the name of group as per the requirement.

Click on Edit button, available besides each of the available users. Select a group name, to which the user needs to be added.

![](https://visionai.azureedge.net/docs-images/Web-app_Pictures/CreateGroup_notification.jpg)



Click on Edit Group button, which will let you make changes to the created group of users.

Click on Delete button, besides the Group name. The group will then be deleted permanently.

![](https://visionai.azureedge.net/docs-images/Web-app_Pictures/DeleteGrp_Notification.jpg)