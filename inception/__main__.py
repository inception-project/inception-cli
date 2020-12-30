import click

from inception.commands import project


@click.group(help="CLI tool for INCEpTION")
def cli():
    pass


cli.add_command(project.export_projects)


if __name__ == '__main__':
    cli()
