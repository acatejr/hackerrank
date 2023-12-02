import sys
import math

def pageCount(n, p):
    """
    n = how many pages long the book is
    p = destination page
    """

    if p % 2 == 0:
        s = 1 + (p - 2) // 2
        e = (n - p) // 2
    if p % 2 == 1:
        s = (p - 1) // 2
        e = (n + 1 - p) // 2

    return min(s, e)


if __name__ == "__main__":

    n = 5
    p = 3
    result = pageCount(n,p)
    print(f"result: {result}")

    n = 6
    p = 2
    result = pageCount(n,p)
    print(f"result: {result}")

    n = 8
    p = 5
    result = pageCount(n,p)
    print(f"result: {result}")

    n = 5
    p = 4
    result = pageCount(n,p)
    print(f"result: {result}")

    n = 7
    p = 5
    result = pageCount(n,p)
    print(f"result: {result}")