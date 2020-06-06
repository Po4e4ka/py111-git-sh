from typing import Hashable, List
import networkx as nx
import Tasks.a1_my_queue as queue


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    visible = [start_node]
    queue.enqueue(start_node)
    while True:
        versh = queue.dequeue()
        if versh is None:
            break
        list1 = g.neighbors(versh)
        for i in list1:
            if visible.count(i) == 0:
                visible.append(i)
                queue.enqueue(i)

    return visible
