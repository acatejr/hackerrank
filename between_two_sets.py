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

    factors = {}
    _factors = []
    for i in b:
        for v in getFactors(i):
            _factors.append(v)

    fact_dict = {i: _factors.count(i) for i in _factors}
    print(fact_dict)
    # print(_factors)

a = [1,2]
b = [24,36]

# a = [2,4]
# b = [16, 32,96]
print(getTotalX(a,b))

