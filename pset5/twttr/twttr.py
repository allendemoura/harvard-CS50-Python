def main():
    i = input("Input: ")
    print("Output:", shorten(i))


def shorten(str):
    for c in ['a', 'A', 'e', 'E', 'i', 'I' ,'o', 'O', 'u', 'U', ]:
        str = str.replace(c, '')
    return str


if __name__ == "__main__":
    main()