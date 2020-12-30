"""Tests for our main inception CLI module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from inception import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['inception', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)

        output = popen(['inception', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['inception', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip(), VERSION)
