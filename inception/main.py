import logging

import click

from inception.commands import export_projects


@click.group(help="CLI tool for INCEpTION")
def cli():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S", level=logging.INFO
    )


cli.add_command(export_projects)


if __name__ == "__main__":
    cli()
