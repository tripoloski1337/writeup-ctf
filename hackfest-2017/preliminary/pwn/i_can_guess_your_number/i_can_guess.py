#!/usr/bin/env python

import random
import sys
# socat -s -d -d -d TCP-LISTEN:13342,reuseaddr,fork EXEC:'/usr/bin/python i_can_guess.py'

def print_(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def println(s):
    print_(s + "\n")

def printFlag():
    f = open("flag.txt","r").read()
    print_(f)

def main():
    correct = 0

    while True:
        try:
            num = random.randint(1,999999)
            print_("[?] Guess my number : ")
            guess = input()
            if guess == num:
                println("[+] That's correct!")
                correct += 1
            else:
                println("[-] Wrong guess. The correct one is "+str(num))
                break
            if correct == 20:
                printFlag()
                break
        except:
            println("[-] Incorrect input")
            break


if __name__ == "__main__":
    main()
