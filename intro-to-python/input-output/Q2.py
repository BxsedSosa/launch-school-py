'''
Modify the last question to ask for the user's first and last names separately, then greet the user with their full name
'''

first_name = str(input('What is your first name?: \n'))
last_name = str(input('What is your last name?: \n'))

print(f'Hello, {first_name} {last_name}!')