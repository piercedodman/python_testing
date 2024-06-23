import random as r


def main():
    intro()
    try:
        guesses()
        while True:
            ans = input("\nDo you want to play again? (yes or no)\n")
            if ans.lower().strip() == "no" or ans.lower().strip() == "n":
                exit("Thanks for playing!")
            elif ans.lower().strip() == "yes" or ans.lower().strip() == "y":
                guesses()
    except KeyboardInterrupt:
        exit()


def intro():
    print(
        "Bagels, a deductive logic game\nBy PieDod\nI am thinking of a 3-digit number. Try to guess what it is."
    )
    print("Here are some clues:")
    print("When I say:     That means:")
    print("  Pico          One digit is correct but in the wrong place.")
    print("  Fermi         One digit is correct and in the right place.")
    print("  Bagels        No digit is correct.")
    print("I have thought of a number.")
    print("  You have 10 guesses to get it.")


def guesses():
    num1 = r.randint(100, 999)
    num = [int(x) for x in str(num1)]
    i = 1
    while i <= 10:
        print(f"\nGuess #{i}:")
        inp = input()
        try:
            inp = [int(x) for x in inp]
            if inp == num:
                print("You got it!")
                break
            for n in range(len(num)):
                if inp[n] == num[n]:
                    print("Fermi", end=" ")
                elif inp[n] in num:
                    print("Pico", end=" ")

            check = False
            for n in inp:
                if n in num:
                    check = True
            if check == False:
                print("Bagels", end=" ")
            i += 1
        except ValueError:
            print("Please enter a 3-digit integer.")
        except IndexError:
            print("Please enter a 3-digit integer.")

    print("\nThe correct number was", num1)


if __name__ == "__main__":
    main()
