"""
6. Lets try another variabtion on the even/odd-numbers theme

We'll return to the simpler one-dimensional version of my_list. In this problem, you should wirte code that creates a new list with one elemnt for each numebr in my_list. If the original number is an even, then the corresponding elemnt in the new list should contain the string 'even'; otherwise; the element should contain 'add' 
"""

my_list = [1, 3, 6, 11, 4, 2, 4, 9, 17, 16, 0]

for_list = []

for num in my_list:
    if num % 2 == 0:
        for_list.append("even")
    else:
        for_list.append("odd")

print(for_list)
