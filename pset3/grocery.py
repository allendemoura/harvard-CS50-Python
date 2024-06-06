groc = {}
try:
    while True:
        item = input().upper()
        if item in groc:
            groc[item] += 1
        else:
            groc[item] = 1
except EOFError:
    sgroc = sorted(groc.items())
    for item, amount in sgroc:
        print(amount, item)