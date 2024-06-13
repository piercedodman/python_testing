import random as r

def main():
    intro()
    guesses()

def intro():
    print("Bagels, a deductive logic game\nBy PieDod\nI am thinking of a 3-digit number. Try to guess what it is.")
    print("Here are some clues:")
    print("When I say:     That means:")
    print("  Pico          One digit is correct but in the wrong place.")
    print("  Fermi         One digit is correct and in the right place.")
    print("  Bagels        No digit is correct.")
    print("I have thought of a number.")
    print("  You have 10 guesses to get it.")

def guesses():
    num = [int(x) for x in str(r.randint(100,999))]
    i = 1
    while i <= 10:
        print(f"\nGuess #{i}:")
        inp = input()
        inp = [int(x) for x in inp]
        for n in range(len(num)):
            if inp == num:
                exit("You got it!")     
            elif inp[n] == num[n]:
                print("Fermi", end = ' ')
            elif inp[n] in num:
                print("Pico", end = ' ')
            elif set(inp).intersection(set(num)) == None:
                print("Bagels")
        i += 1

if __name__ == "__main__":
    main()
