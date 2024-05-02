"""
Q5. Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.
"""

operations = ["+", "-", "*", "/", "//", "%", "**"]

number1 = int(input("==> Enter the first number:"))
number2 = int(input("==> Enter the second number:"))

for operation in operations:
    results = eval(f"{number1}{operation}{number2}")
    print(f"{number1} {operation} {number2} = {results}")

"""
This example I created a list of each operation. Then 2 variables that will take a integer as an input. After a for loop which will iterate over each operation in the list and use the eval() function which evaluates the string as if it was a math arithmetic making the code short and sweet
"""
