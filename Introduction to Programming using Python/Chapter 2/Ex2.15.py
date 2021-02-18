'''
15.(Geometry: area of a hexagon) Write a program that prompts the user to enter the
side of a hexagon and displays its area. The formula for computing the area of a
hexagon is

    Area = (3 * (3)**0.5 / 2) * s ** 2, 
 where s is the length of a side.
'''
# Prompting User for input values
sides = eval(input("Enter the side:"))

# Calculating the area
area = (3 * (3) ** 0.5 / 2) * sides ** 2

# Displaying the results 
print("The area of the hexagon is {}".format(area))