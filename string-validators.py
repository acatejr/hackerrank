def any_alnum(s):
    for c in s:
        if c.isalnum():
            return True

    return False

def any_isalpha(s):
    for c in s:
        if c.isalpha():
            return True

    return False

def any_isdigit(s):
    for c in s:
        if c.isdigit():
            return True

    return False

def any_islower(s):
    for c in s:
        if c.islower():
            return True

    return False

def any_isupper(s):
    for c in s:
        if c.isupper():
            return True

    return False

if __name__ == "__main__":
    # s = "qA2"
    s = input()
    if 0 < len(s) and len(s) < 1000:
        print(any_alnum(s))
        print(any_isalpha(s))
        print(any_isdigit(s))
        print(any_islower(s))
        print(any_isupper(s))