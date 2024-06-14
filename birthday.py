import random 
import datetime 

def main():
    while True:
        bdays = int(input("How many birthdays should I generate? (Max 100)\n"))
        if bdays <= 100:
            break
        else:
            raise ValueError("Please enter a lower integer.")
    bdayList = []
    for _ in range(int(bdays)):
        bdayList.append(randomDate())
    
    print(f"Here are {bdays} birthdays:")
    for i in range(len(bdayList)):
        print(f"{monthConverter(bdayList[i][0])} {bdayList[i][1]},", end = ' ')

    print("\nIn this simulation multiple people have their birthday on", end=' ')
    n = dupFinder(bdayList)
    for i in range(len(n)):
        print(f"{monthConverter(n[i][0])} {n[i][1]},", end = ' ')

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

if __name__ == "__main__":
    main()