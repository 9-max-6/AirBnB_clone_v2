#!/usr/bin/python3
"""
Fabric script to create archive
"""

from datetime import datetime
from fabric import *


def do_pack():
    """
    making an archive best on the web_static folder
    """
    with Connection(host='127.0.0.1') as c:
        static_archive = 'web_static_' + datetime.now().strftime(
            "%Y%m%d%H%M%S") + '.' + 'tgz'
        c.local('mkdir -p versions')
        create = c.local(f'tar -cvzf versions/{static_archive} web_static')
        if create is not None:
            return static_archive
        else:
            return None
do_pack()