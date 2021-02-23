import re
from typing import Optional, List

from pycaprio import Pycaprio

import click


def make_client(url: str, user: Optional[str]) -> Pycaprio:
    if user:
        password = click.prompt("Password", hide_input=True)
        client = Pycaprio(url, authentication=(user, password))
    else:
        client = Pycaprio(url)
    return client


def list_matching_projects(client: Pycaprio, patterns: List[str]) -> List[str]:
    """
    Scans the server for any projects matching the given patterns and returns their names.
    """

    projects = []
    accessible_projects = client.api.projects()
    for pattern in patterns:
        for accessible_project in accessible_projects:
            if re.fullmatch(pattern, accessible_project.project_name) is not None:
                projects.append(accessible_project)

    return projects


def get_project_from_name(client: Pycaprio, name: str) -> List[str]:
    """
    Scans the server for any projects matching the given name and returns the corresponding project.
    """

    projects = []
    accessible_projects = client.api.projects()
    for accessible_project in accessible_projects:
        if name == accessible_project.project_name:
            projects.append(accessible_project)

    return projects
