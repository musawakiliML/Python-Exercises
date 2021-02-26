'''
3.10 (Reverse number) Write a program that prompts the user to enter a four-digit integer 
and displays the number in reverse order. 

'''
# get user input
number = eval(input("Enter a number:"))

# Reverse number
first_digit = number // 1000
second_digit = number // 100 % 10
third_digit = number % 100 // 10
fourth_digit = number % 10 

# Display Result
print(f"The Number:{number} is")
print(fourth_digit, end="")
print(third_digit, end="")
print(second_digit, end="")
print(first_digit, end="")