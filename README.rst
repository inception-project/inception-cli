inception-cli
=============

*Command line tool for INCEpTION.*


Purpose
-------

This project provides a command line tool for the INCEpTION text annotation platform which allows
you to import, export and delete projects.


Installation
------------

So far, the INCEpTION command line tool is not available from Pypi, but you can still
install it using pip directly from this GitHub repository using the following command:

.. code:: shell

    $ pip install -U git+https://github.com/inception-project/inception-cli.git


Prepare INCEpTION to be able to use the Remote API
--------------------------------------------------

- enable the remote API
    - go to INCEpTIONs home folder
    - open INCEpTIONs `settings.properties` file
    - add the line ``remote-api.enabled=true``
    - restart INCEpTION
    - now it should be possible to assign the role `ROLE_REMOTE` to a user
- create a remote-api user
    - got to the user management page
    - create a new user, e.g. remote-api
    - assign at least the roles ``ROLE_ADMIN``, ``ROLE_USER`` and ``ROLE_REMOTE``
    - make sure that the new user is enabled
    - click on ``Save``

Usage
-----

Run it from the command line to get a list of the available commands:

.. code:: shell

    $ inception project

All commands require the following options:

- "-u", "--url" INCEpTION instance URL
- "-U", "--user" User name of the previously created user, you will be prompted to enter the
password

If you do not want to enter this information multiple times, just set the environment variables
``INCEPTION_USERNAME`` and ``INCEPTION_PASSWORD``according to the previously created user in the
console session where you invoke the CLI.
You can also set the INCEpTION instance url by the environment variable ``INCEPTION_HOST``.

delete
^^^^^^
Deletes the given projects.

Options:

- "-u", "--url" INCEpTION instance URL
- "-U", "--user" User name of the previously created user, you will be prompted to enter the password
- "--regex" (default=False) Whether to interpret the project name as a regular expression
- "--dry-run" (default=False) Whether log actions would be performed without performing them
- "--projects" Names / regular expression of the projects which should be deleted

export
^^^^^^
Exports projects and saves them to disk.

Options:

- "-u", "--url" INCEpTION instance URL
- "-U", "--user" User name of the previously created user, you will be prompted to enter the password
- "--regex" (default=False) Whether to interpret the project name as a regular expression
- "--dry-run" (default=False) Whether log actions would be performed without performing them
- "-o", "--out" (default=".") Where the exported projects should be saved
- "--projects" Names / regular expression of the projects which should be exported

import
^^^^^^
Imports the given projects.

Options:

- "-u", "--url" INCEpTION instance URL
- "-U", "--user" User name of the previously created user, you will be prompted to enter the password
- "--projects" Names of the zip-files which should be imported


list
^^^^
Lists the projects.

Options:

- "-u", "--url" INCEpTION instance URL
- "-U", "--user" User name of the previously created user, you will be prompted to enter the password



