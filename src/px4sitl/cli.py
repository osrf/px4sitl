import sys

import rocker
from rocker.core import list_plugins
from rocker.core import pull_image
from rocker.core import DockerImageGenerator


def mcmillan():
    print("Launching McMillan Airfield")
    run_drone_demo('roslaunch sitl_launcher demo.launch gui:=false sitl_world:=mcmillan')

def yosemite():
    print("Launching Yosemite Valley")
    run_drone_demo('roslaunch sitl_launcher demo.launch gui:=false sitl_world:=yosemite')


def run_drone_demo(command):
    plugins = list_plugins()
    base_image = 'tfoote/drone_demo'
    desired_plugins = ['nvidia', 'pulse', 'user', 'home', 'x11']
    active_extensions = [e() for e in plugins.values() if e.get_name() in desired_plugins]
    pull_image(base_image)
    dig = DockerImageGenerator(active_extensions, {}, base_image)
    if dig.build() != 0:
        print ("Failed to build")
        sys.exit(1)
    if dig.run(command) != 0:
        print ("Failed to run")
        sys.exit(1)
