'''
15. Without running the following code, what values will be printed by line 10?
'''

pets = {
    'Cat':    'Meow',
    'Dog':    'Bark',
    'Bird':   'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

'''
It will print out

dict_keys (['Cat', 'Dog', 'Bird'])

Im assuming that sine the tuple is already created before the del and the new assignment happens it will only hold the keys of the original keys
'''

'''
Answer:

dict_keys (['Cat', 'Bird', 'Snake'])

I was wrong even though the key method has already happened and the del and new assignment happened after it still mutates the keys variable to adjust for the changes
'''
