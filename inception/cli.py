"""
inception

Usage:
  inception exportprojects [-u URL] [TARGET]
  inception -h | --help
  inception --version

Options:
  -u URL, --url=URL                 URL of the INCEpTION instance.
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  inception exportprojects

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/rdegges/skele-cli
"""


from inspect import getmembers, isclass

from docopt import docopt

from inception import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import inception.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items(): 
        if hasattr(inception.commands, k) and v:
            module = getattr(inception.commands, k)
            inception.commands = getmembers(module, isclass)
            command = [command[1] for command in inception.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
