"""
Q3. Write a function that takes a short line of text and prints in within a box
"""


def banner(string):
    print(
        f"""
    +-{'-' * len(string)}-+
    | {' ' * len(string)} |
    | {string} |
    | {' ' * len(string)} |
    +-{'-' * len(string)}-+
    """
    )


banner("To boldly go where no one has gone before.")
