"""
8. Write code that capitalizes the words in the string 'launch school tech & talk', so that you get the string 'launch School Tech & Talk'.
"""

string = "launch school tech & talk"


def cap_each_word(string):
    strings = string.split()
    temp_list = []
    for i in strings:
        i = i.capitalize()
        temp_list.append(i)
    return " ".join(temp_list)


print(cap_each_word(string))
