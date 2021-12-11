'''
*4.11 (Find the number of days in a month) Write a program that prompts the user to
enter the month and year and displays the number of days in the month. 
For example, if the user entered month 2 and year 2000, 
the program should display that February 2000 has 29 days. 
If the user entered month 3 and year 2005, the program should display that March 2005 has 31 days.
'''
month, year = eval(input("Enter Month and Year:"))

if month == 2:
    if (year % 4 == 0 and year % 100 != 0):
        print(f"February {year} has 29 days.")
    else:
        print(f"February {year} has 28 days.")
elif month == 1:
    print(f"January {year} has 31 days.")
elif month == 3:
    print(f"March {year} has 31 days.")
elif month == 4:
    print(f"April {year} has 30 days.")
elif month == 5:
    print(f"May {year} has 31 days.")
elif month == 6:
    print(f"June {year} has 30 days.")
elif month == 7:
    print(f"July {year} has 31 days.")
elif month == 8:
    print(f"August {year} has 31 days.")
elif month == 9:
    print(f"September {year} has 30 days.")
elif month == 10:
    print(f"October {year} has 31 days.")
elif month == 11:
    print(f"November {year} has 30 days.")
elif month == 12:
    print(f"December {year} has 31 days.")
