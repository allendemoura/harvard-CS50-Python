from pyfiglet import Figlet
import random, sys

figlet = Figlet()

if len(sys.argv) == 2:
    sys.exit("too few arguments")
elif len(sys.argv) == 3:
    if sys.argv[1] not in ("-f", "--font") or sys.argv[2] not in figlet.getFonts():
        sys.exit("Usage: (-f or --font) font")
    else:
        figlet.setFont(font=sys.argv[2])
elif len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
else:
    sys.exit("Usage: (-f or --font) font")

text = input("Input: ").strip()

print(figlet.renderText(text))