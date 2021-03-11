'''
*4.1 (Algebra: solve quadratic equations) The two roots of a quadratic equation, 
for example, ax2 + bx + c = 0, can be obtained using the following formula:
        
        r1 = -b + sqrt(b^2 - 4*a*c) / 2*a and r2 = -b - sqrt(b^2 - 4*a*c) / 2*a
        
b^2 - 4*a*c is called the discriminant of the quadratic equation. 
If it is positive, the equation has two real roots. 
If it is zero, the equation has one root. 
If it is negative, the equation has no real roots.

Write a program that prompts the user to enter values for a, b, and c 
and displays the result based on the discriminant. If the discriminant is positive, 
display two roots. If the discriminant is 0, display one root. 
Otherwise, display The equa- tion has no real roots. 
'''
import math 

# Get user input
a = eval(input("Enter a:"))
b = eval(input("Enter b:"))
c = eval(input("Enter c:"))

# Compute the discriminant and the Roots
r_1 = (-b + math.sqrt(math.pow(b,2) - 4 * a * c)) / (2 * a)
r_2 = (-b - math.sqrt(math.pow(b,2) - 4 * a * c)) / (2 * a)

discriminant = math.pow(b,2) - 4 * a * c

# Displaying results using If selections
if discriminant > 0:
    print(f"The Equations Has Two Real Roots {r_1} and {r_2}.")
    
elif discriminant == 0:
    print(f"The Equation Has One Root {r_1}.")
    
else:
    print("The Equation Has No Real Roots.")
