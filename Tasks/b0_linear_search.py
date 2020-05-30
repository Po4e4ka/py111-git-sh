"""
This module implements some functions based on linear search algo
"""
from typing import Sequence
import random

def linar_search(arr, elem):
    for i in range(len(arr)):
        if arr[i] == elem:
            print(f'элемент найден. индекс {i}')
            return elem
    print("элемент не найден")
    return None




def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min = 0
    for i in range(len(arr)):
        if arr[i] < arr[min]:
            min = i
    print(f"Минимальный элемент массива {arr} \nравен {arr[min]}")
    return min
