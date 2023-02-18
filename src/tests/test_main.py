"""Test main module"""

from example import main


def test_main():
    """
    Test the print function

    Returns:

    """

    assert main.print_hi("test_name") == "Hi, test_name"
