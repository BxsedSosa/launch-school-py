'''
7. Write python code to replace all the : characters in the string below with +
'''

info1 = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
print('+'.join(info1.split(':')))

print('---------------------')

info2 = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
print(info2.replace(':', '+'))
'''
We will have to slip the string by the semi colon which will turn it into a list

Then will have to join them together by + character

after print the string
'''
