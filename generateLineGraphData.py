import random


def main():
    data = []
    lastNum = random.randint(10, 50)
    for _ in range(6, 19):
        newNum = random.randint(lastNum-10, lastNum+10)
        lastNum = newNum
        data.append(newNum)
    print(data)


if __name__ == "__main__":
    main()
