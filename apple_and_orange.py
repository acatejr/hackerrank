
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here

    apple_landings = [a + i for i in apples]
    orange_landings = [b + i for i in oranges]

    apple_count = 0
    orange_count = 0
    for a in apple_landings:
        if a >= s and a <= t:
            apple_count += 1

    for o in orange_landings:
        if o >= s and o <= t:
            orange_count += 1

    print(apple_count)
    print(orange_count)
