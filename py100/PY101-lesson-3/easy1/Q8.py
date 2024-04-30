"""
Q8. In the previous problem, our first answer added 'Dino' to the list

How can we add multiple items to our list? Replace the call to append with another method invocation 
"""

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

new_list = ["Dino", "Happy"]

flintstones.extend(new_list)

print(flintstones)
