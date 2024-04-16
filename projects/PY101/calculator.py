# Ask the user for the 1st number
# Ask the user for the 2nd number
# Ask the user for an operation to perform
# Perform the operation on the two numbers
# Print the result to the terminal

print("Welcome to Calculator!")

print("What's the first number?")
number1 = int(input())

print("What's the second number?")
number2 = int(input())

print(
    "What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide"
)
operation = input()

output = 0
match operation:
    case "1":
        output = number1 + number2
    case "2":
        output = number1 - number2
    case "3":
        output = number1 * number2
    case "4":
        output = number1 // number2
    case _:
        print("You didn't provide a number 1-4")

print(f"The result is: {output}")
