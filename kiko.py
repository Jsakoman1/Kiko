import json
from pathlib import Path
import sys

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
            "current_step" : 2
        }
    }
    return context

def save_context(context):
    path = Path(".tutor/state.json")
    context_text = json.dumps(context, indent=2)
    path.write_text(context_text)

def load_context():
    path = Path(".tutor/state.json")

    if path.exists():
        text = path.read_text()
        return json.loads(text)
    else:
        context = create_context()
        save_context(context)
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

def select_relevant_concepts(learner, language):
    prefix = f"{language.lower()}:"
    concepts = learner.get("concepts", [])
    
    relevant = []
    for concept in concepts:
        if concept["id"].startswith(prefix):
            relevant.append(concept["id"] + "|" + concept["stage"])
    return relevant

def main():
    arguments = sys.argv[1:]
    learner = load_learner_state()

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
            print("Current step:", context["tutor"]["current_step"])
            print("Previous languages:", learner["profile"]["previous_languages"])
            print("Relevant concepts:", select_relevant_concepts(learner, context["project"]["language"]))

if __name__ == "__main__":
    main()