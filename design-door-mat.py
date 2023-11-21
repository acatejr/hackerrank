from math import floor
# Enter your code here. Read input from STDIN. Print output to STDOUT
def mat(n, m):
    string = None
    item = ".|."
    mid_row = floor(n/2)
    for i in range(n):
        if i != mid_row:
            print(f"{item}")
        else:
            print("WELCOME")
    return string


if __name__ == "__main__":
    # vals = input()
    # vals = "9 27"
    vals = "11 33"
    vals = vals.split(" ")
    n = int(vals[0])
    m = int(vals[1])
    mat(n, m)