"""The export projects command"""

from json import dumps
from pathlib import Path

from .base import Base
from pycaprio import Pycaprio
from pycaprio.mappings import InceptionFormat


class ExportProjects(Base):
    def run(self):
        host = self.options["--url"]
        output_folder = self.options["TARGET"]

        if output_folder:
            output_folder = Path(output_folder)
            output_folder.mkdir(parents=True, exist_ok=True)

        else:
            output_folder = Path()

        client = Pycaprio(host)

        # List projects
        projects = client.api.projects()

        # Export all projects
        for project in projects:
            print(f"Exporting project {project}... ", end='')
            zip_content = client.api.export_project(project, project_format=InceptionFormat.BIN)
            with open(output_folder.joinpath(project.project_name+".zip"), 'wb') as zip_file:
                zip_file.write(zip_content)
            print(f"done.")
