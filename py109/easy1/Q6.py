"""
6. Write a program that asks the user to enter an integer greater than 0, then ask whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive
"""


def sum(number):
    sum = 0
    for i in range(number + 1):
        sum += i

    return sum


def product(number):
    product = 1
    for i in range(1, number + 1):
        product *= i

    return product


def main():

    ask_user_number = int(input("Please enter a number greater than 0: "))

    while ask_user_number <= 0:
        ask_user_number = int(input("Please enter a number greater than 0: "))

    ask_user_operation = str(
        input("Enter 's' to compute the sum\nOR 'p' to compute the product\n")
    )

    while ask_user_operation not in ["s", "p"]:
        ask_user_operation = str(
            input(
                "Please only enter 's' to compute the sum\nOR 'p' to compute the product\n"
            )
        )

    if ask_user_operation == "s":
        print(sum(ask_user_number))
    elif ask_user_operation == "p":
        print(product(ask_user_number))


main()


"""
In this code I created 3 seperate functions 2 are helper functinos to do the math for getting the sum of all the number betwen 1 and the given number and did the same for the product as well. 

In the main loop i asked the user to enter a number greater than 0 didn't do a try eexecpt but created a loop if a int was recieved and it was 0 or below

and same for the input for asking the sum or product i created a while loop that checked if the users input was not in the list of 's' and 'p' 

Once the inputs were recieved then if statements branched off if we were going to do the sum or product of the number and the functions will return the results 
"""
