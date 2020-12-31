"""The export projects command"""
import logging
from pathlib import Path
from typing import Optional, List
import re

from pycaprio import Pycaprio
from pycaprio.mappings import InceptionFormat

import click

_log = logging.getLogger("inception")


def make_client(url: str, user: Optional[str]) -> Pycaprio:
    if user:
        password = click.prompt("Password", hide_input=True)
        client = Pycaprio(url, authentication=(user, password))
    else:
        client = Pycaprio(url)
    return client


@click.command(name="export")
@click.option("-u", "--url", help="INCEpTION instance URL")
@click.option("-U", "--user", help="User name")
@click.argument("target", default=".", type=click.Path())
def export_projects(url: str, user: Optional[str], target: Optional[str]):
    """ Exports all projects and saves them to disk.

    Args:
        url: The URL pointing to the INCEpTION instance whose projects are exported
        target: Directory in which to save the projects (default: current working directory)
        user: Remote API access user
    """

    _log.info("Exporting all projects")

    client = make_client(url, user=user)

    # List projects
    projects = client.api.projects()

    target_folder = Path(target)
    target_folder.mkdir(parents=True, exist_ok=True)

    # Export all projects
    for project in projects:
        target_path = target_folder / (project.project_name + ".zip")

        _log.info("Exporting project [%s] to [%s]", project, target_path)
        zip_content = client.api.export_project(project, project_format=InceptionFormat.BIN)

        with target_path.open("wb") as zip_file:
            zip_file.write(zip_content)

        _log.info("Finished exporting projects")


@click.command(name="import")
@click.option("-u", "--url", help="INCEpTION instance URL")
@click.option("-U", "--user", help="User name")
@click.argument("projects", type=click.File('rb'), nargs=-1)
def import_project(url: str, user: Optional[str], projects: List[str]):
    """ Imports the given projects.

    Args:
        url: The URL pointing to the INCEpTION instance into which the projects are imported
        projects: one or more INCEpTION project ZIP files
        user: Remote API access user
    """

    client = make_client(url, user=user)

    for project in projects:
        _log.info("Importing project [%s] ...", project.name)
        imported_project = client.api.import_project(project)
        _log.info("Imported project as [%s]", imported_project.project_name)


@click.command(name="list")
@click.option("-u", "--url", help="INCEpTION instance URL")
@click.option("-U", "--user", help="User name")
def list_projects(url: str, user: Optional[str]):
    """ Lists the projects.

    Args:
        url: The URL pointing to the INCEpTION instance into which the projects are imported
        user: Remote API access user
    """

    client = make_client(url, user=user)

    projects = client.api.projects()
    for project in projects:
        _log.info("[%s]", project.project_name)


@click.command(name="delete")
@click.option("-u", "--url", help="INCEpTION instance URL")
@click.option("-U", "--user", help="User name")
@click.option("--regex", is_flag=True, default=False, help="Whether to interpret the project name as a regular expression")
@click.option("--dry-run", is_flag=True, default=False, help="Log which projects would be deleted without deleting them")
@click.argument("projects", nargs=-1)
def delete_project(url: str, user: Optional[str], regex: bool, dry_run: bool, projects: List[str]):
    """ Lists the projects.

    Args:
        url: The URL pointing to the INCEpTION instance into which the projects are imported
        user: Remote API access user
        projects: the projects to delete
        regex: whether to interpret the project names as regular expressions
        dry_run: Log which projects would be deleted without deleting them
    """

    client = make_client(url, user=user)

    if regex:
        patterns = projects
        projects = []
        accessible_projects = client.api.projects()
        for pattern in patterns:
            for accessible_project in accessible_projects:
                if re.fullmatch(pattern, accessible_project.project_name) is not None:
                    projects.append(accessible_project)

    for project in projects:
        _log.info("Deleting [%s]", project.project_name)
        if not dry_run:
            client.api.delete_project(project)
