"""
2. In the following code snippet, find all violations of the PEP8 STyle guide. Rewrite it so that it conforms with the guide

iceCreamDensity=10

while iceCreamDensity>0 :
    print('Drip...')
    iceCreamDensity-=1

print('The ice cream melted.')
"""

"""
In the first line they are using CamelCase as well as not spacning out the equal sign with the integer on the right

in the while loop they dont space out the comparison operator but the semi colon got spaced out that shouln't be

on line 5 iceCreamDensity is not spaced out from the short substraction expression
"""

ice_cream_density = 10

while ice_cream_density > 0:
    print("Drip...")
    ice_cream_density -= 1

print("The ice cream melted")
