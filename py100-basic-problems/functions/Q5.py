"""
5. Without running the following code, determine what it will print:
"""


def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f"{dividend} / {divisor} = 3")
        divisor += 1


multiples_of_three

"""
This code will raise an SytaxError because in the last line python thinks youre calling a undefined variable but just forgot to add the parentheses at the end 
"""
"""
Answer
------
<function multiples_of_three at 0x102656200>
"""
