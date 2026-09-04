import unittest

from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
from kiko.cli import load_learner_state

class LearnerStateTests(unittest.TestCase):
    def test_missing_learner_state(self):
        with TemporaryDirectory() as temporary_home:
            with patch.object(Path,"home",return_value = Path(temporary_home)):
                learner = load_learner_state()

        self.assertEqual(learner["profile"]["previous_languages"], [])
        self.assertEqual(learner["concepts"], [])