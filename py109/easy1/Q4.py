"""
Q4. Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's' area in both square meters and square feet
"""


def square_ft(square_meters):
    return round(float(square_meters * 10.7639), 2)


def square_meters():
    length = int(input("What is the length of the room?:\n"))
    width = int(input("What is the width of the room?:\n"))

    square_meters = length * width
    square_feet = square_ft(square_meters)

    print(f"Square meters: {square_meters}\nSquare feet: {square_feet}")
    pass


square_meters()

"""
In this example we are asking the user for 2 inputs `length` and `width` asking for integers to find what the size of a room is in square meters. Once we get the 2 inputs we then multiple them together to retrieve square meters. 

Then I created a function called square_ft with 1 parameter that multiples `square_meters` to `10.7639` and using the round function so that we return a value will a max of 2 decimal points

so the variables after the line with `square_ft` function
    - `square_meters` would equal the current square meters
    - `square_feet` will equal the current square feet

Then on the last line we print both of them
"""
