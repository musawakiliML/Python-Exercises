'''
22.(Population projection) The US Census Bureau projects population based on the
following assumptions:

    One birth every 7 seconds
    One death every 13 seconds
    One new immigrant every 45 seconds

Write a program to display the population for each of the next five years. Assume the
current population is 312032486 and one year has 365 days. Hint: in Python, you
can use integer division operator // to perform division. The result is an integer. For
example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5). 
Make the program to prompt the user to enter the number of years and displays 
the population after that many years.
'''
# Prompting user for input value
number_of_years = eval(input("Enter the Number of years:"))

#Calculating the population 
total_seconds_per_year = 60 * 60 * 24 * 365
total_births_per_year = total_seconds_per_year // 7
total_deaths_per_year = total_seconds_per_year // 13
total_immigrants_per_year = total_seconds_per_year // 45
current_population = 312032486
new_population = current_population + ((total_births_per_year + total_immigrants_per_year - total_deaths_per_year) * number_of_years)

# Displaying results
print("The Population in 5 years is {}".format(new_population))