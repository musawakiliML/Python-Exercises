'''
*4.9 (Financial: compare costs) Suppose you shop for rice and find it in two different sized packages. You would like to write a program to compare the costs of the
packages. The program prompts the user to enter the weight and price of each
package and then displays the one with the better price.
'''
weight_1, price_1 = eval(input("Enter Weight and Price for Package1:"))
weight_2, price_2 = eval(input("Enter Weight and Price for Package2:"))

price_per_kilo_1 = price_1 / weight_1
price_per_kilo_2 = price_2 / weight_2
if price_per_kilo_1 > price_per_kilo_2:
    print("Package 1 has the better price.")
elif price_per_kilo_2 > price_per_kilo_1:
    print("Package 2 has the better price.")
else:
    price("Both Have Good Price.")