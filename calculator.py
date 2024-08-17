# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 20:51:33 2024

@author: nidhi
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    print("Select any operation:")
    print("1. Type 1 for Addition")
    print("2. Type 2 for Subtraction")
    print("3. Type 3 for Multiplication")
    print("4. Type 4 for Division")
    
    choice = input("Enter any operation from 1 to 4: ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid Input")

# Run the calculator
calculator()
