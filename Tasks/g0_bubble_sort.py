from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    a = len(container)
    for i in range(a-2):
        for j in range(1, a - i):
            if container[j] < container[j-1]:
                container[j], container[j-1] = container[j-1], container[j]

    return container
