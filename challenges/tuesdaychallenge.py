#!/usr/env/python3

mylist = [1,2,3,4,5, "Python"]

def main():

    name_input = input("What is your name? \n")

    # This is what you should see when print runs:
    # Hi <name>! Welcome to Day 2 of Python Training!
    print("Hi", name_input + "! Welcome to Day", str(mylist[1]) + " of", str(mylist[5]) + " Training!")


main() 
