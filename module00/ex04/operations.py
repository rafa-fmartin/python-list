import sys


def validate():
    if len(sys.argv) < 3:
        print(
            """Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3"""
        )
        return False
    if len(sys.argv) > 3:
        print("AssertionError: too many arguments")
        return False
    if not isinstance(sys.argv[1], int) or not isinstance(sys.argv[2], int):
        print("AssertionError: only integers")
        return False
    return True


def main():
    if validate():
        number1 = int(sys.argv[1])
        number2 = int(sys.argv[2])

        summ = number1 + number2
        diff = number1 - number2
        prdct = number1 * number2
        if not number2:
            div = "ERROR (division by zero)"
            mod = "ERROR (modulo by zero)"
        else:
            div = number1 / number2
            mod = number1 % number2

        message = """Sum:        {sum}
Difference: {diff}
Product:    {prdct}
Quotient:   {div}
Remainder:  {mod}""".format(
            sum=summ, diff=diff, prdct=prdct, div=div, mod=mod
        )

        print(message)

    return


if __name__ == "__main__":
    main()
