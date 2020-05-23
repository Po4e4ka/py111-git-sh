import Tasks.a0_my_stack as my_stack
def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    count_0, count_1 = 0, 0
    for i in brackets_row:  # Оргиназовать стек из строки
        my_stack.push(i)
    for i in range(len(my_stack.my_litle_stack)):
        a = my_stack.pop()
        if a == ')':
            count_1 += 1
        if a == '(':
            count_0 += 1
            if count_0 > count_1:
                return False
    print(count_1,count_0)
    if count_1 == count_0:
        return True
    else:
        return False

