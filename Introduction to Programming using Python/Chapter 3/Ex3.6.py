'''
*3.6 (Find the character of an ASCII code) Write a program that receives an ASCII code 
(an integer between 0 and 127) and displays its character. For example, if the user enters 97, 
the program displays the character a. 
'''

# Get user character
get_ascii_code = eval(input("Enter ASCII Code:"))

# Convert the ASCII code to Character
character = chr(get_ascii_code)

# Displaying the results
print(f"The ASCII Code {get_ascii_code} is Character '{character}'")