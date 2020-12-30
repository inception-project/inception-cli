"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from inception import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, "README.rst"), encoding="utf-8") as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""

    description = "run tests"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(["py.test", "--cov=inception", "--cov-report=term-missing"])
        raise SystemExit(errno)


setup(
    name="inception",
    version=__version__,
    description="INCEpTION command line tool",
    long_description=long_description,
    url="https://github.com/inception-project/inception",
    author="INCEpTION Team",
    author_email="",
    license="Apache License 2.0",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: Apache License 2.0",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    keywords="cli",
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=["click", "pycaprio"],
    extras_require={"test": ["coverage", "pytest", "pytest-cov", "black"],},
    entry_points={"console_scripts": ["inception=inception.main:cli",],},
    cmdclass={"test": RunTests},
)
