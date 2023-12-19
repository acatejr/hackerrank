def utopian_tree(n):
    height = 1
    
    if 0 <= n and n <= 60:        
        if n == 0:
            return height
        elif n == 1:
            height = 2
        else:
            for p in range(0, n):
                if p%2 == 0:
                    height = height * 2
                else:
                    height = height + 1

    return height

print(utopian_tree(0))
print(utopian_tree(1))
print(utopian_tree(4))
