'''
4.7 (Financial application: monetary units) Modify Listing 3.4, ComputeChange.py,
to display the nonzero denominations only, using singular words for single units
such as 1 dollar and 1 penny, and plural words for more than one unit such as 2
dollars and 3 pennies.

'''

# Recieve the amount
amount = eval(input("Enter an amount, for example 11.56:"))

# Convert the amount to cents
remaining_amount = int(amount * 100)

# Find the number of dollars
number_of_one_dollars = remaining_amount // 100
remaining_amount = remaining_amount % 100

#Find the numnber of quaters in the remaining amount
number_of_quaters = remaining_amount // 25
remaining_amount = remaining_amount % 25

#find the number of dimes in the remaining amount
number_of_dimes = remaining_amount // 10
remaining_amount = remaining_amount % 10

#find the number of nickels in the remaining amount
number_of_nickels = remaining_amount // 5
remaining_amount = remaining_amount % 5

#find the number of pennies in the remaining amount
number_of_pennies = remaining_amount

#displaying result
print(f"Your Amount {amount} Consists of:\n")

if number_of_one_dollars != 0:
    if number_of_one_dollars > 1:
        print(f"\t {number_of_one_dollars} Dollars\n")
    else:
        print(f"\t {number_of_one_dollars} Dollar\n")
if number_of_quaters != 0:
    if number_of_quaters > 1:
        print(f"\t {number_of_quaters} Quaters\n")
    else:
        print(f"\t {number_of_quaters} Quater\n")
if number_of_dimes != 0:
    if number_of_dimes > 1:
        print(f"\t {number_of_dimes} Dimes\n")
    else:
        print(f"\t {number_of_dimes} Dime\n")
if number_of_nickels != 0:
    if number_of_nickels > 1:
        print(f"\t {number_of_nickels} Nickels\n")
    else:
        print(f"\t {number_of_nickels} Nickel\n")
if number_of_pennies != 0:
    if number_of_pennies > 1:
        print(f"\t {number_of_pennies} Pennies\n")
    else:
        print(f"\t {number_of_pennies} Penny\n")