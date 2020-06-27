from typing import List
import random

def sort(container: List[int]) -> List[int]:
    """
        Sort input container with quick sort

        :param container: container of elements to be sorted
        :return: container sorted in ascending order
        """
    leng = len(container)
    if leng <= 1 :
        return container
    op_elem = random.choice(container)
    left_mass, right_mass, middle = [],[],[]
    for i in container:
        if i < op_elem:
            left_mass.append(i)
        elif i > op_elem:
            right_mass.append(i)
        else:
            middle.append(i)
    return sort(left_mass) + middle + sort(right_mass)