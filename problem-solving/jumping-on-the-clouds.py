def jumping_on_clouds(c, k):
    results = None
    n = len(c)
    energy = 100
    cloud = c[0]
    for i, v in enumerate(c):
        print(i, v, cloud)
        jump = (i+k)%n
        cloud = c[jump]
        if v == 0:
            energy -= 1
        elif v == 1:
            energy -= 2

    print(energy)
    return results

c = [0, 0, 1, 0, 0, 1, 1, 0]
k = 2
jumping_on_clouds(c, k)