'''
*3.2 (Geometry: great circle distance) The great circle distance is the distance between two points on the surface of a sphere. 

Let (x1, y1) and (x2, y2) be the geographical latitude and longitude of two points. 
The great circle distance between the two points can be computed using the following formula:
    
    d= radius * arccos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))
    
Write a program that prompts the user to enter the latitude and longitude of two points on the earth in degrees and displays its great circle distance. 

The average earth radius is 6,371.01 km. Note that you need to convert the degrees into radians using the math.radians function since the Python trigonometric functions use radians. 

The latitude and longitude degrees in the formula are for north and west. 
Use negative to indicate south and east degrees. 
'''
import math

# Get input from user
latitude_1, longitude_1 = eval(input("Enter point 1 (latitude and longitude) in degrees:"))
latitude_2, longitude_2 = eval(input("Enter point 2 (latitude and longitude) in degrees:"))

AVG_EARTH_RADIUS = 6371.01 # declaring average earth radius

# convert degrees to radians both latitude and longitude
latitude_1 = math.radians(latitude_1)
latitude_2 = math.radians(latitude_2)
longitude_1 = math.radians(longitude_1)
longitude_2 = math.radians(longitude_2)

# calculate great circle distance
d = AVG_EARTH_RADIUS * math.acos(math.sin(latitude_1) * math.sin(latitude_2) + math.cos(latitude_1) * math.cos(latitude_2) * math.cos(longitude_1 - longitude_2))

# Displaying Result 
print(f"The distance between the two points is {d} km")