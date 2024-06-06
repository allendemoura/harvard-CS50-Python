cost = 50
while True:
    print("Amount Due: ", cost)
    coin = int(input("Insert Coin: "))
    if coin not in [5, 10, 25]:
        continue
    cost -= coin
    if cost <= 0:
        print("Change Owed: ", 0 - cost)
        break
