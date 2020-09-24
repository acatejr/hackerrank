import math

def diagonalDifference(arr):
    index = len(arr)
    first_dia =  sum(arr[i][i]for i in range(index))
    second_dia = sum(arr[i][index-i-1]for i in range(index))
    return (abs(first_dia - second_dia))

arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

print(diagonalDifference(arr))