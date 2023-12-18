def picking_numbers(a):
    multiset = []
    a.sort()

    curr_vals = []
    for v in a:
        if len(curr_vals) == 0:
            curr_vals.append(v)
        else:
            diff = abs(v - curr_vals[0])
            if  diff <= 1:
                curr_vals.append(v)
            else:
                multiset.append(len(curr_vals))
                curr_vals = [v]

    multiset.append(len(curr_vals))
    return max(multiset)

a = [4,6,5,3,3,1]
print(picking_numbers(a))

a = [1, 2, 2, 3, 1, 2]
print(picking_numbers(a))

a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
print(picking_numbers(a))
