def minion_game(string):
    str_len = len(string)
    vowels = "AEIOU"
    cscore = 0
    vscore = 0

    if 0 < str_len and str_len <= 10**6:
        if string.isupper() == False:
            string = string.upper()

        for i in range(str_len):
            c = string[i]
            if c in vowels:
                vscore += str_len - i
            else:
                cscore += str_len - i

    if vscore == cscore:
        print("Draw")
    elif vscore > cscore:
        print(f"Kevin {vscore}")
    else:
        print(f"Stuart {cscore}")

if __name__ == '__main__':
    # s = input()
    s = "BANANA"
    minion_game(s)