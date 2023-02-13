def birthday(s, d, m):
    """_summary_

    Args:
        s (_type_): Chocolate array
        d (_type_): Number to sum to
        m (_type_): Number of squares of chocolate

    Returns:
        _type_: _description_
    """
    num_days = 0

    if len(s) == 0:
        return 0

    print(s, d, m)
    for cnt, val in enumerate(s):
        squares_to_sum = s[cnt:cnt+m]
        if len(squares_to_sum) == m:
            total = sum(squares_to_sum)
            if total == d:
                print(cnt, val, num_days, squares_to_sum, total)
                num_days += 1

    return num_days


# print(birthday([1, 2, 1, 3, 2,], 3, 2))
# print(birthday([4], 4, 1))
print(birthday([1, 1, 1, 1, 1, 1,], 3, 2))