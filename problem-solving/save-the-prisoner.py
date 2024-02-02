def save_the_prisoner(n, m, s):

    prisoner = 0

    if (1 <= n and n <= 10**9) and (1 <= m and m <= 10**9) and (1 <= s and s <= n):
        positions = list(range(1, m+1))
        seats = list(range(1, n+1))
        padd = list(range(1, n))
        print(seats, positions, seats[s-1:] + padd)

    return prisoner

# print(save_the_prisoner(4, 6, 2))
# print(save_the_prisoner(7, 19, 2))
print(save_the_prisoner(3, 7, 3))