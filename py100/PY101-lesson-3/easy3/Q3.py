"""
Q3. What will the following code output:
"""

str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)

"""
The code will print out:

"hello there"


str2 only changed its own value and not str1 since strings are immutable
"""
