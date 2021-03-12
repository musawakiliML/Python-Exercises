'''
**4.4 (Game: learn addition) Write a program that generates two integers under 100 
and prompts the user to enter the sum of these two integers. 
The program then reports true if the answer is correct, false otherwise. 
The program is similar to Listing 4.1.
'''
import random

# generating two random integers
integer_1 = random.randint(0,100)
integer_2 = random.randint(0,100)

# Get user Input

get_sum = eval(input(f"What is {integer_1} + {integer_2}?"))

# Displaying result
if integer_1 + integer_2 == get_sum:
    print(f"{integer_1} + {integer_2} = {get_sum} is {integer_1 + integer_2 == get_sum}")
else:
    print(f"{integer_1} + {integer_2} = {get_sum} is {integer_1 + integer_2 == get_sum}")