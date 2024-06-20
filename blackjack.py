import itertools, random, sys, collections

def main():
    try:
        dnum = int(sys.argv[1])
    except IndexError:
        dnum = 1
    except ValueError:
        dnum = 1
    
    deck = list(itertools.product(range(1,14), ['s', 'h', 'd', 'c']))
    random.shuffle(deck)

    shoe = []
    money = 5000
    
    while True:
        print(f"Money: {money:,}")
        bet = input(f"\nHow much do you bet? (1 - {money:,} or Quit)\n")
        try:
            if bet[0].lower() == 'q':
                sys.exit("Thank you for playing!")
            if 1 <= int(bet) <= money:
                print(f"Bet: {bet}\n")
            else:
                continue
        except ValueError:
            continue
        
        house = deck[:2]
        player = deck[2:4]

        print("DEALER: ???")

        render(house[0])

        print(f"\nPLAYER:{...}\n")

        render(*player)

def suits(t):
    match t:
        case 's':
            return chr(9824)
        case 'h':
            return chr(9829)
        case 'd':
            return chr(9830)
        case 'c':
            return chr(9827)

def render(*args):
    n = None
    if len(args) == 1:
        n = numToName(args[0][0])
        print(f" ___   ___ \n|## | |{n:<3}|\n|###| |{suits(args[0][1]):^3}|\n|_##| |{n:_>3}|\n")

    if len(args) == 2:
        n = numToName(args[0][0])
        n0 = numToName(args[1][0])
        print(f" ___   ___ \n|{n0:<3}| |{n:<3}|\n|{suits(args[1][1]):^3}| |{suits(args[0][1]):^3}|\n|{n0:_>3}| |{n:_>3}|\n")

def total(*args):
    cards = []
    total = 0
    for n in args:
        cards.append(args[n][0])
    if 1 in cards:
        return

#figure out total mechanism here 


def numToName(n: int):
    if n == 13:
        return 'K'
    elif n == 12:
        return 'Q'
    elif n == 11:
        return 'J'
    elif n == 1:
        return 'A'
    else:
        return n
        
if __name__ == "__main__":
    main()