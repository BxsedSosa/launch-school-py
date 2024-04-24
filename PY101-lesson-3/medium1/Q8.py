"""
Q8. Functinos and methods calls can take expressions as arguments. suppose we define a function named rps as follow, which follows the classic rules of the rps game, but with a slight twist: in the event of a tie, it just returns the choice made by both players
"""


def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"


print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))


"""
I believe the output will be 'paper'
"""
