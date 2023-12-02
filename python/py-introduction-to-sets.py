def average(array):
    n = len(array)
    s = set(array)

    if 0 < n and n <= 100:
        return (sum(s)/len(s))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    result = average(arr)
    print(result)