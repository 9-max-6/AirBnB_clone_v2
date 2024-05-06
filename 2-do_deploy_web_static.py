#!/usr/bin/python3
"""
Fabric script to upload archive using the function do_deploy
"""

from fabric.api import *

env.hosts = [
    '54.210.57.216',
    '54.167.150.28'
    ]
hosts = ['54.210.57.216', '54.167.150.28']
@task
def do_deploy(c, archive_path):
    """return False if the file at the parth archive_path doesn't exist."""
    with cd('/temp/'):
        archive_name = archive_path.split('/')[-1]
        upload = put(archive_path, archive_name)
        if not upload.failed:
            archive_name = archive_path.split('/')[-1].split('.')[0]
            with cd('/data/web_static/releases/'):
                result = run(f'tar -xzvf /temp/{archive_name}.tgz -C {archive_name}')
                result = run('rm ../current')
                result = run(f'ln -s ../current ./{archive_name}')
            if result.failed:
                return (False)
            else:
                return (True)
