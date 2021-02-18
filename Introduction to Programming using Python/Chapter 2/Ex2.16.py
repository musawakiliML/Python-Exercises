'''
16.(Physics: acceleration) Average acceleration is defined as the change of velocity
divided by the time taken to make the change, as shown in the following formula:

    a = (vf - vi) / t
    
Write a program that prompts the user to enter the starting velocity vi in
meters/second, the ending velocity vf in meters/second, and the time span t in
seconds, and displays the average acceleration.
'''
# Prompting user for input values
initial_velocity, final_velocity = eval(input("Enter the initial and final velocity in meters:"))
time_taken = eval(input("Enter the time taken in seconds:"))

# Calculating acceleration
acceleration = (final_velocity - initial_velocity) / time_taken

# Displaying the average acceleration
print("The Average Acceleration is {}".format(acceleration))