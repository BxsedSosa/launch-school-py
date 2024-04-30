"""
Q5. Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The programm must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers
"""

bill = float(input("What is the bill?: "))
percent = float(input("What is the tip percentage?: ")) * 0.01

tip = round(bill * percent, 2)
total = round(bill + tip, 2)

print(f"The tip is ${tip}")
print(f"The total is ${total}")


"""
In this example we are collecting 2 inputs from the user. One will be for the `bill` amount and the second is the `tip percentage` and explicitly making it a float data type.

Since we recieved a whole number as the percent I am converting it to a decimal for later use to get the tip amount

After we use the round function to get only 2 decimal places over and multiple the `bill` amount to the `percent`

The line after is the variable total which also uses the round function to get 2 deciamls over and adds the `bill` amount and the `tip` amount to get the grand total of the bill
"""
