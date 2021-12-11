'''
4.10 (Game: multiplication quiz) Listing 4.4, SubtractionQuiz.py, randomly generates
a subtraction question. Revise the program to randomly generate a multiplication
question with two integers less than 100.
'''
import random

num_1 = random.randint(0,100)
num_2 = random.randint(0,100)

question = input(f"What is {num_1} * {num_2}?")

if question == num_1 * num_2:
    print("Correct Answer!")
else:
    print("Wrong Answer! \n", "Correct Answer:",num_1*num_2)