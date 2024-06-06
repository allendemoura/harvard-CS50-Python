months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    date = input("Date: ").title().strip()
    if date[0].isalpha() and "/" not in date:
        month, day, year = date.split(sep=" ")
        if month in months:
            month = months[month]
        else:
            continue
        if day.endswith(","):
            day = day.rstrip(",")
        else:
            continue
    elif "/" in date and date[0].isdecimal():
        month, day, year = date.split(sep="/")
    else:
        continue
    month, day, year = int(month), int(day), int(year)
    if 1 <= month <= 12 and 1 <= day <= 31 and 0 <= year < 10000:
        break
print(f"{year:04}-{month:02}-{day:02}")