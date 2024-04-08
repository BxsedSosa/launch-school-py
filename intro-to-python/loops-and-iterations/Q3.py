'''
3. Use a while loop to print the numbers in my_list, one number per line. Then, do the same with a for loop
'''

my_list = [6, 3, 0, 11, 20, 4, 17]
count = 0

print('While loop \n -----------------------------')
while count < len(my_list):
    print(my_list[count])
    count += 1

print()
print('For loop \n -----------------------------')
for i in my_list:
    print(i)
