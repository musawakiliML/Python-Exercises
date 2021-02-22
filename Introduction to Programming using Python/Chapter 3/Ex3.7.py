'''
3.7 (Random character) Write a program that displays a random uppercase letter 
using the time.time() function.
'''

# getting time module
import time

# get the random time value in integer
t = int(time.time())

# getting a random character by using ord and chr function
random_character = chr(ord('A') + t % (ord('Z') - ord('A') + 1))

# Displaying the random Character
print(f"Random Character:{random_character}")