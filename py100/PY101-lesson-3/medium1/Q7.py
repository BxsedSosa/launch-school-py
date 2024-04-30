"""
Q7. One day, Spot was playing with the munster family's home computer, and he wrote a small program to mess with their demographic data
"""

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}


def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"


mess_with_demographics(munsters)

print(munsters)
"""
Before grandpa could stop him, Spot hit the enter key with his tail. Did the family's data get ransacked?

Why or why not?
"""

"""
This data will be mutated since the data given is mutable
"""
