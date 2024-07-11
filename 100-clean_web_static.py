#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives, using the function do_clean
Usage:
fab -f 100-clean_web_static.py \
do_clean:number=2 -i my_ssh_private_key \
-u ubuntu > /dev/null 2>&1
"""
import os
from fabric.api import env, lcd, local, cd, run

env.hosts = ['52.207.208.230', '18.204.11.104']


def do_clean(number=0):
    """A function that deletes out-of-date archives"""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
