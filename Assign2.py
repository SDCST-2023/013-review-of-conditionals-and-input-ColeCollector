"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""

import math
num = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

check = input("Is either number the hypotenuse? ")
if check == "yes": 

    if num > num2:
        hyp = num
        side = num2

    if num < num2:
        hyp = num2
        side = num
    
    answer = math.sqrt((hyp**2) - (side**2))
    print("The answer is", answer)

if check == "no":
    answer = math.sqrt((num**2) + (num2**2))
    print("The answer is", answer)


