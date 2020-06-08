from typing import Hashable, List
import networkx as nx
import Tasks.a0_my_stack as stk

def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    visible = [start_node]
    for i in visible:
        list1 = list(g.neighbors(i))
        bol = 0  # Флаг проверки добавления в висибл
        for j in list1:
            if visible.count(j) == 0:
                if bol == 0:  # Если уже добавили элемент в визибл
                    bol = 1
                    visible.append(j)
                else:  # все остальные в стэк
                    stk.push(j)
        if len(list1) == 1:  # Если из соседей только предыдущий элемент
            x = stk.pop()    # то берем элемент из стэка
            if x is None:    # Если стэк пустой, то завершаем цикл - все элементы найдены
                break
            if visible.count(x) == 0:
                visible.append(x)
    return visible
