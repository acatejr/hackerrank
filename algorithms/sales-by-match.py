#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    num_pairs = 0

    pairs = {}
    if 1 <= n and n <= 100:
        for i in range(n):
            if ar[i] not in pairs.keys():
                pairs[ar[i]] = 1
            else:
                pairs[ar[i]] += 1

        for p in pairs:
            color = pairs[p]
            if color % 2 == 0:
                num_pairs += int(color/2)
            if color != 0 and color % 2 > 0: 
                num_pairs += math.floor(color/2)

    return num_pairs

if __name__ == '__main__':
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    result = sockMerchant(n, ar)
    print(result)

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input().strip())
    # ar = list(map(int, input().rstrip().split()))
    # result = sockMerchant(n, ar)
    # fptr.write(str(result) + '\n')
    # fptr.close()
