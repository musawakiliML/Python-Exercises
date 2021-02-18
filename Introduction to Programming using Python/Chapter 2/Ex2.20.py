'''
**20.(Financial application: calculate interest) If you know the balance and the annual
percentage interest rate, you can compute the interest on the next monthly payment
using the following formula:

    interest = balance * (annualInterestRate / 1200)

Write a program that reads the balance and the annual percentage interest rate
and displays the interest for the next month.
'''
# Prompting user for input values
balance,interest_rate = eval(input("Enter The balance and interest rate(e.g 3 for 3%):"))

# calculating interest
interest = balance * (interest_rate / 1200)

# Displaying the interest as the value
print("The Interest is: {}".format(interest))
