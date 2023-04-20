## **Cameras**

An organization can have multiple cameras that are installed at different places. They may be from different vendors and/or maybe using different security surveillance software. Most cameras however do support RTSP, RTMP or HLS streams as an output. Please refer to your camera vendor documentation to find this out. This module will help you onboard those cameras on visionai systems by using a simple named instance for each camera.


### Add camera 
* Add a named camera instance through the following command:

``` bash
$ visionai camera add --name OFFICE-01 --url rtsp://192.168.0.1:554/1
```

### Add scenario

* Add a scenario for a camera through the following command:

``` bash
$ visionai camera add-scenario --name OFFICE-01 --scenario ppe-detection
```

### List cameras

* List available cameras through the following command:
``` bash
$ visionai camera list
```

### List scenarios

* List scenarios configured for a camera through the following command:

``` bash
$ visionai camera list-scenarios --name OFFICE-01
```

### Preview camera

* Preview the camera system through the following command:

``` bash
$ visionai camera preview --name OFFICE-01
```


### Remove camera

* Remove a camera from the system through the following command:

``` bash
$ visionai camera remove --name OFFICE-01
```

### Remove scenario

* Remove a scenario from a camera through the following command:

``` bash
$ visionai camera remove-scenario --name OFFICE-01 --scenario ppe-detection
```

### Reset camera

* Reset all camera configuration through the following command:

``` bash
$ visionai camera reset
```
