#!/usr/bin/python3
"""print the numbers from 0 to 100 seperated by space,
for multiples of three, print Fizz instead of number
for multiples of five, print Buzz instead of number
for multiples of three and five, print FizzBuzz instead of number"""

def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
