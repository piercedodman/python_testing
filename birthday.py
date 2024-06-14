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
    for i in range(bdayList):
        print(f"{bdayList[i][0]}")

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

if __name__ == "__main__":
    main()