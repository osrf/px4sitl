# Imaging the machine and high level Summary

These documents have been tested for installing from scratch with Ubuntu 18.04 with an Nvidia Graphic Card in an Asus Predator Laptop.

## OS Installation
* plug in ethernet cable
* Install 18.04.2 Desktop (all settings by default unless otherwise specified)
 * enable download updates and 3rdparty
* erase ubuntu and install
* update all packages `sudo apt update && sudo apt dist-upgrade`
* install nvidia driver `sudo apt install nvidia-384` 
* restart

## Software installation

High level summary
* install docker https://docs.docker.com/install/linux/docker-ce/ubuntu/
* install nvidia-docker2 https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0)

Detailed command line for phase:

```
sudo apt-get install     apt-transport-https     ca-certificates     curl     software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository    "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt-get install docker-ce
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey |   sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list |   sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update
sudo apt-get install nvidia-docker2
sudo pkill -SIGHUP dockerd
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
sudo adduser osrf docker

# backport some package for xenial
wget https://raw.githubusercontent.com/osrf/rocker/master/backport_xenial.bash
bash backport_xenial.bash


sudo apt-get update
sudo apt-get install python3-px4sitl
```
# CentOS 6 variations

This has also been tested on CentOS 6 using a ToughPad following this procedure.

## Install Docker CE

Install Docker as recommeded by upstream: https://docs.docker.com/install/linux/docker-ce/ubuntu/

Make sure to add your user to the `docker` group.

## Install Rocker

https://github.com/osrf/rocker which is available from [pypi](https://pypi.org/project/rocker/).
I recommed using a virtualenv for isolation.

## Video card variation

The ToughPad does not have an nvidia graphics card, so you need to mount the integrated intel graphics card. Use the `--devices /dev/dri/card0` option when launching.


## Running

An example run will look like this:
`rocker --x11 --user --home --devices /dev/dri/card0 --pulse tfoote/drone_demo`
