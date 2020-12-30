"""The export projects command"""
import logging
from pathlib import Path
from typing import Optional

from pycaprio import Pycaprio
from pycaprio.mappings import InceptionFormat

import click

_log = logging.getLogger("inception")


@click.command()
@click.option("-h", "--host", help="INCEpTION instance")
@click.option("-u", "--user", help="User name")
@click.argument("target", default=".", type=click.Path())
def export_projects(host: Optional[str], user: Optional[str], target: Optional[str]):
    """ Exports all projects and saves them to disk.

    Args:
        host: The URL pointing to the INCEpTION instance whose projects are exported
        target: Directory in which to save the projects (default: current working directory)
    """

    _log.info("Exporting all projects")

    if user:
        password = click.prompt("Password", hide_input=True)
        client = Pycaprio(host, authentication=(user, password))
    else:
        client = Pycaprio(host)

    # List projects
    projects = client.api.projects()

    target_folder = Path(target)
    target_folder.mkdir(parents=True, exist_ok=True)

    # Export all projects
    for project in projects:
        target_path = target_folder / (project.project_name + ".zip")

        _log.info("Exporting project [{0}] to [{1}]", project, target_path)
        zip_content = client.api.export_project(project, project_format=InceptionFormat.BIN)

        with target_path.open("wb") as zip_file:
            zip_file.write(zip_content)

        _log.info("Finished exporting projects")
