"""
My little Stack
"""
from typing import Any

my_litle_stack = []

def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    global my_litle_stack
    my_litle_stack.append(elem)
    print(f"Добавлен элемент {elem}")
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    global my_litle_stack
    if my_litle_stack != []:
        result = my_litle_stack[-1]
        del my_litle_stack[-1]
    else:
        return None
    return result


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    print(ind)
    global my_litle_stack
    if ind > len(my_litle_stack):
        return None
    else:
        return my_litle_stack[-ind-1]


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    global my_litle_stack
    my_litle_stack = []
    return None



