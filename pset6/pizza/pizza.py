from tabulate import tabulate
import sys, csv

if len(sys.argv) != 2:
    sys.exit("usage: pizza.py menuFile.csv")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("CL arg must be CSV file")

try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
