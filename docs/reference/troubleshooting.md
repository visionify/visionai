# Troubleshooting

## Windows Installation through WSL2
Installation on a Windows system is usually challenging because of the various Docker and NVIDIA dependencies. If you come across any issues - please do not hesitate to reach out to us.

### Install WSL 2 (Windows Subsystem for Linux 2)
Install WSL2 using the following steps.

1. Open Command Prompt, and run the following command:

```cmd
wsl.exe --install
```

2. This should install WSL Ubuntu image on your desktop. Once installed - it will ask you to reboot the system. 

3. Once reboot is complete, WSL will prompt you for username & password for your Linux system. Enter this information.


### Install Docker

1. Download docker desktop from [here](https://docs.docker.com/desktop/install/windows-install/).

2. Follow the on-screen instructions and install Docker Desktop. 

3. Reboot the system again.

### Set WSL to Ubuntu

1. Set the default Linux distribution to Ubuntu on WSL.

```cmd
wsl.exe --set-version Ubuntu
```

2. Start the Linux Subsystem

```
wsl.exe
```

### Complete installation

1. This concludes installing Docker and WSL Subsystems on Windows Environment. From this point onwards, you can follow the Ubuntu instructions. For example, next step is to install VisionAI package using `pip install visionai` command.

