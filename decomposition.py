import math
# THINGS TO DO
# Get user input of a single integer (DONE)
# Divide that input by a number (2>>> increasing onwards) (DONE)
# stop if that number is over the square root of the input (DONE)
# print that number (DONE)

# getting input
number = int(input())
# for loop that is from 2 (the lowest prime number) as it progressively goes up, it wont use other numbers because the lowest primes will divide first
# and thus the numbers that arent prime that follow dont matter
for i in range (2, int(math.ceil(math.sqrt(number)))):
    while (number % i == 0):
        print (i)
        number = number/i

# if the number is anything other than 1 it will be printed, because it isnt divided by anything between 2 or the square root of the input number
if number > 1:
    print (int(number))
