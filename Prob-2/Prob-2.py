# Module 3
#   Programming Assignment 4
#     Prob-2.py

# Frank Dvorak

'''
Your IPO comment goes here
'''
import math
def main():
    empName = input("Input Full Name: ")
    empWage = eval(input("Input your your hourly wage in numarical input only: "))
    empHours = eval(input("Input total hours worked: "))
    if empHours <= 40:
        regularWages = empWage * empHours 
        overtimeWages = 0
    
    else:
        regularWages = empWage * 40
        overtimeWages = (empHours - 40) * 1.5 * empWage 
    totalWages = regularWages + overtimeWages
    tax = totalWages * 0.2 
    insurance = totalWages * 0.1
    net = totalWages - tax - insurance
    print("Total Wages.....",totalWages)
    print("Net.............",net)

main()