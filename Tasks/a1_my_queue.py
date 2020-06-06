"""
My little Queue
"""
from typing import Any

my_litle_queue = []

def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global my_litle_queue
    my_litle_queue.append(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    global my_litle_queue
    if len(my_litle_queue) > 0:
        temp = my_litle_queue[0]
        del my_litle_queue[0]
        return temp
    else:
        return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    print(ind)
    global my_litle_queue
    if ind > len(my_litle_queue):
        return None
    else:
        return my_litle_queue[ind]

def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global my_litle_queue
    for _ in range(len(my_litle_queue)):
        del my_litle_queue[0]
    return None
