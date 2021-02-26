'''
*3.9 (Financial application: payroll) Write a program that reads the following information and prints a payroll statement:

        Employee’s name (e.g., Smith)
        Number of hours worked in a week (e.g., 10)
        Hourly pay rate (e.g., 9.75)
        Federal tax withholding rate (e.g., 20%) 
        State tax withholding rate (e.g., 9%)
'''
# Get user input for payroll
employee_name = input("Enter employee's name:")
number_of_hours = eval(input("Enter number of hours worked in a week:"))
hourly_pay_rate = eval(input("Enter hourly pay rate:"))
federal_tax_withholding_rate = eval(input("Enter federal tax withholding rate:"))
state_tax_withholding_rate = eval(input("Enter state tax withholding rate:"))

# Calculating the payroll
gross_pay = number_of_hours * hourly_pay_rate
federal_tax_withholding = 0.2 * gross_pay
state_tax_withholding = state_tax_withholding_rate * gross_pay
total = federal_tax_withholding + state_tax_withholding
net = gross_pay - total

# Displaying Results
print(f"Employee Name:{employee_name}")
print(f"Hours Worked:{float(number_of_hours)}")
print(f"Pay Rate:${float(hourly_pay_rate)}")
print(f"Gross Pay:${float(gross_pay)}")
print(f"Deductions:")
print(f"\tFederal Withholding (20.0%):${federal_tax_withholding}")
print(f"\tState Withholding (9.0%):${state_tax_withholding}")
print(f"\tTotal Deducation:${total}")
print(f"Net Pay:${net}")