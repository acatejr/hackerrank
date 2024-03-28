def save_the_prisoner(n, m, s):
    w = (m + s - 1) % n
    if (w == 0):
        w = n
        return w
    else:
        return w

n = 4 
m = 6
s = 2
print(save_the_prisoner(n, m, s)) # 3


n = 5
m = 2
s = 1
print(save_the_prisoner(n, m, s)) # 2

n = 5
m = 2
s = 2
print(save_the_prisoner(n, m, s)) # 3

n = 7 
m = 19
s = 2
print(save_the_prisoner(n, m, s)) # 3

n = 3 
m = 7
s = 3
save_the_prisoner(n, m, s) # 3