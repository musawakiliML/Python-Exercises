'''
*3.5 (Geometry: area of a regular polygon) A regular polygon is an n-sided polygon in which all sides are of the same length
and all angles have the same degree (i.e., the polygon is both equilateral and equiangular). 
The formula for computing the area of a regular polygon is
             area = (n * s^2) / 4 * tan(pi / n)
Here, s is the length of a side. 
Write a program that prompts the user to enter the number of sides and 
their length of a regular polygon and displays its area.
'''
import math

# Get User input
number_of_sides = eval(input("Enter the number of sides:"))
sides = eval(input("Enter the side:"))

# Calculating the area of the pentagon
area = (number_of_sides * math.pow(sides, 2)) / 4 * math.tan(math.pi / number_of_sides)

# Displaying the results
print(f"The Area of the polygon is {area}")