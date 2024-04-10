"""
2. Without running this code, what will it print? why?
"""

set1 = {42, "Monty Python", ("a", "b", "c")}
set2 = set1
set1.add(range(5, 10))
print(set2)

"""
The program will print out {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)} 
"""
