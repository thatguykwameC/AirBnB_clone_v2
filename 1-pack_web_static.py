#!/usr/bin/python3

"""This script creates a compressed archive (.tgz) of the web_static
folder in the AirBnB Clone repository."""

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Packs the web_static folder into a timestamped .tgz archive."""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"versions/web_static_{date}.tgz"
    if os.path.exists('web_static') is False:
        return None

    local(f"tar -cvzf {file_path} web_static")
    return file_path
