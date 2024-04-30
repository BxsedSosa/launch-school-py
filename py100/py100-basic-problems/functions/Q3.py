"""
3. Let's generalize the function from the previous exercise. Implement a function names cite that takes two string arguemnts: the author of the quote and what they said. then prints the quote as shown below

# Bruce Eckel said: "Python is executable pseudocode"
"""


def cite(author, quote):
    print(f'{author} said: "{quote}"')


cite("Bruce Eckel", "Python is executable pseudocode")
