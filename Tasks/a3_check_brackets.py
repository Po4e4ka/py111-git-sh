import Tasks.a0_my_stack as my_stack
def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    my_stack.clear()
    for i in brackets_row:
        if i == '(':
            my_stack.push('')
        elif i == ')':
            if my_stack.pop() is None:
                return False
    if len(my_stack.my_litle_stack) > 0:
        return False
    return True



