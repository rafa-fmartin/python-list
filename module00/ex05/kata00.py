kata = (19, 42, 21)


def main():
    str = "".join([f" {x}," for x in kata])[:-1]
    print("The {numbers} numbers are:{str}".format(numbers=len(kata), str=str))


if __name__ == "__main__":
    main()
