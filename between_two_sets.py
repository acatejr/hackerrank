"""_summary_
https://courses.lumenlearning.com/mathforliberalartscorequisite/chapter/finding-all-the-factors-of-a-number/
"""

def getTotalX(a, b):

    factors = []
    for i in b:
        _factors = [x for x in range(1, i+1) if i % x == 0]    
        factors += _factors
    
    factors = {i: factors.count(i) for i in factors}
    factors = [i for i in factors if factors[i] == len(b)]
    
    total = 0        
    candidates = []
    for v in a:
        for f in factors:
            rem = f % v
            if rem == 0:
                candidates.append(f)

    candidates = {i: candidates.count(i) for i in candidates}
    candidates = [i for i in candidates if candidates[i] == len(a)]    
    total = len(candidates)

    return total

a = [2, 6]
b = [24, 36]
print(getTotalX(a,b))

a = [2, 4]
b = [16, 32, 96]
print(getTotalX(a,b))

a = [1]
b = [100]
print(getTotalX(a,b))

a = [1]
b = [72, 48]
print(getTotalX(a,b))

