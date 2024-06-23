import itertools, random, sys


def main():
    try:
        dnum = int(sys.argv[1])
    except IndexError:
        dnum = 1
    except ValueError:
        dnum = 1

    deck = list(itertools.product(range(1, 14), ["s", "h", "d", "c"]))
    random.shuffle(deck)

    shoe = []
    money = 5000

    while True:
        print(f"\nMoney: {money:,}")
        bet = input(f"\nHow much do you bet? (1 - {money:,} or Quit)\n")
        try:
            if bet[0].lower() == "q":
                sys.exit("Thank you for playing!")
            elif 1 <= int(bet) <= money:
                print(f"Bet: {bet}\n")
            else:
                continue
        except ValueError:
            continue

        house = None
        player = None

        house = deck[:2]
        player = deck[2:4]

        bet = int(bet)
        dP = 4
        print("DEALER: ???")

        render(house[0])

        print(f"\nPLAYER:{numTotal(*player)}\n")

        render(*player)

        while True:
            if numTotal(*house) <= 16:
                house.append(deck[dP])
                dP += 1
            move = input("Hit, Stand, or Double Down?\n")
            if move[0].lower() == "h":
                player.append(deck[dP])
                print(f"\nYou drew a {numToName(deck[dP][0])} of {suits(deck[dP][1])}")
                dP += 1
                if numTotal(*player) > 21:
                    break
                else:
                    continue
            elif move[0].lower() == "s":
                break
            elif move[0].lower() == "d":
                bet *= 2
                player.append(deck[dP])
                print(f"\nYou drew a {numToName(deck[dP][0])} of {suits(deck[dP][1])}")
                dP += 1
                break
            elif move[0].lower() == "q":
                sys.exit("Thank you for playing!")
            else:
                continue

        print(f"\nDEALER:{numTotal(*house)}\n")

        render(*house)

        print(f"\nPLAYER:{numTotal(*player)}\n")

        render(*player)

        for _ in range(dP):
            shoe.append(deck[0])
            deck.pop(0)

        if (numTotal(*player) <= 21) and (numTotal(*house) <= 21):
            if numTotal(*player) > numTotal(*house):
                print(f"You win ${bet}!")
                money += bet
                continue
            elif numTotal(*house) > numTotal(*player):
                print(f"You lose ${bet}.")
                money -= bet
                if money <= 0:
                    sys.exit("You are out of money! Thanks for playing!")
                continue
            elif numTotal(*player) == numTotal(*house):
                print("Its a tie!")
                continue
            else:
                print("Error")
                sys.exit()
        elif numTotal(*house) > 21:
            if numTotal(*player) <= 21:
                print(f"You win ${bet}!")
                money += bet
                continue
            else:
                print("Its a tie!")
                continue
        elif numTotal(*player) > 21:
            if numTotal(*house) <= 21:
                print(f"You lose ${bet}.")
                money -= bet
                if money <= 0:
                    sys.exit("You are out of money! Thanks for playing!")
                continue
            else:
                print("Its a tie!")
                continue


def suits(t):
    match t:
        case "s":
            return chr(9824)
        case "h":
            return chr(9829)
        case "d":
            return chr(9830)
        case "c":
            return chr(9827)


def render(*args):
    n = None
    if len(args) == 1:
        n = numToName(args[0][0])
        print(
            f" ___   ___ \n|## | |{n:<3}|\n|###| |{suits(args[0][1]):^3}|\n|_##| |{n:_>3}|\n"
        )
    else:
        cardListT = []
        cardListM1 = []
        cardListM2 = []
        cardListM3 = []
        for i in range(len(args)):
            n = numToName(args[i][0])
            cardListT.append(" ___ ")
            cardListM1.append(f"|{n:<3}|")
            cardListM2.append(f"|{suits(args[i][1]):^3}|")
            cardListM3.append(f"|{n:_>3}|")
        cardListT = "".join(cardListT)
        cardListM1 = "".join(cardListM1)
        cardListM2 = "".join(cardListM2)
        cardListM3 = "".join(cardListM3)
        print(cardListT, cardListM1, cardListM2, cardListM3, sep="\n", end="\n\n")


def numTotal(*args):
    cards = []
    total = 0
    for n in range(len(args)):
        cards.append(args[n][0])
    for i in range(len(cards)):
        if cards[i] == 11 or cards[i] == 12 or cards[i] == 13:
            cards[i] = 10
            total += cards[i]
        else:
            total += cards[i]
    if 1 in cards:
        if total + 10 <= 21:
            return total + 10
        else:
            return total
    else:
        return total


def numToName(n: int):
    match n:
        case 13:
            return "K"
        case 12:
            return "Q"
        case 11:
            return "J"
        case 1:
            return "A"
        case _:
            return n


if __name__ == "__main__":
    main()
