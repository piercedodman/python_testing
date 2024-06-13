from random import randrange
from datetime import timedelta
def main():
    ...
def randomDate(start, end):
    delta = end - start
    intDelta = (delta.days * 24 * 60 * 60) + delta.seconds
    randomSecond = randrange(intDelta)
    return start +
if __name__ == "__main__":
    main()