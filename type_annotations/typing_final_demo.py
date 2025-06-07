from typing import Final,Union

VERSION:Final['str'] = '1.0.12'
# VERSION = '1.0.11'

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Adds two numbers together.

    :param x: The first number to add.
    :param y: The second number to add.
    :return: The sum of x and y.
    """
    return x + y