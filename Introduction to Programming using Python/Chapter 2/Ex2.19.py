'''
*19.(Financial application: calculate future investment value) Write a program that
reads in an investment amount, the annual interest rate, and the number of years,
and displays the future investment value using the following formula:

    futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate)^ numberOfMonths
    
For example, if you enter the amount 1000, an annual interest rate of 4.25%,
and the number of years as 1, the future investment value is 1043.33
'''
# Reading Invesment amount from the user
investment_amount = eval(input("Enter Investment Amount:"))
annual_interest_rate = eval(input("Enter Annual Interest rate:"))
number_of_years = eval(input("Enter Number of years:"))

#Calculating the future investment value
monthly_interest_rate = annual_interest_rate / 1200
number_of_months = number_of_years * 12
future_investment_value = investment_amount * (1 + monthly_interest_rate) ** number_of_months

# Displaying The future investment 
print("Accumulated value is: {}".format(future_investment_value))