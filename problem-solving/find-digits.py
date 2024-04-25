def find_digits(n):
    digits = 0

    for d in f"{n}":
        i = int(d)
        if i != 0:
            if n%i == 0:
                digits += 1

    return (digits)

print(find_digits(124))
print(find_digits(111))
print(find_digits(10))