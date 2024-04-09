#!/usr/bin/env python3

def main():

    numbeers = int(input("How many beers are going on the wall?\n"))
    
    if numbeers <100:
        for beers in range(numbeers):
            strbeers = str(numbeers)
            print(strbeers + " bottles of beer on the wall!")
            print(strbeers + " bottles of beer on the wall!", strbeers + " bottles of beer! You take one down, pass it around!")
            numbeers = numbeers - 1
            if numbeers == 0:
                print("No more bottles of beer on the wall!")
    else:
        print("Please input a number from 1 to 99.")
        main()

main()

