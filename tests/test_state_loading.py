import json
import unittest

from pathlib import Path
from tempfile import TemporaryDirectory

from kiko.cli import ProjectStateError, create_context, load_context


class ProjectStateLoadingTests(unittest.TestCase):
    def test_loads_valid_saved_state(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            state = create_context()
            path.write_text(json.dumps(state))

            result = load_context(path)

            self.assertEqual(result, state)

    def test_creates_and_loads_default_state_when_missing(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            expected = create_context()

            result = load_context(path)

            self.assertEqual(result, expected)
            self.assertEqual(json.loads(path.read_text()), expected)

    def test_rejects_invalid_saved_shape(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            state = create_context()
            state["project"] = "invalid"
            path.write_text(json.dumps(state))

            with self.assertRaises(ProjectStateError):
                load_context(path)

    def test_rejects_future_saved_version(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            state = create_context()
            state["version"] = 2
            path.write_text(json.dumps(state))

            with self.assertRaises(ProjectStateError):
                load_context(path)

    def test_does_not_rewrite_invalid_saved_state(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            state = create_context()
            state["mission"] = None
            original_text = json.dumps(state, indent=2)
            path.write_text(original_text)

            with self.assertRaises(ProjectStateError):
                load_context(path)

            self.assertEqual(path.read_text(), original_text)
