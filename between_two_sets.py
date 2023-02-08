"""_summary_
https://courses.lumenlearning.com/mathforliberalartscorequisite/chapter/finding-all-the-factors-of-a-number/
"""

def getTotalX(a, b):

    total = 0
    
    factors = []
    for i in b:
        _factors = [x for x in range(1, i+1) if i % x == 0]    
        factors += _factors
    
    factors = {i: factors.count(i) for i in factors}
    factors = [i for i in factors if factors[i] == len(b)]
    # print(factors)
    
    total = 0        
    candidates = []
    print(a)
    # for v in a:
    #     print(v)
    #     for f in factors:
    #         rem = f % v
    #         if rem == 0:
    #             # print(f"{f} % {v} = {rem}")
    #             candidates.append(f)

    # candidates = {i: candidates.count(i) for i in candidates}
    # candidates = [i for i in candidates if candidates[i] == len(a)]
    # print(candidates)
    # total = len(candidates)

    return total

    # if len(a) == 1 and a[0] == 1:
    #     return len(getFactors(b[0]))
    
    # _factors = []
    # for i in b:
    #     for v in getFactors(i):
    #         _factors.append(v)
    
    # _factors = {i: _factors.count(i) for i in _factors}
    # _factors = [i for i in _factors if _factors[i] == len(b)]
    # # print(_factors) # [1, 2, 3, 4, 6, 12]
    
    
    # total = 0        
    # candidates = []
    # for v in a:
    #     for f in _factors:
    #         rem = f % v
    #         if rem == 0:
    #             # print(f"{f} % {v} = {rem}")
    #             candidates.append(f)

    # candidates = {i: candidates.count(i) for i in candidates}
    # candidates = [i for i in candidates if candidates[i] == len(a)]
    # total = len(candidates)
    
    # return total

a = [2, 6]
b = [24, 36]
getTotalX(a,b)

a = [2, 4]
b = [16, 32, 96]
getTotalX(a,b)

a = [1]
b = [100]
getTotalX(a,b)

# a = [1]
# b = [72, 48]
# getTotalX(a,b)

