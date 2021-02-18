'''
8.(Science: calculate energy) Write a program that calculates the energy needed to
heat water from an initial temperature to a final temperature. Your program should 
prompt the user to enter the amount of water in kilograms and the initial and final
temperatures of the water. The formula to compute the energy is

    Q = M x (finalTemperature – initialTemperature) x 4184

where M is the weight of water in kilograms, temperatures are in degrees Celsius,
and energy Q is measured in joules.
'''

# Taking Values from the user
amount_of_water = eval(input("Enter the amount of water in kilograms:"))
initial_temperature = eval(input("Enter The Initial Temperature:"))
final_temperature = eval(input("Enter the Final Temperature:"))

# Computing the energy required to heat the water
energy = amount_of_water * (final_temperature - initial_temperature) * 4184

# Displaying Results
print("The Energy Needed Is:{}".format(energy))