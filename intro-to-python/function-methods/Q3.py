'''
3. Write a program that uses a multiply function to multiply two numbers and returns the result. Ask the user to enter the two numbers, then output theh numbers and result as a simple equation.
'''

first_num = float(input('Enter the first number: \n'))
second_num = float(input('Enter the second numer: \n'))
total = float(first_num * second_num)

print(f'{first_num} * {second_num} = {total}')