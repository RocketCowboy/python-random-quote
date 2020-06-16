import random


def startup():
    # print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = len(quotes) - 1
    rnd = random.randint(0, last)
    if rnd <= last - 2:
        print(quotes[rnd], end='')
        print(quotes[rnd + 1], end='')
    else:
        print(quotes[rnd - 1], end='')
        print(quotes[rnd], end='')


if __name__== "__main__":
    startup()
