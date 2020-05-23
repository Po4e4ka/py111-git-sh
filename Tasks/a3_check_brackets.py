import re
def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    count_0, count_1 = 0, 0
    for i in brackets_row:
        if i == "(":
            count_0 += 1
        if i == ")":
            count_1 += 1
            if count_0 < count_1:
                return False
    if count_1 == count_0:
        return True
    else:
        return False
