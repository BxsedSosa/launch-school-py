"""
7. What will the following code do?
"""

a = 1


def my_func():
    global a
    a = 2


my_func()
print(a)


"""
This code will print 2
"""
