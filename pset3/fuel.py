while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split(sep="/")
        z = int(x) / int(y)
        if 0 <= z <= 1: break
    except (ValueError, ZeroDivisionError):
        pass

z = round(z * 100)
if z <= 1:
    print("E")
elif z >= 99:
    print("F")
else:
    print(f"{z}%")

