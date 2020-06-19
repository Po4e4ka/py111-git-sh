"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple

my_little_tree = None

def reg_insert(local_tree, key, value):
    if local_tree is None:
        return {'key': key,
                'value': value,
                'l': None,
                'r': None}
    elif key < local_tree['key']:
        local_tree['l'] = reg_insert(local_tree['l'], key, value)
    elif key > local_tree['key']:
        local_tree['r'] = reg_insert(local_tree['r'], key, value)
    return local_tree


def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    global my_little_tree
    my_little_tree = reg_insert(my_little_tree,key,value)

def reg_remove(local_tree, key):
    pass
    # Не смотреть, пока ещё работаю:)
    # if local_tree is None:
    #     print('Нет такого ключа')
    #     return None
    # elif local_tree['key'] == key:
    #     if local_tree['l'] is None and local_tree['r'] is None:
    #         return local_tree
    # elif key > local_tree['key']:
    #     return reg_remove(local_tree['r'], key)
    # elif local_tree['key'] > key:
    #     return reg_remove(local_tree['l'], key)
    # return local_tree

def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """


def reg_find(local_tree, key):
    if local_tree is None:
        print('Нет такого ключа')
        return None
    elif local_tree['key'] == key:
        return local_tree['value']
    elif key > local_tree['key']:
        return reg_find(local_tree['r'], key)
    elif local_tree['key'] > key:
        return reg_find(local_tree['l'], key)

def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """

    return reg_find(my_little_tree, key)


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    return None


if __name__ == '__main__':

    insert(5, 'sdfga')
    insert(3, 'sga')
    insert(4, 'dfa')
    insert(7, 'sfa')
    insert(12, 'sa')
    insert(9, 'a')
    print(my_little_tree)
    print(find())