import random


def menu():
    return """This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!"""


def main():
    secret_number = random.choice(range(1, 100))

    attempts = 0
    while True:
        choice = input("What's your guess between 1 and 99?\n")
        attempts += 1
        if choice == "exit":
            print("Goodbye!")
            break
        elif int(choice) > 99:
            print("Must be below or equal 99.")
        elif int(choice) < 1:
            print("Must be above or equal 1.")
        elif int(choice) > secret_number:
            print("Too high!")
        elif int(choice) < secret_number:
            print("Too low!")
        elif int(choice) == secret_number:
            if attempts == 1:
                congrats = "Congratulations, you've got it on your first try!"
            else:
                congrats = (
                    f"Congratulations, you've got it!\nYou won in {attempts} attempts!"
                )
            if secret_number == 42:
                print(
                    "The answer to the ultimate question of life, the universe and everything is 42.\n"
                    + congrats
                )
            else:
                print(congrats)
            break
        else:
            print("That's not a number.")


if __name__ == "__main__":
    main()
