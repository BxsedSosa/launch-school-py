"""
5. print all of the even numbers in the following list of nested list. Don't use any while loops
"""

my_lists = [[1, 3, 6, 11], [4, 2, 4], [9, 17, 16, 0]]

print("List Composition \n-----------")
even_comp = [num for list in my_lists for num in list if num % 2 == 0]

print(even_comp, "\n")

print("For Loop \n------------")
for list in my_lists:
    for num in list:
        if num % 2 == 0:
            print(num)
