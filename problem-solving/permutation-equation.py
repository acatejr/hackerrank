def permutation_equation(p):
    results = []
    
    for i in range(len(p)):
        x = i + 1
        idx = p.index(p.index(x)+1)+1
        results.append(idx)

    return results

p = [2,3,1]
print(permutation_equation(p))

p = [5,2,1,3,4]
print(permutation_equation(p))

p = [4,3,5,1,2]
print(permutation_equation(p))