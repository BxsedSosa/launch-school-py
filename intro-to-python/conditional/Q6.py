'''
6. Write a function that takes a string as an argument and returns an all-caps version of the string when the string is longer than 10 characters. Otherwise, it should return the original string. Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.
'''

def all_cap():
    string = str(input('Enter in a string: \n'))
    stringLen = len(string)
    
    if stringLen > 10:
        print(string.upper())
    else:
        print(string)

all_cap()