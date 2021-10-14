'''
*4.8 (Sort three integers) Write a program that prompts the user to enter three integers
and displays them in increasing order.
'''

num1 = eval(input("Enter Number 1:"))
num2 = eval(input("Enter Number 2:"))
num3 = eval(input("Enter Number 3:"))

if (num1 > num2) and (num1 > num3):
    if num2 > num3:
        print(f"{num3}, {num2}, {num1}")
    else:
        print(f"{num2}, {num3}, {num1}")
if (num2 > num1) and (num2 > num3):
    if num1 > num3:
        print(f"{num3}, {num1}, {num2}")
    else:
        print(f"{num1}, {num3}, {num2}")
if (num3 > num2) and (num3 > num1):
    if num2 > num1:
        print(f"{num1}, {num2}, {num3}")
    else:
        print(f"{num2}, {num1}, {num3}")