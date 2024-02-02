def angry_professor(k, a):
    on_time = 0

    for v in a:
        if v <= 0:
            on_time += 1

    if on_time >= k:
        return "NO"
    else:
        return "YES"
