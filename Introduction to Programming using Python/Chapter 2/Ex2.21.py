'''
**21.(Financial application: compound value) Suppose you save $100 each month into
a savings account with an annual interest rate of 5%.Therefore, the monthly interest
rate is 0.05 / 12 = 0.00417. After the first month, the value in the account
becomes

    100 * (1 + 0.00417) = 100.417
    
After the second month, the value in the account becomes

    (100 + 100.417) * (1 + 0.00417) = 201.252
    
After the third month, the value in the account becomes

    (100 + 201.252) * (1 + 0.00417) = 302.507

and so on.

Write a program that prompts the user to enter a monthly saving amount and
displays the account value after the sixth month. Here is a sample run of the
program:
'''
# Prompting user for monthly saving amount
monthly_saving_amount = eval(input("Enter monthy saving amount:"))

# Computing the compound value
first_month = 100 * (1 + 0.00417)
second_month = (100 + first_month) * (1 + 0.00417)
third_month = (100 + second_month) * (1 + 0.00417)
fourth_month = (100 + third_month) * (1 + 0.00417)
fifth_month = (100 + fourth_month) * (1 + 0.00417)
sixth_month = (100 + fifth_month) * (1 + 0.00417)

# Displaying results
print("After the sixth month, the account value is {}".format(sixth_month))