'''
15. Using the code below, classify the identifiers as global, local, or built in.
'''

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

'''
Global:
multiply = line 5, 13
get_num = line 8, 11, 12
first_number = line 11, 13, 14
second_number = line 12, 13 ,14
product = line 13, 14

Local:
left = line 5, 6
right = line 5, 6
prompt = line 8, 9


Built-in:
print = line 14
float = line 9
input = line 9
'''