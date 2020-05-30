def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """

    print(n)
    if n < 1:
        raise ValueError('n < 0')
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    result = 1
    for i in range(1,n):
        result *= (i+1)
    return result

if __name__ == "__main__":
    print(factorial_recursive(5))
    print(factorial_iterative(5))