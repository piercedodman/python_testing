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
    print(bdayList)


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

if __name__ == "__main__":
    main()