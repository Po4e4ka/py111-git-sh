"""
My little Stack
"""
from typing import Any

my_litle_stack: list

def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    my_litle_stack.append(elem)
    print(f"Добавлен элемент {elem}")


    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """

    return my_litle_stack.pop()


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    print(ind)
    return my_litle_stack[-ind-1]


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    my_litle_stack.clear()
    return None
