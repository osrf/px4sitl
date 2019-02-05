import sys

import rocker
from rocker.core import list_plugins
from rocker.core import pull_image
from rocker.core import DockerImageGenerator


def iris():
    print("running iris")
    run_drone_demo('roslaunch sitl_launcher demo.launch mavros:=true gui:=false')

def plane():
    print("running plane")
    run_drone_demo('roslaunch sitl_launcher plane_demo.launch world_name:=worlds/plane_cam.world gui:=false')


def run_drone_demo(command):
    plugins = list_plugins()
    base_image = 'tfoote/drone_demo'
    desired_plugins = ['nvidia', 'pulse', 'user']
    active_extensions = [e() for e in plugins.values() if e.get_name() in desired_plugins]
    pull_image(base_image)
    dig = DockerImageGenerator(active_extensions, '', base_image)
    if dig.build() != 0:
        print ("Failed to build")
        sys.exit(1)
    if dig.run(command) != 0:
        print ("Failed to run")
        sys.exit(1)
