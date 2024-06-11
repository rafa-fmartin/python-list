import sys


def main():
    if len(sys.argv) < 2:
        return

    string = ""
    for arg in sys.argv[1:]:
        string += arg + " "

    string = string.strip()
    print(string[::-1].swapcase())


if __name__ == "__main__":
    main()
