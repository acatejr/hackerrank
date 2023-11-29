def merge_the_tools(string, k):
    n = len(string)

    if (1 <= n and n <= 10**4) and (1 <= k and k <= n):
        part_count = int(n/k)
        for i in range(part_count):
            start = i * k
            stop = start + k
            part = string[start:stop]

            _part = []
            for c in part:
                if c not in _part:
                    _part.append(c)

            part = "".join(c for c in _part)
            print(part)

    else:
        return

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
