import json
import sys

from pathlib import Path

def create_context():
    context = {
        "mission" : "AIS",
        "rules" : ['Keep the code simple'],
        "notes" : ['The project uses Python'],
        "version" : 1,
        "project" : {
            "name": "Kiko",
            "language" : "Python"
        },
        "tutor" :  {
            "help_preference": "guided",
            "runtime_checkpoint" : "not-initialized"
        }
    }
    return context

def save_context(context, path=Path(".tutor/state.json")):
    text = json.dumps(context, indent=2)
    path.write_text(text)

def load_context(path=Path(".tutor/state.json")):
    if path.exists():
        text = path.read_text()
        context = json.loads(text)
        return validate_project_state(context)
    else:
        context = create_context()
        save_context(context,path)
        validate_project_state(context)
        return context

def load_learner_state():
    path = Path.home() / "Library" / "Application Support" / "Project Tutor" / "learner.json"

    if path.exists():
        text = path.read_text()
        return json.loads(text)
    else:
        return {
            "profile" : {
                "previous_languages": []
            },
            "concepts": []
        }

def load_personal_reference():
    path = Path.home() / "Library" / "Application Support" / "Project Tutor" / "REFERENCE.md"

    if path.exists():
        text = path.read_text()
        return text
    else:
        return ""

def select_relevant_concepts(learner, language):
    prefix = f"{language.lower()}:"
    concepts = learner.get("concepts", [])
    
    relevant = []
    for concept in concepts:
        if concept["id"].startswith(prefix):
            relevant.append(concept["id"] + "|" + concept["stage"])
    return relevant

class ProjectStateError(Exception):
    pass

class LearnerStateError(Exception):
    pass

class SessionStateError(Exception):
    pass

class FeedbackStateError(Exception):
    pass

def require_typed_field(container, field, expected_type, error_type, message=None):
    value = container.get(field)
    if not isinstance(value, expected_type):
        raise error_type(message or f"Invalid field: {field}")
    return value

def require_optional_typed_field(container, field, expected_type, error_type):
    if field not in container:
        return None
    return require_typed_field(container, field, expected_type, error_type)

def reject_unknown_fields(container, allowed_fields, error_type):
    for field in container:
        if field not in allowed_fields:
            raise error_type(f"Unexpected field: {field}")

def validate_project_state(state):
    if not isinstance(state, dict):
        raise ProjectStateError("State is not a dictionary!")
    if state.get("version") != 1:
        raise ProjectStateError("State version is not 1")

    require_typed_field(
        state, "mission", str, ProjectStateError, "State Mission is not a String"
    )
    require_typed_field(
        state, "rules", list, ProjectStateError, "State Rules is not a list"
    )
    require_typed_field(
        state, "notes", list, ProjectStateError, "State notes is not a list!"
    )

    project = require_typed_field(
        state, "project", dict, ProjectStateError, "Project is not a dictionary!"
    )
    require_typed_field(
        project, "name", str, ProjectStateError, "Project name is not a String!"
    )
    require_typed_field(
        project,
        "language",
        str,
        ProjectStateError,
        "Project language is not a String!",
    )

    tutor = require_typed_field(
        state, "tutor", dict, ProjectStateError, "State Tutor is not a dictionary!"
    )
    require_typed_field(
        tutor,
        "help_preference",
        str,
        ProjectStateError,
        "Project Tutor Help-reference is not a String!",
    )
    require_typed_field(
        tutor,
        "runtime_checkpoint",
        str,
        ProjectStateError,
        "Project Tutor Runtime-checkpoint is not a String!",
    )

    return state

def validate_learner_state(state):
    if not isinstance(state, dict):
        raise LearnerStateError("Learner state is not a dictionary")
    if state.get("schema_version") != 1:
        raise LearnerStateError("Learner state schema version is not 1")

    profile = require_typed_field(state, "profile", dict, LearnerStateError)
    require_typed_field(profile, "explanation_language", str, LearnerStateError)
    require_typed_field(profile, "help_preference", str, LearnerStateError)
    require_typed_field(profile, "previous_languages", list, LearnerStateError)
    require_typed_field(profile, "current_learning_goals", list, LearnerStateError)
    require_typed_field(state, "concepts", list, LearnerStateError)

    return state

def validate_session_state(state):
    if not isinstance(state, dict):
        raise SessionStateError("Session state is not a dictionary")
    if state.get("schema_version") != 1:
        raise SessionStateError("Session state schema version is not 1")

    allowed_fields = {"schema_version", "provider", "thread_id"}
    reject_unknown_fields(state, allowed_fields, SessionStateError)

    require_optional_typed_field(state, "provider", str, SessionStateError)
    require_optional_typed_field(state, "thread_id", str, SessionStateError)

    return state

def validate_feedback_state(state):
    if not isinstance(state, dict):
        raise FeedbackStateError("Feedback state is not a dictionary")
    if state.get("schema_version") != 1:
        raise FeedbackStateError("Feedback state schema version is not 1")

    reject_unknown_fields(
        state,
        {"schema_version", "candidates"},
        FeedbackStateError,
    )
    candidates = require_typed_field(
        state,
        "candidates",
        list,
        FeedbackStateError,
    )
    candidate_fields = {
        "category",
        "violated_contract",
        "observation",
        "proposed_improvement",
        "regression_target",
    }

    for candidate in candidates:
        if not isinstance(candidate, dict):
            raise FeedbackStateError("Feedback candidate is not a dictionary")
        reject_unknown_fields(candidate, candidate_fields, FeedbackStateError)
        for field in candidate_fields:
            require_typed_field(candidate, field, str, FeedbackStateError)

    return state


def main():
    arguments = sys.argv[1:]
    learner = load_learner_state()
    personal_reference = load_personal_reference()

    personal_reference_lines = personal_reference.splitlines()
    personal_reference_lines_preview = personal_reference_lines[:5]

    context = load_context()

    if len(arguments) == 0:
        print("Welcome to Kiko")
    else:
        if arguments[0] == "help":
            print("Kiko commands:")
            print("init")
            print("rule")
            print("note")
            print("show")
            print("help")
        elif arguments[0] == "show":
            print("Mission:", context["mission"])
            print("Rules:", context["rules"])
            print("Notes:", context["notes"])
            print("Project:", context["project"]["name"])
            print("Language:", context["project"]["language"])
            print("Help preference:", context["tutor"]["help_preference"])
            print("Runtime project checkpoint:", context["tutor"]["runtime_checkpoint"])
            print("Previous languages:", learner["profile"]["previous_languages"])
            print("Relevant concepts:", select_relevant_concepts(learner, context["project"]["language"]))
            print("Reference preview:")

            for personal_reference_line in personal_reference_lines_preview:
                print(personal_reference_line)

if __name__ == "__main__":
    main()
