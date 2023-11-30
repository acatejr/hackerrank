import cmath

def complex_to_polar(z):
    if "+" in z:
        x,y = list(map(int, z.replace("j", "").split("+")))
    elif "-" in z:
        pos = z.rfind("-")
        z = z.replace("j", "")
        x = int(z[:pos])
        y = int(z[pos:])

    r = cmath.sqrt((x**2 + y**2))
    theta = cmath.phase(complex(x, y))
    print(r.real)
    print(theta)



if __name__ == "__main__":
    # z = input()
    z = "-1-5j"
    z = "1-1j"
    z = "1+2j"
    complex_to_polar(z)
