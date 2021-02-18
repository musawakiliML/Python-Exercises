'''
2.(Compute the volume of a cylinder) Write a program that reads in the radius and length of a cylinder and computes the area and volume using the following formulas:

    area = radius x radius x π

    volume = area * length

'''

# Takes in the Radius and Length
radius, lenght = eval(input("Enter Radius and Lenght of the Cylinder:"))

# Declaring a constant Pi value
PI = 3.14159

# Computes The Area and Volume
area = radius * radius * PI
volume = area * lenght

# Displays The Result
print("The Area Is", area)
print("The Volume Is",volume)