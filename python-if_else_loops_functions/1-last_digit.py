#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = number % 10
if lastd > 5:
    print(f"Last digit of {number} is {lastd} and is greater than 5")
if lastd == 0:    
    print(f"Last digit of {number} is {lastd} and is 0")
if lastd != 0 and lastd < 6:
    print(f"Last digit of {number} is {lastd} and is less than 6 and not 0")
