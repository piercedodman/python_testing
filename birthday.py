import random 
import datetime 

def main():
    randomDate()

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