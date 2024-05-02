"""
Q7. The `or` operator returns a truthy value if either or both of its operands are truthy, a falsy value if both operands are falsy. The `and` operator returns a struthy value if both of its poerands are truthy, and a falsy value if either operand is faly. This works great until you need only one of two conditions to be truthy, the so-called exclusive or, known as xor
"""


def xor(operand1, operand2):

    return False if bool(operand1) and bool(operand2) else True


print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
