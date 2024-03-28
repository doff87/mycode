#!/usr/bin/env python3

def main():

    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)").title()

    char_stat = input("What statistic do you want to know about? (real name, power, archenemy)").lower()

    marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "power": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "power": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "power": "super strength",
  "archenemy": "adrenaline"}
             }

    print(char_name + "'s",  char_stat + " is:" + marvelchars[char_name][char_stat].title())

main()
