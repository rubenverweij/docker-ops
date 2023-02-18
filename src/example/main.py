"""The main module"""


def print_hi(name: str):
    """
    Print the name

    Args:
        name: str

    Returns:
        Response "Hi, <name>"

    """
    if not isinstance(name, str):
        raise ValueError("The class is not defined well")
    return f"Hi, {name}"


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print_hi("PyCharm")
