'''
10. assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statements reassign the variable? Which statements mutate the value of the object that obj references? Which statements do neither? If necessary, you can read the documentation.

obj = 'ABcd'
obj.upper()
obj = obj.lower()
print(len(obj))
obj = list(obj)
obj.pop()
obj[2] = 'X'
obj.sort()
set(obj)
obj = tuple(obj)
'''

'''
reassigned
neither
reassigned
neither
reassigned
mutate
reassigned and mutated
mutate
neither
mutate
'''

'''
Answers:

obj = 'ABcd'      # Reassignment
obj.upper()       # Neither
obj = obj.lower() # Reassignment
print(len(obj))   # Neither
obj = list(obj)   # Reassignment
obj.pop()         # Mutation
obj[2] = 'X'      # Mutation
obj.sort()        # Mutation
set(obj)          # Neither
obj = tuple(obj)  # Reassignment
'''