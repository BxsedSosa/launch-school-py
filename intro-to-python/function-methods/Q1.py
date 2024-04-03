'''
1. What happens when you run the following program? Why do we get that result
'''

def set_foo():
    foo = 'bar'
    
set_foo()
print(foo)

'''
We will get a error due to the program not being able to see the foo variable inside of the set_foo function. This is because of variable scope.
'''