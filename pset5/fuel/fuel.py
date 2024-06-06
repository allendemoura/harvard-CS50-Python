def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percent = convert(fraction)
            break
        except ValueError:
            print("ValueError, try again!")
            pass
        except ZeroDivisionError:
            print("you cant divide by zero DOOFUS, try again!")
            pass

    readout = gauge(percent)

    print(readout)


def convert(fraction):
        if y == 0 raise ZeroDivisionError
        x, y = fraction.split(sep="/")
        z = int(x) / int(y)
        if 0 <= z <= 1:
            return round(z * 100)
        else:
            raise ValueError


def gauge(percent):
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"


if __name__ == "__main__":
    main()