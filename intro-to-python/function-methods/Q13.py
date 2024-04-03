'''
13. Without running the following code, what do you think it will do?
'''

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

'''
This code will give an error due to the third parameter not having a default parameter in place. Whenever useing a default parameter in the middle of the positional parameters all of the parameters to the right have to have a default parameter as well.
'''