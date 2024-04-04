'''
4. Refactor this statement to usea regular if statement instead
'''

# return ('bar' if foo() else qux())

if foo():
    return 'bar'
else:
    return qux()