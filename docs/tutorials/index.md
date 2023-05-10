# **Tutorials**

## Set up a **Pipeline**

You can specify a single scenario or multiple scenarios along with pre-processing steps under pipeline creation.

In other words, pipeline is a list of scenarios to be run for specific cameras. The flow is as follows.

You can create a pipeline by using the following command:

```console
$ visionai pipeline create --name test_pipe
```

    
Scenarios can be added as follows:

For example let's add Smoke-and-Fire dection and PPE detection to our pipeline.

```console
$ visionai pipeline add-scenario --pipeline test_pipe  --name smoke-and-fire
```

```console
$ visionai pipeline add-scenario --pipeline test_pipe  --name ppe-detection
```


You can get the details of the pipeline:

```console
$ visionai pipeline show --pipeline test_pipe
```
