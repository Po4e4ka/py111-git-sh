def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 1:
        raise ValueError('n < 0')
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n-1)+fib_recursive(n-2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 1:
        raise ValueError('n < 0')
    result = [1,1]
    for i in range(3,n+1):
        result[0], result[1] = result[1], result[0] + result[1]
    return result[1]

