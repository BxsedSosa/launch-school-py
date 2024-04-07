'''
12. Write some code that determines and prints whether the number 3 ppears inside each of these  list:
'''

num1 = [1, 3, 5, 7, 9, 11]
num2 = []
num3 = [2, 4, 6, 8]
num4 = ['1',  '3', '5']
num5 = ['1', 3.0, '5']

num_list = [num1, num2, num3, num4, num5]

for num in num_list:
    print(3 in num)
