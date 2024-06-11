kata = (0, 4, 132.42222, 10000, 12345.67)


def main():
    exercise = "module_{:02d}, ex_{:02d}".format(kata[0], kata[1])
    infos = "{:.2f}, {:.2e}, {:.2e}".format(kata[2], kata[3], kata[4])
    print("{} : {}".format(exercise, infos))


if __name__ == "__main__":
    main()
