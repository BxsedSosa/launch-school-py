"""
Q10. In Python, every object has a unique identifier that can be accessed using the id() function. This function returns the identity of an object, which is guaranteed to be unique for the object's lifetime. For certain basic immutable data types like short strings or integers, Python might reuse the memory address for objects with the same value. This is known as "interning".

Given the following code, predict the output:
"""

a = 42
b = 42
c = a


print(id(a) == id(b) == id(c))

"""
This code will print out 'True'

since in python the value of 42 has a memory location and all the variables point to that location
"""
