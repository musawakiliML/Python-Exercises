'''
**7. (Find the number of years and days) Write a program that prompts the user to
enter the minutes (e.g., 1 billion), and displays the number of years and days for
the minutes. For simplicity, assume a year has 365 days.
'''
#Taking values from user
minutes = eval(input("Enter the Minutes:"))

# Computing number of Years and Days
total_minutes_per_day = 60 * 24
minutes_per_year = total_minutes_per_day * 365
number_of_years = minutes // minutes_per_year
days = minutes % minutes_per_year // 1440

#Displaying Results
print("{} Minutes is Approximately {} Years and {} days".format(minutes, number_of_years,days))
