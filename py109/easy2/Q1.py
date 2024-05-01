'''
Q1. Create a function that takes 2 arguments, a list and a dict. The list will contain 2 or more elements that, when joined with spaces, will produce a person's name. The dict will contain two keys 'title' and 'occupation', and the appropriate values. Your function should return a greeting that uses the person's full name, and metntions the person's title.
'''

def greetings(lst, diction):
    return f'Hello, {' '.join(lst)}! Nice to have a {diction['title']} {diction['occupation']} around.'

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

'''
This code just demostrates the use of f-strings to make formatting variables within a string a lot easier than using comma seperations
'''
