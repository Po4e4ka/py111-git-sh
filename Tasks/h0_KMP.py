from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """
    result = []

    a = len(prefix_str)
    for i in range(a):
        pref = prefix_str[:i+1]
        suff = pref[1:]
        leng = len(suff)
        for j in range(leng,0,-1):
            if pref[:j] == suff[leng-j:]:
                result.append(j)
                break
        else:
            result.append(0)


    return result


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """
    j = 0
    start = -1
    for i in range(len(inp_string)):
        if substr[j] == inp_string[i]:
            if start == -1:
                start = i
            if j == len(substr)-1:
                return start
            j += 1
        elif j <= 0:
            start = -1
            continue
        elif j > 0:
            start = -1
            j = _prefix_fun(inp_string)[j-1]