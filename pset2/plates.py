def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    digits = False
    if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        for char in s:
            if not digits and char.isdigit():
                digits = True
                if char == '0':
                    return False
            elif digits and char.isalpha():
                return False
        return True
    else:
        return False


main()