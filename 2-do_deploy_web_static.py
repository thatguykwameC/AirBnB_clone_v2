#!/usr/bin/python3
"""
    Fab-script to generate a .tgz archive
    from the contents of the web_static folder
"""
from fabric.api import env, put, run
from datetime import datetime
from os.path import exists

env.hosts = ['18.206.198.224', '100.25.135.96']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    
    try:
        farchive = basename(archive_path)
        RName = farchive.split('.')[0]
        RPath = "/data/web_static/releases/"

        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(RPath, RName))
        run('tar -xzf /tmp/{} -C {}{}/'.format(farchive, RPath, RName))
        run('rm /tmp/{}'.format(farchive))
        run('mv {}{}/web_static/* {}{}/'.format(RPath, RName))
        run('rm -rf {}{}/web_static'.format(RPath, RName))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(RPath, RName))
        return True
    except Exception:
        return False
