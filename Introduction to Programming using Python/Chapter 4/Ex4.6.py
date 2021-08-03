'''
*4.6 (Health application: BMI ) Revise Listing 4.6, ComputeBMI.py, to let users enter 
their weight in pounds and their height in feet and inches. 
For example, if a person is 5 feet and 10 inches, you will enter 5 for feet 
and 10 for inches. 
'''

# get user input
weight_in_pounds = eval(input("Enter weight in pounds:"))
feet = eval(input("Enter feet:"))
inches = eval(input("Enter inches:"))

# Converting the values
weight_in_kg = weight_in_pounds * 0.453592
feet_to_inches = feet * 12
total_inches = feet_to_inches + inches
height_in_meters = total_inches * 0.0254

# Computing the BMI Value
BMI = weight_in_kg / (height_in_meters ** 2)

print(f"BMI is {BMI}")

# Condition for BMI range
if BMI > 30.0:
    print("You are Obese")
elif BMI > 25.0:
    print("You are Overweight")
elif BMI > 18.5:
    print("You are Normal")
elif BMI < 18.5:
    print("You are Underweight")    