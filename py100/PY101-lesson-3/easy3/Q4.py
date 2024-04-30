"""
Q4. What will the following code output?
"""

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]["first"] = 42
print(my_list1)

"""
This code will change the key/value pair's value to 42
"""
