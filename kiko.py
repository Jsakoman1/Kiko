import sys

def main():
    arguments = sys.argv[1:]
    context = {
        "mission" : "AIS",
        "rules" : ['Keep the code simple'],
        "notes" : ['The project uses Python']
    }

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

if __name__ == "__main__":
    main()