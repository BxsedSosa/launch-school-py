'''
2. Modify the age.py program you wrote in Exercise 3 of 'input/output chapter'. The updated code should use a for loop to display the future ages
'''

age = int(input('What is your age? \n'))
print(f'You are {age} years old.')
print()

for i in range(1,5):
    year = i * 10
    new_age = age + year
    print(f'In {year} years, you will be {new_age} years old.') 
