inception-cli
=========

*Command line tool for INCEpTION.*


Purpose
-------

This project provides a command line tool for the INCEpTION text annotation platform.


Usage
-----

Run it from the command line to get a list of the available commands:

.. code:: shell

    $ inception

In order to use commands that access the INCEpTION Remote API, you need to:

* enable the remote API by adding the line `remote-api.enabled=true` to the INCEpTION `settings.properties` file and
  re-start INCEpTION
* add the role `ROLE_REMOTE` to a user in the user management of INCEpTION

Authentication can either be done via the command line argument `-u` or `--user`, then you will be prompted to
enter the password. Alternatively, set the environment variables `INCEPTION_USERNAME` and `INCEPTION_PASSWORD`
according to the user you have given `ROLE_REMOTE` in the console session where you invoke the CLI.
