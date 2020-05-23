"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any


my_priority_queue = []


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global  my_priority_queue
    my_priority_queue.append({"priority": priority, "elem": elem})
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    temp = 0
    global my_priority_queue
    if len(my_priority_queue) < 1:
        return None
    result = my_priority_queue[0]
    for i in range(1,len(my_priority_queue)):
        if result["priority"] > my_priority_queue[i]["priority"]:
            result = my_priority_queue[i]
            temp = i
    del my_priority_queue[temp]
    return result["elem"]


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global my_priority_queue
    if ind > len(my_priority_queue):
        return None
    else:
        return my_priority_queue[ind]["elem"]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global my_priority_queue
    my_priority_queue = []
    return None

if __name__ == "__main__":
    for i in range(10,20):
        enqueue(i, 2)
    for i in range(10):
        enqueue(i, 0)
    print(dequeue())