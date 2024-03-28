#!/usr/bin/env python3

## Collect input from user
hostname = input("What value should we set for hostname?\n")

## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be MTG.")
    #Printing this on two lines and stating the same thing is essentially superfluous
    print("The hostname matches expected configuration.")

# This prints to the user regardless of input
print("Exiting script.")
