'''
7. Write a function that takes a single integer argument and prints a message that describes whether:

    the value is between 0 and 50 (inclusive)
    the value is between 51 and 100 (inclusive)
    the value is greater than 100
    the value is less than 0

'''

def number_range():
    num = int(input('Enter in a number: \n'))
    
    if num < 0:
        print(f'{num} is less than 0')
    elif num <= 50:
        print(f'{num} is between 0 and 50')
    elif num <= 100:
        print(f'{num} is between 51 and 100')
    else:
        print(f'{num} is greater than 100')

number_range()