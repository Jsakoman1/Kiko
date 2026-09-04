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

def require_typed_field(container, field, expected_type, error_type):
    value = container.get(field)
    if not isinstance(value, expected_type):
        raise error_type(f"Invalid field: {field}")
    return value

def validate_project_state(state):
    if not isinstance(state, dict):
        raise ProjectStateError("State is not a dictionary!")
    if state.get("version") != 1:
        raise ProjectStateError("State version is not 1")
    if not isinstance(state.get("mission"), str):
        raise ProjectStateError("State Mission is not a String")
    if not isinstance(state.get("rules"), list):
        raise ProjectStateError("State Rules is not a list")
    if not isinstance(state.get("notes"), list):
        raise ProjectStateError("State notes is not a list!")
    if not isinstance(state.get("project"), dict):
        raise ProjectStateError("Project is not a dictionary!")
    if not isinstance(state["project"].get("name"), str):
        raise ProjectStateError("Project name is not a String!")
    if not isinstance(state["project"].get("language"), str):
        raise ProjectStateError("Project language is not a String!")
    if not isinstance(state.get("tutor"), dict):
        raise ProjectStateError("State Tutor is not a dictionary!")
    if not isinstance(state["tutor"].get("help_preference"), str):
        raise ProjectStateError("Project Tutor Help-reference is not a String!")
    if not isinstance(state["tutor"].get("runtime_checkpoint"), str):
        raise ProjectStateError("Project Tutor Runtime-checkpoint is not a String!")

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
