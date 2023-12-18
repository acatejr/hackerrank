def hurdle_race(k, height):
    result = None

    if 1 <= len(height) and k <= 100:
        max_height = max(height)
        if k >= max_height:
            result = 0
        elif k < max_height:
            result = max_height - k

    return result

if __name__ == "__main__":
    print(hurdle_race(1, [1,2,3,3,2]))
    print(hurdle_race(4, [1,6,3,5,2]))
    print(hurdle_race(7, [2,5,4,5,2]))