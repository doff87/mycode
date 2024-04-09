#!/usr/bin/env python3

farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

def main():
    print("Place holder for future main function")

def challenge1():
    NE_farm_animals = farms[0]["agriculture"]
    
    for x in NE_farm_animals:
        print(x)

def challenge2():
    for farm in farms:
        print("-", farm["name"])
    choice = input("Pick a farm!\n")

    for farm in farms:
        if farm["name"].lower() == choice.lower():
            print(farm["agriculture"])

def challenge3():
    
    discard = ["carrots", "celery", "bananas", "apples", "oranges"]

    for farm in farms:
        print("-", farm["name"])
    choice = input("Pick a farm!\n")

    for farm in farms:
        if farm["name"].lower() == choice.lower():
            for animal in farm["agriculture"]:
                if animal not in discard:
                    print(animal)

challenge3()

