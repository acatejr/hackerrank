def kangaro(x1, v1, x2, v2):

    k1 = x1 + v1
    k2 = x2 + v2

    if k1 == k2:
        return "YES"
    else:
        return "NO"

print(kangaro(2, 1, 1, 2))
print(kangaro(0, 3, 4, 2))
print(kangaro(0, 2, 5, 3))