from typing import Hashable, List
import networkx as nx
import Tasks.a0_my_stack as queue


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    visible = [start_node]
    queue.push(start_node)
    while True:
        versh = queue.pop()
        if versh is None:
            break
        list1 = g.neighbors(versh)
        for i in list1:
            if visible.count(i) == 0:
                visible.append(i)
                queue.push(i)

    return visible

