def main():
    time = convert(input("Time? ").strip())
    if 7 <= time <= 8:
        print("breakfast time")
    if 12 <= time <= 13:
        print("lunch time")
    if 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hr, min = time.split(":")
    hr = int(hr)
    if time.endswith("p.m."):
        hr += 12
    min = float(int(min.rstrip('.apm')) / 60)
    return hr + min


if __name__ == "__main__":
    main()