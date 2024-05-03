#!/usr/bin/python3
"""
    Fab-script to generate a .tgz archive
    from the contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ func that generate a .tgz """
    dt = datetime.now()
    arc_name = "web_static_{}.tgz".format(dt.strftime("%Y%m%d%H%M%S"))
    arc_path = "versions/{}".format(arc_name)
    local('mkdir -p versions')
    print("Packing web_static to", arc_path)
    create_local = local("tar -cvzf {} web_static".format(arc_path))

    if (create_local.succeeded):
        return arc_path
    else:
        return None
