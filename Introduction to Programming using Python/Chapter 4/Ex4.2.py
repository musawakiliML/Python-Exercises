'''
*4.2 (Game: add three numbers) The program in Listing 4.1 generates two integers 
and prompts the user to enter the sum of these two integers. 
Revise the program to generate three single-digit integers 
and prompt the user to enter the sum of these three integers.
'''
import random

# get random numbers
number_1 = random.randint(0,9)
number_2 = random.randint(0,9)
number_3 = random.randint(0,9)

# Display question and accept user input
answer = eval(input(f"What is {number_1} + {number_2} + {number_3}?"))

# compare answer and display result
if number_1 + number_2 + number_3 == answer:
    print(f"{number_1} + {number_2} + {number_3} = {answer} is {number_1 + number_2 + number_3 == answer}")
else:
    print(f"{number_1} + {number_2} + {number_3} = {answer} is {number_1 + number_2 + number_3 == answer}")