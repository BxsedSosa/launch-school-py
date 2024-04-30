"""
Q7. Write a function that takes two strings as arguments, determines the length of the two strings, and then returns the result of concatenating the shorter string, the longer string, and the shorter once again. You may assume that the sting are of different lengths
"""


def short_long_short(string1, string2):

    if len(string1) > len(string2):
        return string2 + string1 + string2
    else:
        return string1 + string2 + string1


print(short_long_short("abc", "defgh") == "abcdefghabc")
print(short_long_short("abcde", "fgh") == "fghabcdefgh")
print(short_long_short("", "xyz") == "xyz")


"""
In my example I defined the `short_long_short` function with 2 parameters of `string1` and `string2`

I have a if statment to check wheather the length of string1 is greater than string2. And if so then string2 will sandwich string 1 

and the else statement will just be the opposite of the if statement
"""
