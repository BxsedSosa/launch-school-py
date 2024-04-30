"""
7. Use Pythons string methods on the string 'Captain Ruby' to create a string with the value 'Captain Python'
"""

string = "Captain Ruby"

string_list = string.split()
string_list[1] = "Python"

print(" ".join(string_list))
