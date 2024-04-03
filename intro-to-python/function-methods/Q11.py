'''
11. Without running the following code, what do you think it will do?
'''

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

'''
In this program it will print out:

42
3
2

Since there are 2 default parameters in place you arent required to place in arguments for those positiions
'''