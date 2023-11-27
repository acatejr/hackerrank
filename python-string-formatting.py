def print_formatted(number):

    if 1 <= number and number <= 99:
        for i in range(number):
            n = i + 1
            n_bin = f"{n:b}"
            width = len(f"{number:b}")
            n_oct = f"{n:o}"
            n_hex = f"{n:x}".upper()
            l = f"{n: >{width}} {n_oct: >{width}} {n_hex: >{width}} {n_bin: >{width}}"
            print(l)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
