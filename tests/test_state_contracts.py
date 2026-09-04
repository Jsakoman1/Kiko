import unittest

from kiko.cli import (
    LearnerStateError,
    ProjectStateError,
    create_context,
    validate_learner_state,
    validate_project_state,
)


def create_learner_state():
    return {
        "schema_version": 1,
        "profile": {
            "explanation_language": "Croatian",
            "help_preference": "guided",
            "previous_languages": ["Java"],
            "current_learning_goals": ["Python"],
        },
        "concepts": [],
    }

class ProjectStateRootTests(unittest.TestCase):
    def test_project_state_version_valid(self):
        state = create_context()
        result = validate_project_state(state)
        self.assertEqual(result, state)

    def test_project_state_not_dictionary(self):
        state = "Text"
        with self.assertRaises(ProjectStateError):
            result = validate_project_state(state)
        
    def test_project_state_version_in_future(self):
        state = {"version": 4}
        with self.assertRaises(ProjectStateError):
            result = validate_project_state(state)
    
    def test_project_state_version_mising(self):
        state = {}
        with self.assertRaises(ProjectStateError):
            result = validate_project_state(state)

class ProjectStateFieldTests(unittest.TestCase):
    def test_project_name_missing(self):
        state = create_context()
        state["project"] = {"language": "python"}
        with self.assertRaises(ProjectStateError):
            result = validate_project_state(state)
    
    def test_context_valid(self):
        state = create_context()
        result = validate_project_state(state)
        self.assertEqual(result, state)
    
    def test_rules_type_invalid(self):
        state = create_context()
        state["rules"] = "text"
        with self.assertRaises(ProjectStateError):
            result = validate_project_state(state)
    
    def test_project_not_dictionary(self):
        state = create_context()
        state["project"] = "text"
        with self.assertRaises(ProjectStateError):
            result = validate_project_state(state)
    
    def test_additional_unknown_field(self):
        state = create_context()
        state["future_setting"] = "kept"
        
        result = validate_project_state(state)

        self.assertEqual(result["future_setting"], "kept")


class LearnerStateTests(unittest.TestCase):
    def test_accepts_valid_learner_state(self):
        state = create_learner_state()

        result = validate_learner_state(state)

        self.assertEqual(result, state)

    def test_rejects_non_dictionary_learner_state(self):
        with self.assertRaises(LearnerStateError):
            validate_learner_state([])

    def test_rejects_missing_profile(self):
        state = create_learner_state()
        state.pop("profile")

        with self.assertRaises(LearnerStateError):
            validate_learner_state(state)

    def test_rejects_wrong_profile_field_type(self):
        state = create_learner_state()
        state["profile"]["previous_languages"] = "Java"

        with self.assertRaises(LearnerStateError):
            validate_learner_state(state)

    def test_rejects_wrong_concepts_type(self):
        state = create_learner_state()
        state["concepts"] = {}

        with self.assertRaises(LearnerStateError):
            validate_learner_state(state)

    def test_rejects_project_state_shape(self):
        with self.assertRaises(LearnerStateError):
            validate_learner_state(create_context())

    def test_preserves_unknown_learner_field(self):
        state = create_learner_state()
        state["future_setting"] = "kept"

        result = validate_learner_state(state)

        self.assertEqual(result["future_setting"], "kept")

    def test_rejects_future_schema_version(self):
        state = create_learner_state()
        state["schema_version"] = 2

        with self.assertRaises(LearnerStateError):
            validate_learner_state(state)
        
