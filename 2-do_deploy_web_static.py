#!/usr/bin/python3
"""
Fabric script to upload archive using the function do_deploy
"""

from fabric.api import task, env, put, cd, run

env.hosts = [
    '54.210.57.216',
    '54.167.150.28'
    ]

@task
def do_deploy(archive_path):
    """return False if the file at the parth archive_path doesn't exist."""
    archive_name = archive_path.split('/')[-1]

    put(archive_path, f'/tmp/{archive_name}')

    with cd('/data/web_static/releases'):
        run(f'mkdir -p {archive_name.split(".")[0]}')
        run(f'tar -xzvf /tmp/{archive_name} -C {archive_name.split(".")[0]}')
    with cd('/tmp'):
        run(f'rm /tmp/{archive_name}')
    with cd('/data/web_static'):
        run('rm -rf current')
        run(f'ln -s /data/web_static/releases/{archive_name.split(".")[0]} current')
