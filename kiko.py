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


def main():
    arguments = sys.argv[1:]

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

if __name__ == "__main__":
    main()