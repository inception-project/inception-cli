"""The export projects command"""
from pathlib import Path

from pycaprio import Pycaprio
from pycaprio.mappings import InceptionFormat

import click


@click.command()
@click.option('-u', '--url', help='INCEpTION URL')
@click.argument('target', default='.', type=click.Path())
def export_projects(url, target):
    client = Pycaprio(url)

    # List projects
    projects = client.api.projects()

    target = Path(target)
    target.mkdir(parents=True, exist_ok=True)

    # Export all projects
    for project in projects:
        print(f"Exporting project {project}... ", end='')
        zip_content = client.api.export_project(project, project_format=InceptionFormat.BIN)
        with open(target.joinpath(project.project_name+".zip"), 'wb') as zip_file:
            zip_file.write(zip_content)
        print(f"done.")
