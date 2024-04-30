"""
Q1. Let's do some "ASCII Art": a stone-age form of nerd artwork from back in the days before computers had video screens

For this practice prblem, write a program that outputs The Flinstones Rock! 10 times, with each line prefixed by one more hypehn than the line above it
"""

string = "The Flintstones Rock!"

for i in range(1, 11):
    print(("-" * i) + string)
