#!/usr/bin/python3
"""
Fabric script generates .tgz archive of all in web_static/ using func 'do_pack'
Usage: fab -f 1-pack_web_static.py do_pack

All files in the folder web_static must be added to the final archive
All archives must be stored in the folder 'versions' (create folder if none)
Create archive "web_static_<year><month><day><hour><minute><second>.tgz"
The function do_pack must return the archive path, else return None
"""
from fabric.api import local
from time import strftime


def do_pack():
    """A function that generates .tgz archive from contents of web_static"""

    name = strftime('%Y%m%d%H%M%S')

    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static".format(name))
        return ("versions/web_static_{}.tgz".format(name))

    except Exception:
        return None
