"""
9. Determine what the following code snippet prints. First solve it in your head or on paper, then run it in your Python environment to check the result
"""

speed = 0
accleration = 24
break_force = 19
is_moving = break_force < accleration and (speed > 0 or accleration > 0)
print(is_moving)

"""
This script will print out True
"""

"""
Bonus:

Do we need paraentheses in the boolean expression or could we have written without them?

Yes you need parentheses because the 'and' operator has a higher precedece than the or operator
"""
