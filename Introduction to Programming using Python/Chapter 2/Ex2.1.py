'''
1.(Convert Celsius to Fahrenheit) Write a program that reads a Celsius degree from
the console and converts it to Fahrenheit and displays the result. The formula for
the conversion is as follows:

    fahrenheit = (9 / 5) * celsius + 32
'''

# Takes in the celsius value from user
celsius = input("Enter Degree in Celsius:")

# Computes the value of fahrenheit
fahrenheit = (9 / 5) * int(celsius) + 32

#Displays the result
print("{} Celsius is {} Fahrenheit".format(celsius, fahrenheit))