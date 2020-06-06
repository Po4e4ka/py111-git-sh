from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    print(arr)
    print(elem)
    ind = len(arr)//2

    result = ind
    print(arr[ind])
    if elem == arr[ind]:
        # Блок комбинации бинарного поиска и линейного с уходом влево
        if len(arr) != 1 and arr[len(arr[:ind])//2] == elem:  # Если следующий элемент бинарного поиска такой же
            return binary_search(elem, arr[:ind])
        else:  # Если следующий бинарный элемент отличается, то включаем линейный
            while len(arr) > 1 and arr[ind] == arr[ind - 1]:
                ind -= 1
            return ind
        # -------------------------------------------------------------
    elif ind == 0:
        return None
    elif elem > arr[ind]:
        a = binary_search(elem, arr[ind:])
        if a is not None:
            result += a
        else:
            result = None
        return result
    elif elem < arr[ind]:
        return binary_search(elem, arr[:ind])

