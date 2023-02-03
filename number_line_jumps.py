def kangaro(x1, v1, x2, v2):

    if (x1 == x2):
        return "YES"

    if (v2 - v1) == 0:
        return "NO"

    j = (x1 - x2) / (v2 - v1)

    if j >= 0 and j.is_integer():
        return "YES"
    else:
        return "NO"


# print(kangaro(2, 1, 1, 2))
# print(kangaro(0, 3, 4, 2))
# print(kangaro(0, 2, 5, 3))
# print(kangaro(21, 6, 47, 3)) # Expect NO
print(kangaro(43, 2, 70, 2)) # Expect NO