import sys, csv

if len(sys.argv) != 3:
    sys.exit("usage: scourgify.py inputFile.csv outputFile.csv")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("CL args must be CSV files")

students = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(",")
            students.append({"first": first.strip(), "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit("File does not exist")

with open(sys.argv[2], 'w') as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    writer.writerows(students)
