import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"src=\"https?://(www\.)?youtube\.com/embed/([\w]+)", s):
        short = re.sub(r"src=\"https?://(www\.)?youtube\.com/embed", "https://youtu.be", matches.group(0))
        return short
    else:
        return None


if __name__ == "__main__":
    main()