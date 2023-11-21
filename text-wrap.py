import textwrap

def wrap(string, max_width):
    s = None

    str_len = len(string)
    if 0 < str_len and str_len < 1000 and 0 < max_width and max_width < str_len:
        _s = "\n".join(s for s in textwrap.wrap(string, max_width))
        s = _s

    return s

if __name__ == '__main__':
    # string, max_width = input(), int(input())
    string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    max_width = 4
    result = wrap(string, max_width)
    print(result)
