'''
*4.3 (Algebra: Solve 2 x 2 Linear Eqautions) You can use the Cramer's to solve the following 2 x 2 system of linear equation:
        
        ax + by = e      x = (ed - bf) / (ad - bc)
        cx + dy = f      y = (af - ec) / (ad - bc)
        
Write a program that prompts the user to enter a,b,c,d,e, and f and display the result. 
If ad - bc = 0,report that The Equation has no solution.
'''
# Get User Input
a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f:"))

# Calculating the values of x and y
x = (e * d - b * f) / (a * d - b * c)
y = (a * f - e * c) / (a * d - b * c)

if (a * d - b * c) == 0:
    print("The Equation Has No Solution.")
else:
    print(f"X is {x} and Y is {y}.")