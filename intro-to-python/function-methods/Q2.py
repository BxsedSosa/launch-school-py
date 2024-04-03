'''
Take a look at this code snipppet

What does the program print? Why?
'''

foo = 'bar'

def set_foo():
    foo = 'qux'
    
set_foo()
print(foo)

'''
In this program the program will print out 'bar' because the global scope foo is accessiable to the print function while the one in the function is blocked off by the functions scope. The variable foo inside of the function is variable shadowing it has the same indetifier but isn't the same in memory
'''