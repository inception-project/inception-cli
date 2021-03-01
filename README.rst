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
- "-U", "--user" User name of the previously created user, you will be prompted to enter the password

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



Use inception-cli to easily migrate from WebAnno to INCEpTION
-------------------------------------------------------------

1. Enable the remote API in WebAnno
    - go to WebAnnos home folder
    - open WebAnnos `settings.properties` file
    - add the line ``remote-api.enabled=true``
    - restart WebAnno
    - now it should be possible to assign the role `ROLE_REMOTE` to a user
2. Create a remote-api user in WebAnno
    - got to the user management page
    - create a new user, e.g. remote-api
    - assign at least the roles ``ROLE_ADMIN``, ``ROLE_USER`` and ``ROLE_REMOTE``
    - make sure that the new user is enabled
    - click on ``Save``
3. Export all projects from WebAnno using inception-cli
    - install inception-cli
        .. code:: shell

            $ pip install -U git+https://github.com/inception-project/inception-cli.git
    - export all projects from WebAnno (replace WEBANNO_URL and WEBANNO_REMOTE_API_USERNAME with the url of your WebAnno instance and the name of the user created in step 2.)
        .. code:: shell

            $ python inception project export -u WEBANNO_URL -U WEBANNO_REMOTE_API_USERNAME --regex .*
    - enter the password of the user created in step 2. when asked
    - inception-cli creates one zip-file for each exported project in the current directory
#. Enable the remote API in INCEpTION
    - go to INCEpTIONs home folder
    - open INCEpTIONs `settings.properties` file
    - add the line ``remote-api.enabled=true``
    - restart INCEpTION
    - now it should be possible to assign the role `ROLE_REMOTE` to a user
#. Create a remote-api user in INCEpTION
    - got to the user management page
    - create a new user, e.g. remote-api
    - assign at least the roles ``ROLE_ADMIN``, ``ROLE_USER`` and ``ROLE_REMOTE``
    - make sure that the new user is enabled
    - click on ``Save``
#. Import all exported projects to INCEpTION using inception-cli (replace WEBANNO_URL and WEBANNO_REMOTE_API_USERNAME with the url of your WebAnno instance and the name of the user created in step 2 and replace PATH_TO_EXPORTED_PROJECT_1 etc. with the paths to each of the zip-files created in step 3)
     .. code:: shell

            $ python inception project export -u INCEPTION_URL -U INCEPTION_REMOTE_API_USERNAME PATH_TO_EXPORTED_PROJECT_1, PATH_TO_EXPORTED_PROJECT_2, PATH_TO_EXPORTED_PROJECT_3
