"""The export projects command"""
import logging
from pathlib import Path
from typing import Optional, List

from pycaprio.mappings import InceptionFormat

import click

from inception.utils import make_client, list_matching_projects, get_project_from_name

_log = logging.getLogger("inception")


@click.command(name="export")
@click.option("-u", "--url", help="INCEpTION instance URL")
@click.option("-U", "--user", help="User name")
@click.option(
    "--regex", is_flag=True, default=False, help="Whether to interpret the project name as a regular expression"
)
@click.option("--dry-run", is_flag=True, default=False, help="Log actions would be performed without performing them")
@click.option("-o", "--out", default=".", type=click.Path())
@click.argument("projects", nargs=-1)
def export_projects(url: str, user: Optional[str], regex: bool, dry_run: bool, out: Optional[str], projects: List[str]):
    """Exports projects and saves them to disk."""

    client = make_client(url, user=user)

    if regex:
        projects = list_matching_projects(client, projects)
    else:
        projects = get_project_from_name(client, projects[0])

    target_folder = Path(out)
    target_folder.mkdir(parents=True, exist_ok=True)

    for project in projects:
        target_path = target_folder / (project.project_name + ".zip")

        _log.info("Exporting project [%s] to [%s]", project, target_path)
        if not dry_run:
            zip_content = client.api.export_project(project, project_format=InceptionFormat.BIN)
            with target_path.open("wb") as zip_file:
                zip_file.write(zip_content)


@click.command(name="import")
@click.option("-u", "--url", help="INCEpTION instance URL")
@click.option("-U", "--user", help="User name")
@click.argument("projects", type=click.File("rb"), nargs=-1)
def import_projects(url: str, user: Optional[str], projects: List[str]):
    """Imports the given projects."""

    client = make_client(url, user=user)

    for project in projects:
        _log.info("Importing project [%s] ...", project.name)
        imported_project = client.api.import_project(project)
        _log.info("Imported project as [%s]", imported_project.project_name)


@click.command(name="list")
@click.option("-u", "--url", help="INCEpTION instance URL")
@click.option("-U", "--user", help="User name")
def list_projects(url: str, user: Optional[str]):
    """Lists the projects."""

    client = make_client(url, user=user)

    projects = client.api.projects()
    for project in projects:
        _log.info("[%s]", project.project_name)


@click.command(name="delete")
@click.option("-u", "--url", help="INCEpTION instance URL")
@click.option("-U", "--user", help="User name")
@click.option(
    "--regex", is_flag=True, default=False, help="Whether to interpret the project name as a regular expression"
)
@click.option("--dry-run", is_flag=True, default=False, help="Log actions would be performed without performing them")
@click.argument("projects", nargs=-1)
def delete_project(url: str, user: Optional[str], regex: bool, dry_run: bool, projects: List[str]):
    """
    Deletes the given projects.
    """

    client = make_client(url, user=user)

    if regex:
        projects = list_matching_projects(client, projects)
    else:
        projects = get_project_from_name(client, projects[0])

    for project in projects:
        _log.info("Deleting [%s]", project.project_name)
        if not dry_run:
            client.api.delete_project(project)
