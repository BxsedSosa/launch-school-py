"""
9. The following code raises a TypeErorr

What does a TypeErorr indicate? Try running the code and fixing the issue
"""

tweet = "Woohoo! :-)"

if len(tweet) > 140:
    print("Tweet is too long!")

length_of_tweet = len(tweet) + 5

"""
The reason the code had a TypeErorr is because we are putting a int inside of the len function which is looking for a sequence to find the length of that object.

This is raised when a operation or function is applied to an object of inappropriate type
"""
