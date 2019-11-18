# file: quiz1.py
# author: Sofia Kurd (sofiak@bu.edu)
# description: Quiz

import math
import random

def cone_volume(radius, height):
    """calculates and returns the volume of a cone given its dimensions"""
    return math.pi * (radius) **2 * (height) / 3

def random_date():
    """return a string containing a random calendar date in the form MM//DD"""
    return(str(random.randint(1, 12)) + "/" + str(random.randint(1, 31)))

def logs_are_cool():
    """calculates and prints the base-10 logarithm of the input"""
    logs = math.log10(int(input("Enter a positive integer: ")))
    print("The log is:" + str(logs))

# test code:
if __name__ == '__main__':
    print(cone_volume(2, 2,))
    print(random_date())
    logs_are_cool()
    
