def jumping_on_clouds(c, k):
    """Another way to do this.
    Get indices of all clouds where land, get corresponding values.
    Process energy based on those values.  The one more energy process for value at c[0]
    """

    energy = 100
    n = len(c)
    jump = (0 + k) % n

    while jump != 0:
        v = c[jump]
        if v == 1:
            energy -= 3
        elif v == 0:
            energy -= 1
        jump = (jump + k) % n

    if c[0] == 1:
        energy -= 3
    else:
        energy -= 1

    return(energy)

c = [0, 0, 1, 0]
k = 2
print(jumping_on_clouds(c, k))

c = [0, 0, 1, 0, 0, 1, 1, 0]
k = 2
print(jumping_on_clouds(c, k))

c = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
k = 3
print(jumping_on_clouds(c, k))