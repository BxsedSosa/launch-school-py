"""
Q2. Write a program that ask for user's name, then greets the user. IF the user appends a `!` to their name, the computer will yell the greeting
"""

name = input("What is your name?: ")

if "!" in name:
    print(f"HELLO {name} WHY ARE WE YELLING?")
else:
    print(f"Hello {name}")

"""
This code just takes a string input from user and checks if theres a `!` in the string. If it does then it has a unique string for it
"""
