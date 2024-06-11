from datetime import datetime


kata = (2019, 9, 25, 3, 30)


def main():
    print(datetime(*kata).strftime("%d/%m/%Y %H:%M"))


if __name__ == "__main__":
    main()
