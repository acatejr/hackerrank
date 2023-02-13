"""
https://www.delftstack.com/howto/python/data-in-table-format-python/
"""

def breakingRecords(scores):
    """
    >>> breakingRecords([12,24,20,24])
    [3,2]
    """

    min_score = scores[0]
    max_score = scores[0]
    max_delta_cnt = 0
    min_delta_cnt = 0

    for s in scores[1:]:
        if s < min_score:
            min_score = s
            min_delta_cnt += 1
        elif s > max_score:
            max_score = s
            max_delta_cnt += 1


    results = [max_delta_cnt, min_delta_cnt]

    return results


if __name__ == "__main__":
    print(breakingRecords([12, 24, 10, 24]))
    print(breakingRecords([3,4,21,36,10,28,35,5,24,42]))
    print(breakingRecords([10,5,20,20,4,5,2,25,1]))
    # import doctest
    # doctest.testmod(verbose=True)


"""
>>> breakingRecords([3,4,21,36,10,28,35,5,24,42])
[4, 0]
>>> breakingRecords([10,5,20,20,4,5,2,25,1])
[2, 4]
"""