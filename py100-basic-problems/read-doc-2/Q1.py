"""
1. Python offers multiple ways to format strings. The `str.format` method is a popular method, but since python 3.6, a new way called f-stings (formatted string literals) was introduced. F-strings offer a conscise way to embed expressions inside string literals

Given the follwing variables:
"""

name = "Victor"
profession = "programmer"

"""
1. How can you print the string 'Hello, Victor. you are a programmer' using the str.fomat method
"""

print(
    "Hello, {name}. You are a {profession}".format(
        name="Victor", profession="programmer"
    )
)

"""
2. How can you achieve the same result using a f-string?
"""

print(f"Hello, {name}. You are a {profession}")
