def aVeryBigSum(ar):
    total = 0
    for v in ar:
        total += v        

    return total


ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
print(aVeryBigSum(ar))

ar = [1,2,3,4,5]
print(aVeryBigSum(ar))