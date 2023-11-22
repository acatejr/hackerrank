from math import floor
# Enter your code here. Read input from STDIN. Print output to STDOUT
def mat(n, m):
    string = None
    c = ".|."
    cone = []

    # Top Cone
    for i in range(int(n/2)):
        l = (c*i) + c + (c*i)
        pads = "-" * (int((m - len(l))/2))
        item = f"{pads}{l}{pads}"
        cone.append(item)
        print(item)

    # Welcome
    welcome = "WELCOME"
    pads = int((m - len(welcome))/2) * "-"
    print(f"{pads}{welcome}{pads}")

    # Bottom Cone
    cone.reverse()
    for i in cone:
        print(i)

    return string


if __name__ == "__main__":
    
    # vals = "9 27"
    # vals = "11 33"
    vals = input()
    vals = vals.split(" ")
    n = int(vals[0])
    m = int(vals[1])
    mat(n, m)
