"""
3. Using the following code, compare the value of name with the string 'RoGeR' while ignoring the case of both strings. Print true if the values are the same; print false if they aren't. Next, peform a case-insensitive comparison between the value of name and the string 'DAVE'
"""

name = "Roger"

if name.lower() == "RoGeR".lower():
    print("true")
else:
    print("false")

if name == "DAVE":
    print("true")
else:
    print("false")
