import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d\d?)(:\d\d)? ([AP])M to (\d\d?)(:\d\d)? ([AP])M$", s):
        # extract hours
        h1, h2 = int(matches.group(1)), int(matches.group(4))
        # # remove colons and initialize mins to zero if not given in input
        if matches.group(2):
            m1 = matches.group(2).replace(":", "")
        else:
            m1 = "00"
        if matches.group(5):
            m2 = matches.group(5).replace(":", "")
        else:
            m2 = "00"
        # check min validity
        if int(m1) > 59: raise ValueError
        if int(m2) > 59: raise ValueError
        # check for special 12 condition
        if h1 == 12:
            if matches.group(3) == "A":
                h1 = 0
        if h2 == 12:
            if matches.group(6) == "A":
                h1 = 0
        # check hour validity
        if 1 < h1 > 12: raise ValueError
        if 1 < h2 > 12: raise ValueError
        # convert to 24 h
        if h1 < 12 and matches.group(3) == "P": h1 += 12
        if h2 < 12 and matches.group(6) == "P": h2 += 12

        return f"{h1:02}:{m1} to {h2:02}:{m2}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()