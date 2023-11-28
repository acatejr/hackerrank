def print_rangoli(size):

    output = ""
    if 0 < size and size < 27:
        if size == 1:
            output = "a"
        else:
            lines = []
            letters = "abcdefghijklmnopqrstuvwxyz"
            width = (2*(size-1)) + ((2*size) - 1)
            if 0 < size and size < 27:
                for i in range(size-1, -1, -1):
                    _letters = letters[i:size]
                    _letters = _letters[::-1][:-1] + letters[i:size]
                    alphas = "-".join(c for c in _letters)
                    l = alphas.center(width, "-")
                    lines.append(l)

            output = "\n".join(l for l in lines[:-1]) + "\n"
            output += "\n".join(l for l in lines[::-1])

        print(output)
    return output


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

