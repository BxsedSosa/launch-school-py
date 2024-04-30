"""
Q9. Consider these two simple functions:

What will the following function invocatino return
"""


def foo(param="no"):
    return "yes"


def bar(param="no"):
    return param == "no" and foo() or "no"


bar(foo())

"""
This program will print out:

'no'
"""
