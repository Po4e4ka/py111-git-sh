from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    result = [stairway[0], stairway[1]]
    i = 0
    for i in range(2,len(stairway)):
        result.append(stairway[i]+min(result[i-1],result[i-2]))
    return result[-1]
