import math
import os
import random
import re
import sys

def dayOfProgrammer(year):
    result = ""
    isLeapYear = False
    if year >= 1700 and year <= 2700:
        if year == 1918:
            return f"26.09.{year}"

        if year >= 1700 and year < 1917: # Julian
            if year % 4 == 0:
                isLeapYear = True
        else: # Gregorian
            if year % 4 == 0 and year % 100 != 0:
                isLeapYear = True
            elif year % 400 == 0:
                isLeapYear = True

        if isLeapYear == True:
            result = f"12.09.{year}"
        else:
            result = f"13.09.{year}"

    return result


if __name__ == '__main__':
    print(1800, dayOfProgrammer(1800))
    print(1984, dayOfProgrammer(1984))
    print(1985, dayOfProgrammer(1985))
    print(1915, dayOfProgrammer(1915))
    print(1917, dayOfProgrammer(1917))
    print(1918, dayOfProgrammer(1918))
    print(2016, dayOfProgrammer(2016))
    print(2017, dayOfProgrammer(2017))
    print(2020, dayOfProgrammer(2020))
    print(2022, dayOfProgrammer(2022))
    print(2024, dayOfProgrammer(2024))
    print(2100, dayOfProgrammer(2100)) # Expected 13.09.2100