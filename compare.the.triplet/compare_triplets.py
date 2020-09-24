def compareTriplets(a, b):
    result = []
    item_count = len(a)
    item_index = 0
    a_points = 0
    b_points = 0

    while item_index < item_count:
        if a[item_index] > b[item_index]:
            a_points += 1
        elif b[item_index] > a[item_index]:
            b_points += 1

        item_index += 1

    result = [a_points, b_points]

    return result

a = [5,6,7]
b = [3,6,10]
print(compareTriplets(a,b))

a = [17, 28, 30]
b = [99, 16, 8]
print(compareTriplets(a,b))