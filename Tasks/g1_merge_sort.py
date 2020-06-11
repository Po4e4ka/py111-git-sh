from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    print(container)
    x = len(container)
    if x == 1:
        return container
    else:
        a = sort(container[:round(x//2)])  # Рекурсивное деление левой части
        b = sort(container[round(x//2):])  # Рекурсивное деление правой части
        a_len = len(a)
        b_len = len(b)
        result = []
        while a_len > 0 and b_len > 0:  # Пока не прошлись по всем элементам правой или левой части
            if a[-a_len] < b[-b_len]:   # Если слева меньше, то в результат заносим левый
                result += [a[-a_len]]
                a_len -= 1
            else:                       # Если справа меньше, то в результат заносим правый
                result += [b[-b_len]]
                b_len -= 1
        if a_len == 0:                  # Добавление оставшейся части массива, который не кончился, в результат
            result += b[-b_len:]
        elif b_len == 0:
            result += a[-a_len:]
        return result
