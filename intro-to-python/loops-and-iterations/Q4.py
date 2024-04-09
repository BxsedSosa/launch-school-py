"""
4. Use a while loop to print all numbers in my_list with even values, one number per line. Then print, the odd numbers using a 'for' loop
"""

my_list = [6, 3, 0, 11, 20, 4, 17]
counter = 0

print("Even numbers: \n --------------------")
while counter < len(my_list):
    if my_list[counter] % 2 == 0:
        print(my_list[counter])

    counter += 1


print("Odd numbers: \n --------------------")
for i in my_list:
    if i % 2 == 1:
        print(i)
