"""
Q1. Will the following functions return the same results?
"""


def first():
    return {
        "prop1": "hi there",
    }


def second():
    return
    {
        "prop1": "hi there",
    }


print(first())
print(second())

"""
The first function will print out 'prop1: 'hi there''

the second function wont print anything out since nothing is on the return line 
"""
