'''
*10.(Physics: find runway length) Given an airplane’s acceleration a and take-off
speed v, you can compute the minimum runway length needed for an airplane to
take off using the following formula: 

    Lenght = (v x v) / 2 x a.

Write a program that prompts the user to enter v in meters/second (m/s) and the
acceleration a in meters/second squared and displays the minimum runway
length.
'''
# Prompting User for inputs
speed, acceleration = eval(input("Enter the Speed and acceleration:"))

# Computing the runway length
lenght = (speed ** 2) / (2 * acceleration)

# Display Results
print("The minimum runway length for this airplane is {}".format(lenght))