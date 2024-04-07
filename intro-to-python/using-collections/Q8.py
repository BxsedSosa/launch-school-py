'''
8. Explain why the code below prints different values on line 3 and 4
'''

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))  # 8
print(text.rfind('f', 21, 34)) # 29

'''
The code gives two different returns values for the rfind because the indexing is relative to the given string before the method. By splicing the text before hand the indexing is relative to that size of the string. Compared to not splicing before hand and doing the splice in the method arugment it has the full length of the strings length
'''
