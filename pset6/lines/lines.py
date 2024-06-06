import sys

if len(sys.argv) != 2:
    sys.exit("usage: lines.py inputFile.py")
elif not sys.argv[1].endswith(".py"):
    sys.exit("CL arg must be python file")

lines = 0
try:
    with open(sys.argv[1]) as file:
        for line in file:
            if line.lstrip().startswith("#") or line.isspace():
                continue
            lines += 1
except FileNotFoundError:
    sys.exit("File does not exist")
print(lines)