'''
3.1 (Geometry: area of a pentagon) Write a program that prompts the user to enter the length from the center of a pentagon to a vertex and computes the area of the pen- tagon. 
The formula for computing the area of a pentagon is

        Area = (3 * (3 ** 0.5) / 2) * s ** 0.5
        
where s is the length of a side. The side can be computed using the formula 

        s = 2 * radius * sin(pi / 5),
        
where r is the length from the center of a pentagon to a vertex.
'''
# Getting math libary to use sin() method
import math

# get user input
length = eval(input("Enter the length from the center to a vertex:"))

# Calculating the area
s = 2 * length * math.sin(math.pi / 5 )
area = (3 * math.sqrt(3) / 2) * (s ** 2)

# Displaying Results
print(f"The Area of the pentagon is {area}")