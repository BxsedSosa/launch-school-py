'''
2. Write a function, even_or_odd, that determines whether its argument is an even or odd number. If it's even, the function should print 'even'; otherwise it should print 'odd'. Assume the arguments is always an integer.
'''


def even_or_odd():
    num = int(input('Enter a number: \n'))
    result = num % 2
    
    if result == 0:
        print('Even')
    else:
        print('Odd')

even_or_odd()