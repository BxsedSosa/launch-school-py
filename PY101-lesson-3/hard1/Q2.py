"""
Q2. What does the last line in the following code output?
"""

dictionary = {"first": [1]}
num_list = dictionary["first"]
num_list.append(2)

print(num_list)
print(dictionary)

"""
The last line will print output

{'first': [1, 2]} 
"""
