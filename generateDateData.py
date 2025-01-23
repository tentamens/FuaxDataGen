from datetime import datetime


def main():
    current_month = datetime.now().strftime("%h")
    data = []

    for i in range(6, 19):
        data.append(str(i) + " " + current_month)
    print(data)


if __name__ == "__main__":
    main()
