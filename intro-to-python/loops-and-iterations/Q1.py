'''
1. The following code casues an infinite loop ( a loop that never stops iterating ) Why?
'''

counter = 0

while counter < 5:
    print(counter)

'''
This code would endlessly loop '0' to the console because it doesn't have a increment anywhere. Now that is the case the condition statment in the loop will always be True because counter will forever be less than 5

