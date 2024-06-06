import random, sys



def main():
    level = get_level()
    score = 0
    for _ in range(10):
        tries = 3
        num1, num2 = generate_integer(level), generate_integer(level)
        while tries > 0:
            try:
                ans = int(input(f"{num1} + {num2} = "))
                if ans == num1 + num2:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                tries -= 1
        else:
            print(f"{num1} + {num2} = {num1 + num2}")
    print("Score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if 1 <= level <= 3:
            return level

def generate_integer(level):
    if level == 1:
        return random.randint(0,10)
    else:
        return random.randint(10**(level - 1), 10**level - 1)


if __name__ == "__main__":
    main()