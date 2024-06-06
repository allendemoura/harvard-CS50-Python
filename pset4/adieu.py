import inflect

p = inflect.engine()
names = []

while True:
    try:
        text = input("Names: ")
    except EOFError:
        break
    names.append(text)

print("Adieu, adieu, to", p.join(names))
