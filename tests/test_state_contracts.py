import unittest

from kiko.cli import (
    FeedbackStateError,
    LearnerStateError,
    ProjectStateError,
    SessionStateError,
    create_context,
    validate_learner_state,
    validate_feedback_state,
    validate_project_state,
    validate_session_state,
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


def create_feedback_state():
    return {
        "schema_version": 1,
        "candidates": [
            {
                "category": "lesson-clarity",
                "violated_contract": "Explain new syntax before use",
                "observation": "A syntax explanation was missing",
                "proposed_improvement": "Add a syntax preflight",
                "regression_target": "Reject lessons with undeclared syntax",
            }
        ],
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


class SessionStateTests(unittest.TestCase):
    def test_accepts_empty_session(self):
        state = {"schema_version": 1}

        result = validate_session_state(state)

        self.assertEqual(result, state)

    def test_accepts_identified_session(self):
        state = {
            "schema_version": 1,
            "provider": "codex-app-server",
            "thread_id": "thread-123",
        }

        result = validate_session_state(state)

        self.assertEqual(result, state)

    def test_accepts_session_without_thread_id(self):
        state = {"schema_version": 1, "provider": "codex-app-server"}

        result = validate_session_state(state)

        self.assertEqual(result, state)

    def test_rejects_project_state_fields(self):
        with self.assertRaises(SessionStateError):
            validate_session_state(create_context())

    def test_rejects_learner_state_fields(self):
        with self.assertRaises(SessionStateError):
            validate_session_state(create_learner_state())

    def test_rejects_wrong_provider_type(self):
        state = {"schema_version": 1, "provider": 42}

        with self.assertRaises(SessionStateError):
            validate_session_state(state)

    def test_rejects_wrong_thread_id_type(self):
        state = {"schema_version": 1, "thread_id": []}

        with self.assertRaises(SessionStateError):
            validate_session_state(state)

    def test_rejects_future_schema_version(self):
        state = {"schema_version": 2}

        with self.assertRaises(SessionStateError):
            validate_session_state(state)


class FeedbackStateTests(unittest.TestCase):
    def test_accepts_empty_feedback_state(self):
        state = {"schema_version": 1, "candidates": []}

        result = validate_feedback_state(state)

        self.assertEqual(result, state)

    def test_accepts_sanitized_feedback_candidate(self):
        state = create_feedback_state()

        result = validate_feedback_state(state)

        self.assertEqual(result, state)

    def test_rejects_missing_candidate_field(self):
        state = create_feedback_state()
        state["candidates"][0].pop("observation")

        with self.assertRaises(FeedbackStateError):
            validate_feedback_state(state)

    def test_rejects_wrong_candidate_field_type(self):
        state = create_feedback_state()
        state["candidates"][0]["category"] = []

        with self.assertRaises(FeedbackStateError):
            validate_feedback_state(state)

    def test_rejects_raw_content_field(self):
        state = create_feedback_state()
        state["candidates"][0]["raw_conversation"] = "private transcript"

        with self.assertRaises(FeedbackStateError):
            validate_feedback_state(state)

    def test_rejects_project_state_shape(self):
        with self.assertRaises(FeedbackStateError):
            validate_feedback_state(create_context())

    def test_rejects_learner_state_shape(self):
        with self.assertRaises(FeedbackStateError):
            validate_feedback_state(create_learner_state())

    def test_rejects_session_state_shape(self):
        session_state = {"schema_version": 1, "provider": "codex-app-server"}

        with self.assertRaises(FeedbackStateError):
            validate_feedback_state(session_state)

    def test_rejects_future_schema_version(self):
        state = {"schema_version": 2, "candidates": []}

        with self.assertRaises(FeedbackStateError):
            validate_feedback_state(state)

    def test_invalid_feedback_does_not_affect_other_state_validators(self):
        invalid_feedback = create_feedback_state()
        invalid_feedback["candidates"][0]["source_code"] = "private source"

        with self.assertRaises(FeedbackStateError):
            validate_feedback_state(invalid_feedback)

        project_state = create_context()
        learner_state = create_learner_state()
        self.assertEqual(validate_project_state(project_state), project_state)
        self.assertEqual(validate_learner_state(learner_state), learner_state)
        
