from datetime import date
import inflect, re, sys
p = inflect.engine()

def main():
    inp = input("Date of Birth: ")
    d = valiDate(inp)
    min = minutes(d)
    print(p.number_to_words(min).replace(" and", "").capitalize(), "minutes")

def valiDate(inp):
    if matches := re.search(r"^(\d\d\d\d)-(\d\d)-(\d\d)", inp):
        year, month, day = matches.groups()
    else:
        sys.exit("Invalid date")
    try:
        d = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")
    return d

def minutes(d):
    delta = date.today() - d
    return int(delta.total_seconds() / 60)

if __name__ == "__main__":
    main()