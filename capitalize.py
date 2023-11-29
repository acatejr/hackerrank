#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    name = None
    if 0 < len(s) and len(s) < 1000:
        parts = s.split(" ")
        name = " ".join(p.capitalize() for p in parts)

    return name

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
