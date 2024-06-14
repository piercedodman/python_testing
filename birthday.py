import random 

def main():
    SIMRUNS = 1000000
    while True:
        bdays = int(input("How many birthdays should I generate? (Max 100)\n"))
        if bdays <= 100:
            break
        else:
            raise ValueError("Please enter a lower integer.")
        
    bdayList = bdayLGen(bdays)
    
    print(f"Here are {bdays} birthdays:")
    for i in range(len(bdayList)):
        print(f"{monthConverter(bdayList[i][0])} {bdayList[i][1]},", end = ' ')

    n = dupFinder(bdayList)
    if not n:
        print("\nAll birthdays in this simulated group are unique.")
    else:
        print("\nIn this simulation multiple people have their birthday on", end=' ')
        for i in range(len(n)):
            print(f"{monthConverter(n[i][0])} {n[i][1]},", end = ' ')

    print(f"Generating {bdays} random birthdays {SIMRUNS:,d} times...")
    print("This may take a moment. Your patience is appreciated.")

    dupcount = 0
    for i in range(SIMRUNS):
        bdayList1 = bdayLGen(bdays)
        m = dupFinder(bdayList1)
        if len(m) > 0:
            dupcount += 1
    
    print(f"\nOut of {SIMRUNS:,d} simulations of {bdays} people, there was a matching birthday {dupcount:,d} times.")
    print(f"This means that {bdays} people have a {dupcount/SIMRUNS:.2%} of having a matching birthday in their group.")

def randomDate():
    month = random.randint(1, 12)
    match month:
        case 4 | 6 | 9 | 11:
            maxday = 30
        case 2:
            maxday = 28
        case _ :
            maxday = 31
    day = random.randint(1, maxday)
    return (month, day)

def monthConverter(m):
    match m:
        case 1:
            return "Jan"
        case 2:
            return "Feb"
        case 3:
            return "Mar"
        case 4:
            return "Apr"
        case 5:
            return "May"
        case 6:
            return "Jun"
        case 7:
            return "Jul"
        case 8:
            return "Aug"
        case 9:
            return "Sep"
        case 10:
            return "Oct"
        case 11:
            return "Nov"
        case 12:
            return "Dec"

def dupFinder(tlist):
    d = {}
    duplicates = []
    for tup in tlist:
        if tup in d:
            duplicates.append(tup)
        else:
            d[tup] = 1
    return duplicates

def bdayLGen(n):
    bdayList = []
    for _ in range(int(n)):
        bdayList.append(randomDate())
    return bdayList

if __name__ == "__main__":
    main()