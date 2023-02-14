def divisbleSumPairs(n, k, ar):
    count = 0
    for i, x in enumerate(ar):
        for y in ar[i+1:]:
            if ((x+y) % k) == 0:
                # print(x, y, x+y, ((x+y) % k) == 0)
                count += 1

    return (count)

print(divisbleSumPairs(6, 3, [1,3,2,6,1,2]))
print(divisbleSumPairs(6, 5, [1,2,3,4,5,6]))