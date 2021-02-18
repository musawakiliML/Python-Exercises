'''
*18.(Current time) Create a program that displays the
current time in GMT. Revise the program so that it prompts the user to enter the
time zone in hours away from (offset to) GMT and displays the time in the specified
time zone.
'''
import time
# Prompting user for Time zone Input value
timeZone = eval(input("Enter the time zone Offset to GMT:"))

# Getting Current time
currentTime = time.time()

# Getting Total Seconds
totalSeconds = int(currentTime)

# get current seconds
currentSecond = totalSeconds % 60

# obtaining total minutes
totalMinutes = totalSeconds // 60

# get current minutes
currentMinute = totalMinutes % 60

# obtaining total hours
totalHours = totalMinutes // 60

# get current hour
currentHour = totalHours % 24

# Obtaining GMT Offset time zone
currentHour = currentHour + timeZone

# Displaying Current time
print("The Current Time is -:- {} : {} : {} ".format(currentHour,currentMinute,currentSecond))