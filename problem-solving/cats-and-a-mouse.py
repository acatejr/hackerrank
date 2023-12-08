def cat_and_mouse(x, y, z):
    cat_a_dist = abs(x - z)
    cat_b_dist = abs(y - z)

    if cat_a_dist < cat_b_dist:
        return "Cat A"
    elif cat_b_dist < cat_a_dist:
        return "Cat B"
    if cat_a_dist == cat_b_dist:
        return "Mouse C"

x, y, z = 2, 5, 4
print(cat_and_mouse(x, y, z))

x, y, z = 1, 2, 3
print(cat_and_mouse(x, y, z))

x, y, z = 1, 3, 2
print(cat_and_mouse(x, y, z))