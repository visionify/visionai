# VisionAI Unit Test framework
Run these test cases prior to checking in the codebase.

## Package tests

Run these test cases prior to checkin.

```bash
make package.build      # builds a local docker container with Poetry & dependencies
make package.test       # Runs unit tests on the package

```

## Unit tests

- Run unit tests without coverage

```bash
python -m pytest visionai/tests
```

- Run unit tests with Coverage report

```bash
coverage run -m pytest visionai/tests
```


## Coverage report

- Generate text and/or HTML report for coverage analysis:

```bash
coverage report  # text report
coverage html    # HTML report
```

- It will show a report like below. Goal is to make all file's coverage to 100% across all files. Right now since many of the unit tests invoke the CLI, the coverage is low.

```bash
$ coverage report
Name                                  Stmts   Miss  Cover
---------------------------------------------------------
visionai/__init__.py                      0      0   100%
visionai/config.py                       44     13    70%
visionai/tests/__init__.py                0      0   100%
visionai/tests/test_cli_camera.py       130      1    99%
visionai/tests/test_cli_main.py          32      2    94%
visionai/tests/test_cli_models.py        30      4    87%
visionai/tests/test_cli_scenario.py      48      2    96%
visionai/tests/test_cli_web.py           38      2    95%
visionai/tests/test_deps.py              20      2    90%
visionai/tests/test_docker_cli.py        20      3    85%
visionai/util/__init__.py                38     16    58%
visionai/util/general.py                291    212    27%
---------------------------------------------------------
TOTAL                                   691    257    63%

```

## Lint and Safety checks

- Run lint checks

```bash
make lint
```

- Run safety checks

```bash
make safety
```

- Both have a lot of errors - need to fix them


## CI/CD Unit Test Integration

- Azure CI/CD integration is already set-up for running Unit Tests.
- Once a code is checked-in, coverage report will be available in pipeline run.
