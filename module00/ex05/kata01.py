kata = {
    "Python": "Guido van Rossum",
    "Ruby": "Yukihiro Matsumoto",
    "PHP": "Rasmus Lerdorf",
}


def main():
    str = "".join(
        [
            "{language} was created by {creator}\n".format(language=x, creator=kata[x])
            for x in kata
        ]
    )[:-1]

    print("{str}".format(str=str))


if __name__ == "__main__":
    main()
