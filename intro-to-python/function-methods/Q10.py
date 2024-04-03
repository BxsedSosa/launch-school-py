'''
10. Without running the following code, what do you think it will do?
'''

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

'''
In this function it will print out:

42
3.141592
2

since there was a default parameter in place it is optional for there to be 2 or 3 arguments
'''