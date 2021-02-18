'''
*5.(Financial application: calculate tips) Write a program that reads the subtotal and
the gratuity rate and computes the gratuity and total. For example, if the user
enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
as the gratuity and 11.5 as the total.

'''

# Getting Subtotal and gratuity rate from the user
subtotal, gratuity_rate = eval(input("Enter The Subtotal and a Gratuity rate:"))

# Computing Gratuity and total amount
gratuity = (gratuity_rate / 100) * subtotal
total = subtotal + gratuity

# Displaying the results
print("The Gratuity is {} and the total is {}".format(gratuity,total))