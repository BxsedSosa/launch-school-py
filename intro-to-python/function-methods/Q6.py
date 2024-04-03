'''
6. What does the following code print?
'''

def scream(words):
    words = words + '!!!!'
    return
    print(words)
    
scream('Yipeee')

'''
Just like the last questions the program will not print out anything. This is due to the return statement that happens befire the print function. Whenever a return statement happens in a function it ends the function block immediately
'''