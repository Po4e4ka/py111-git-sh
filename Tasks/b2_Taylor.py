"""
Taylor series
"""
from typing import Union
import Tasks.c1_fact as fa

def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    result = 1
    for i in range(1,100):
        result += (x**i)/(fa.factorial_iterative(i))
    return result

def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    result = x
    a = -1
    for i in range(3,10,2):
        print(i)
        s = (x**i)/(fa.factorial_iterative(i))
        result += s*a
        print(result)
        a = -a
    return result