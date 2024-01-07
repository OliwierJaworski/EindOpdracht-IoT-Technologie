# Iot Project
## What is the aim

The aim of the IoT project is to clearly demonstrate the different aspects of developing and maintaining an IoT product. 

## Task
This includes automatically building the software for the appropriate platform, implementing automatic update mechanisms on the target platform and packaging the software in a specific format.

It is also very important that the software is able to send data to the provided database and restore itself if automatic updates fail. 

The project also includes displaying data in a dashboard and setting up a secure internet connection for the target platform.

## What knowledged is needed to complete this project with success:
```
  -beginner level knowledge of github actions
  -intermediate knowledge of any programming language for the use of bash and python script
  -knowledge of port forwarding for the option to connect remotely to the IoT device
```
## which hardware is needed:
```
  -any hardware with an operating system compatible with docker
  -The used hardware is a Pynq Z2 that runs on the arm32/v7 architecture with a custom ubuntu version made by xilinx
```

## Useful links:
```
- Get started guide Docker
https://docs.docker.com/get-started/
https://hub.docker.com/

- Docker on the Pynq debugging
https://discuss.pynq.io/t/docker-xilinx-platforms-pynq/1962/8

- Debian packaging in-depth tutorial
https://www.debian.org/doc/manuals/packaging-tutorial/packaging-tutorial.en.pdf

- Pynq Z2 basic setup
https://pynq.readthedocs.io/en/latest/getting_started/pynq_z2_setup.html

https://www.portainer.io/
```
## Teamwork
You can work on this project alone or with a group. It has lots of things that can help you get better at different skills.
## Criteria for success

#### These objectives act as guiding principles for individuals aiming to undertake and complete this project independently.

- [x] The group is capable of showing they worked as a unit, and not as individuals
- [X] The group has good automation hygiene (no manual tasks, plenty of automation, …)
- [X] The group has good Git hygiene (commit messages, branching, consistency, …)
- [X] The group has good GitHub hygiene (pull requests, issues, actions, …)
- [X] The group produced good documentation about the project
- [X] The group was capable of creating a good developer experience (getting started in the README)
- [X] The group is capable of explaining what makes their project an IoT project

- [X] An IoT device is connected to the internet
- [X] More than one IoT device are connected to each other (mesh)
- [X] An IoT device is securely connected to the internet
- [X] An IoT device of which the application software automatically updates itself (OTA)
- [ ] An IoT device can be completely updated over the air (kernel upgrade)*
- [X] An IoT device is capable of being serviced remotely

- [X] The application software is capable of speaking to an HTTPS CRUD endpoint
- [X] The application software is well written (clean code)
- [ ] The application software uses Xilinx SDK code*
- [X] The application software is written in a consistent style
- [ ] There is automation to lint the application software
- [X] The application software is automatically built
- [X] The application software is automatically packaged

- [X] The application software is packaged in either a Docker format, or a DEB format
- [ ] The application software is packaged in Nix
- [ ] The IoT device is capable of being monitored (node_exporter)
- [ ] The application software uses Python and uses Poetry as a dependency manager
- [ ] The IoT device drives external hardware
- [ ] A Linux kernel module drives the external hardware*
- [ ] The HTTPS CRUD endpoint is self-hosted (AWS, Azure, on-premise, …)

- [X] The group showed an extra not listed above*
