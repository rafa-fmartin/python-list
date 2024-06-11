import sys


# TODO: the code doesn't accept strings with \n, \t, \r
def text_analyzer(message: str = None) -> str:
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if message is None:
        message = input("What is the text to analyze?\n")
    if not isinstance(message, str):
        print("AssertionError: argument is not a string")
        return

    count_letters = {"upper": 0, "lower": 0, "punct": 0, "space": 0}
    for letter in message:
        if letter.isupper():
            count_letters["upper"] += 1
        elif letter.islower():
            count_letters["lower"] += 1
        elif letter.isspace():
            count_letters["space"] += 1
        elif letter in ".,;:!?-'\"":
            count_letters["punct"] += 1

    print(
        """The text contains {total} character(s):
- {upper} upper letter(s)
- {lower} lower letter(s)
- {punct} punctuation mark(s)
- {space} space(s)""".format(
            total=len(message),
            upper=count_letters["upper"],
            lower=count_letters["lower"],
            punct=count_letters["punct"],
            space=count_letters["space"],
        )
    )


if __name__ == "__main__":
    if sys.argv.__len__() != 2:
        print("AssertionError: wrong number of arguments")
        sys.exit(1)
    text_analyzer(sys.argv[1])
