# Kiko Python Syntax Journal

This file contains only Python syntax that you use for the first time while
building Kiko.

## Output text

`print("Welcome to Kiko")` — Prints text in the terminal, so users can see the program's output.

## Define a function

`def main():` — Defines a reusable function named `main`; the colon starts its indented body.

## Program entry point

`if __name__ == "__main__":` — Runs `main()` only when this file is started directly, not when another file imports it.

`main()` — Calls the function named `main`, so the program starts its main behavior.

## Import a module

`import sys` — Loads Python's system module so the program can read terminal arguments.

## Command-line arguments

`sys.argv` — A list containing the values passed when the script is started.

## List slicing

`sys.argv[1:]` — Takes the list from index 1 onward, skipping the script filename.

## List indexing

`arguments[0]` — Reads the first item in a list; Python indexes lists from zero.

## Conditional block

`if condition:` — Runs its indented block only when the condition is true.

## List length

`len(arguments)` — Returns how many items are in a list, useful for checking whether a command was provided.

## Alternative branch

`else:` — Runs its indented block when the preceding `if` condition is false.

## Equality comparison

`left == right` — Checks whether two values are equal and produces `True` or `False`.

## New line inside text

`"Line one\nLine two"` — Uses `\n` to start a new line inside one string.

## Dictionary

`context = {"mission": "Build Kiko"}` — Stores named values together, like a simple Java `Map`.

## List

`rules = ["Keep it simple"]` — Stores an ordered group of values that can grow later.

## Dictionary access

`context["mission"]` — Reads the value stored under the key `"mission"`.

## Multiple print values

`print("Mission:", context["mission"])` — Prints multiple values on one line with a space between them.
