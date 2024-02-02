import math

def viral_advertising(n):

    cumulative_likes = 0

    if 1 <= n and n <= 50:

        shared = 5
        liked = math.floor(shared/2)
        for day in range(1, n+1):
            if day > 1:
                shared = math.floor(shared/2)*3
                liked = math.floor(shared/2)

            cumulative_likes += liked

    return cumulative_likes


print(f"Result: {viral_advertising(5)}")