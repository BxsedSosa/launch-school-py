"""
Q5. What do you think the following code will output?

Bonus: How can you reliably test if the value is nan
"""

from math import isnan

nan_value = float("nan")

print(nan_value == float("nan"))

print(isnan(nan_value))

"""
I believe that the output of the print will be False since nan might unique from one another
"""
