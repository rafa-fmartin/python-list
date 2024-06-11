import sys


def validate():
    if len(sys.argv) < 2:
        return False
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided")
        return False
    if not sys.argv[1].isnumeric():
        print("AssertionError: argument is not an integer")
        return False
    return True


def main():
    if validate():
        number = int(sys.argv[1])

        if not number:
            print("I'm Zero.")
            return

        is_odd = number % 2
        if is_odd:
            print("I'm Odd.")
        else:
            print("I'm Even.")


if __name__ == "__main__":
    main()
