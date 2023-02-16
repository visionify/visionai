import typer
from rich import print

pipeline_app = typer.Typer()

# Pipeline app
@pipeline_app.command('create')
def pipeline_create(
    name : str = typer.Option(..., help='pipeline name')
):
    '''
    Create a named pipeline

    Create a named pipeline. Pipeline is a list of scenarios
    to be run for specific cameras. The flow is as follows. Create
    a pipeline using:

    visionai pipeline create --name test_pipe

    visionai pipeline add-scenario --pipeline test_pipe  --name smoke-and-fire

    visionai pipeline add-scenario --pipeline test_pipe  --name ppe-detection

    visionai pipeline add-preprocess --pipeline test_pipe  --name face-blur

    visionai pipeline add-preprocess --pipeline test_pipe  --name text-blur

    visionai pipeline add-scenario --pipeline test_pipe  --name max-occupancy

    visionai pipeline show --pipeline test_pipe

    visionai pipeline add-camera --pipeline test_pipe  --name CAMERA-01

    visionai pipeline add-camera --pipeline test_pipe  --name CAMERA-02

    visionai pipeline show --pipeline test_pipe

    visionai pipeline run --pipeline test_pipe

    @arg pipeline - specify a named pipeline

    @return None
    '''
    print(f'Creating pipeline f{name}')


@pipeline_app.command('add-scenario')
def pipeline_add_scenario(
    pipeline : str = typer.Option(..., help='pipeline name'),
    scenario: str = typer.Option(..., help='scenario to add')
):
    '''
    Add a scenario to a pipeline

    The order of the scenarios does not matter. All added scenarios
    are run in different threads. All scenarios are run after
    pre-processing stage is done.

    $visionai pipeline --name test_pipe add-scenario --name smoke-and-fire

    $visionai pipeline --name test_pipe add-scenario --name ppe-detection

    $visionai pipeline --name test_pipe run

    @arg pipeline - specify a named pipeline
    @arg scenario - specify name of the scenario to run

    @return None
    '''
    print(f'Adding scenario {scenario} to pipeline f{pipeline}')


@pipeline_app.command('add-preprocess')
def pipeline_add_preprocess(
    pipeline : str = typer.Option(..., help='pipeline name'),
    preprocess: str = typer.Option(..., help='preprocess routine to add')
):
    '''
    Add a preprocess routine to a pipeline

    Preprocessing tasks are run prior to scenarios. The order in which
    multiple preprocess tasks are added does not matter. All added preprocess
    routines are executed in different threads.

    $ visionai pipeline --name test_pipe add-preprocess --name face-blur

    $ visionai pipeline --name test_pipe add-preprocess --name text-blur

    $ visionai pipeline --name test_pipe show

    $ visionai pipeline --name test_pipe run

    @arg pipeline - specify a named pipeline
    @arg preprocess - specify name of the preprocess task to run

    @return None
    '''
    print(f'Adding preprocess {preprocess} to pipeline f{pipeline}')


@pipeline_app.command('add-camera')
def pipeline_add_camera(
    pipeline : str = typer.Option(..., help='pipeline name'),
    camera: str = typer.Option(..., help='camera to add')
):
    '''
    Add a camera to a pipeline

    Each pipeline consists of a bunch of scenarios to run
    and which cameras they need to be run on. This method
    allows the user to add one or more named camera instance
    to a pipeline. Please note the camera instance has to be
    created prior to adding it here.

    # add a camera
    $ visionai camera add --name OFFICE-01 --uri https://youtube.com

    # add camera to pipeline
    $ visionai pipeline --name test_pipe add-camera --name OFFICE-01

    @arg pipeline - specify a named pipeline
    @arg camera - specify name of the camera to add

    @return None
    '''
    print(f'Adding camera {camera} to pipeline f{pipeline}')

@pipeline_app.command('remove-camera')
def pipeline_remove_camera(
    pipeline : str = typer.Option(..., help='pipeline name'),
    camera: str = typer.Option(..., help='camera to remove')
):
    '''
    Remove a camera from a pipeline

    This method can be used to remove a camera from a pipeline.

    $ visionai pipeline --name test_pipe remove-camera --name OFFICE-01

    @arg pipeline - specify a named pipeline
    @arg camera - specify name of the camera to remove

    @return None
    '''
    print(f'Removing camera {camera} to pipeline f{pipeline}')


@pipeline_app.command('reset')
def pipeline_reset(
    pipeline : str = typer.Option(..., help='pipeline name')
):
    '''
    Reset the pipeline to original state.

    Deletes all cameras, scenarios and scenario configuration
    from the pipeline. Its as if the pipeline has been deleted
    and created from scratch again.

    $ visionai pipeline --name test_pipe reset

    @arg pipeline - pipeline to reset

    @return None
    '''
    print(f'Pipeline {pipeline} reset')



@pipeline_app.command('show')
def pipeline_show(
    pipeline : str = typer.Option(..., help='pipeline name')
):
    '''
    Show details of a pipeline

    Show what is configured in the current pipeline.

    $ visionai pipeline --name test_pipe show

    @arg pipeline - specify a named pipeline

    @return None
    '''
    print(f'Show pipeline {pipeline} details')


@pipeline_app.command('run')
def run(
    pipeline: str = typer.Option(..., help='Pipeline to run')
):
    '''
    Run a pipeline of scenarios on given cameras

    Specify different scenarios to run on one or more
    cameras. This method can be directly used to specify scenarios
    and cameras directly. Else you can configure a named pipeline
    and then run it here.

    @arg pipeline - specify a named pipeline

    @return None
    '''
    print(f'Running pipeline f{pipeline}')

@pipeline_app.callback()
def callback():
    '''
    Manage pipelines

    Pipeline is a sequence of preprocess routines and scenarios
    to be run on a given set of cameras. Each pipeline can be
    configured to run specific scenarios - each scenario with their
    own customizations for event notifications. This module provides
    robust methods for managing pipelines, showing their details,
    adding/remove cameras from pipelines and running a pipeline.
   '''


if __name__ == '__main__':
    pipeline_app()
