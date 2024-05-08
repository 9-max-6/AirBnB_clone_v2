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
    new_archive = archive_name.split(".")[0]
    put(archive_path, f'/tmp/{archive_name}')

    with cd('/data/web_static/releases'):
        run(f'mkdir -p {new_archive}')
        run(f'tar -xzvf /tmp/{archive_name} -C {new_archive}')
    with cd('/tmp'):
        run(f'rm /tmp/{archive_name}')
    with cd('/data/web_static'):
        run('rm -rf current')
        command = 'ln -sf /data/web_static/releases/'
        run(f'{command}{new_archive} current')
    with cd(f'/data/web_static/releases/{new_archive}'):
        run(f'cp -r web_static/* .')
        run('rm -r web_static')
