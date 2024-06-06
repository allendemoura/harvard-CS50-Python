def main():
    greet = input("Greet? ")
    print("$" + str(value(greet)))


def value(str):
    str = str.lower().strip()
    if str[0:5] == "hello":
        return 0
    elif str[0] == 'h':
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()