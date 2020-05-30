from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    indl = 0
    indr = len(arr)-1
    result = -1
    while indr-indl > 1:
        ind = int((indl + indr)/2)
        if arr[ind] == elem:
            result = ind
            break
        elif arr[ind] > elem:
            indr = ind
        else:
            indl = ind
    if arr[indr] == elem:
        result = indr
    if arr[indl] == elem:
        result = indl
    if result != -1:
        while arr[result-1] == arr[result]:
            result -= 1
    return None if result == -1 else result

