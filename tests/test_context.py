import unittest

from kiko.cli import create_context

class CliTests(unittest.TestCase):
    def test_create_context(self):
        context = create_context()

        self.assertEqual(context["project"]["name"], "Kiko")