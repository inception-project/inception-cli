import logging

import click

from inception.commands import export_projects
from inception.commands.project import import_project, delete_project, list_projects


@click.group(help="CLI tool for INCEpTION")
def cli():
    logging.basicConfig(
        # format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S", level=logging.INFO
        format = "%(message)s", level = logging.INFO
    )


@click.group(help="CLI tool for INCEpTION")
def project():
    pass


project.add_command(export_projects)
project.add_command(import_project)
project.add_command(list_projects)
project.add_command(delete_project)

cli.add_command(project)

if __name__ == "__main__":
    cli()
