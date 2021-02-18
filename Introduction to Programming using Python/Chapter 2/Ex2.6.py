'''
**6. (Sum the digits in an integer) Write a program that reads an integer between 0 and 1000 
and adds all the digits in the integer. For example, if an integer is 932, 
the sum of all its digits is 14. (Hint: Use the % operator to extract digits, 
and use the // operator to remove the extracted digit. 
For instance, 932 % 10 = 2 and 932 // 10 = 93.)
'''
# Getting a digit between 0 and 1000 from the user
digits = eval(input("Enter a digit between 0 and 1000:"))

# Getting digits one by one
first_number = digits // 100
second_number = (digits // 10) % 10
third_number = digits % 10

# Summing up the digits
sum_of_digits = first_number + second_number + third_number

# Displaying the result
print("The Digits are {} {} {}".format(first_number,second_number,third_number))
print("Their Sum Is: {}".format(sum_of_digits))