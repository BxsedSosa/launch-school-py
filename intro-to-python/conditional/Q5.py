'''
5. What does this code output, and why?
'''

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

'''
This code would print out 'Empty', Since a empty collection is considered falsy so it goes to the else statement.
'''