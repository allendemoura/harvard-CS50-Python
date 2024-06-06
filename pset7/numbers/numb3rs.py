import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([\d]+)\.([\d]+)\.([\d]+)\.([\d]+)$", ip):
        for num in matches.groups():
            if int(num) not in range(256):
                return False
        if len(matches.groups()) == 4:
            return True
    else:
        return False



if __name__ == "__main__":
    main()