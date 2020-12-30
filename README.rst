inception-cli
=============

*Command line tool for INCEpTION.*

.. code-block::

    Usage: inception [OPTIONS] COMMAND [ARGS]...

      CLI tool for INCEpTION

    Options:
      --help  Show this message and exit.

    Commands:
      export-projects  Exports all projects and saves them to disk.



Purpose
-------

This project provides a command line tool for the INCEpTION text annotation platform.


Usage
-----

Authentication can either be done via the command line argument `-u` or `--user`, then you will be prompted to
enter the password. Alternatively, you can provide the password via the environment variable `INCEPTION_PASSWORD`.