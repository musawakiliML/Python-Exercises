'''
*13.(Split digits) Write a program that prompts the user to enter a four-digit integer
and displays the number in reverse order.
'''
# Prompting User for input
four_digit_number = eval(input("Enter a four digit number:"))

# Splitting digits
first_digit = four_digit_number // 1000
second_digit = (four_digit_number // 100) % 10
third_digit = (four_digit_number % 100) // 10
fourth_digit = (four_digit_number % 100) % 10

# Displaying results
print("The Numbers Are: {} {} {} {}".format(first_digit,second_digit,third_digit,fourth_digit))
