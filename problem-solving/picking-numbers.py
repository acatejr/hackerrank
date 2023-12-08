def picking_numbers(a):
    multiset = []

    for i, v in enumerate(a):
        if i+1 < len(a):
            diff = abs(v - a[i+1])
            if diff <= 1:
                multiset.append(v)
                multiset.append(a[i+1])
                multiset += picking_numbers(a[i+1:])

    return multiset

a = [4,6,5,3,3,1]
print(picking_numbers(a))