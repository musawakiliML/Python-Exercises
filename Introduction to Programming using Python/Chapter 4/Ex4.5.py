'''
*4.5 (Find future dates) Write a program that prompts the user to enter an integer 
for today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). 
Also prompt the user to enter the number of days after today for a future day 
and display the future day of the week.
'''
# get user input
todays_day = eval(input("Enter Today's Day:"))
days_elapsed = eval(input("Enter the number of days elapsed since today:"))

# determine the current day
future_day = (todays_day + days_elapsed) % 7
x = ""

if future_day == 0:
    x = "Sunday"   
elif future_day == 1:
    x = "Monday"
elif future_day == 2:
    x = "Tuesday"
elif future_day == 3:
    x = "Wednesday"
elif future_day == 4:
    x = "Thursday"
elif future_day == 5:
    x = "Friday"
elif future_day == 6:
    x = "Saturday"

if todays_day == 0:
    todays_day = "Sunday"
elif todays_day == 1:
    todays_day = "Monday"
elif todays_day == 2:
    todays_day = "Tuesday"
elif todays_day == 3:
    todays_day = "Wednesday"
elif todays_day == 4:
    todays_day = "Thursday"
elif todays_day == 5:
    todays_day = "Friday"
elif todays_day == 6:
    todays_day = "Saturday"

print(f"Today is {todays_day} and the future day is {x}")