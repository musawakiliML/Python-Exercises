'''
4. (Convert pounds into kilograms) Write a program that converts pounds into
kilograms. The program prompts the user to enter a value in pounds, converts it to
kilograms, and displays the result. One pound is 0.454 kilograms.

'''

# Prompting the user to enter value in pounds
pounds = eval(input("Enter a value in pounds:"))

# Converting pounds to kilograms
kilograms = pounds * 0.454

#Displays the result using format string
print("{} Pounds is {} Kilograms".format(pounds, kilograms))