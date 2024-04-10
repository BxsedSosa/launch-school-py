"""
11. Print all of the even numbers in the following list of nested lists. This time, ton't use any for loops
"""

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

print("For Loop \n------------")
for list in my_list:
    for num in list:
        if num % 2 == 0:
            print(num)

print("\n While loop \n------------")
index_1 = 0
while index_1 < len(my_list):
    index_2 = 0
    while index_2 < len(my_list[index_1]):
        if my_list[index_1][index_2] % 2 == 0:
            print(my_list[index_1][index_2])
        index_2 += 1
    index_1 += 1
