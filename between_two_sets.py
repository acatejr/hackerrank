"""_summary_
https://courses.lumenlearning.com/mathforliberalartscorequisite/chapter/finding-all-the-factors-of-a-number/
"""
    
    
def getFactors(v):
    
    results = [1, v]
    
    divisor = 2
    for i in range(divisor, v+1):
        remainder = v % i
        if remainder == 0 and (i > remainder) and (i not in results):
            results.append(i)
            
    results.sort()
    return results

def getTotalX(a, b):
    
    factors = []
    for i in b:
        _factors = getFactors(i)
        factors.append(_factors)
    print(factors)

a = [1,2]
b = [24,36]

print(getTotalX(a,b))

