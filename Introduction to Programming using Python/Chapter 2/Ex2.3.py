'''
3. (Convert feet into meters) Write a program that reads a number in feet, converts it
to meters, and displays the result. One foot is 0.305 meters.

'''

# Getting feet value from the user
feet = eval(input("Enter a value for feet:"))

# Converting feet to meters
meters = feet * 0.305

# Displaying Result(using formating)
print("{} Feet is {} Meters".format(feet, meters))