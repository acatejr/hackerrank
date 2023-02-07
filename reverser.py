def reverse(word):

    out = ""
    size = len(word)
    idx = size - 1

    while idx >= 0:
        out += word[idx]
        idx -= 1
    
    return out

print(reverse("word"))
print(reverse("hockey"))