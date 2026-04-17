def factorial(n):
    """
    :param n - the number to find the factoruial
    :return int -   the factoruial of n
    """

    # the base case
    if n==0:
        return 1
    return n*factorial(n-1)


print(factorial(5))

def fib(n):
    """
    :param n - the number to find the fibonacci
    :return list 
    """

    # if n==0:
    #     return 0
    # if n==1:
    #     return n
    if n in (0,1):
        return n
    return fib(n-1)+fib(n-2)

print(fib(7))
