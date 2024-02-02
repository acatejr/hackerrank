def beautiful_days(i, j, k):
    days = 0
    if 1 <= i and i <= j and j <= (2 * 10**6):
        if 1 <= k and k <= (2 * 10**9):
            for i in range(i, j+1):
                i_rev = int(str(i)[::-1])
                diff = abs(i - i_rev)
                remainder = diff % k
                if remainder == 0:
                    days += 1
    return days

print(beautiful_days(20, 23, 6))
print(beautiful_days(13, 45, 3))