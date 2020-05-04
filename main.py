# question1


def ispalindrome(x):
    return str(x) == str(x)[::-1]


def question1():
    i = 11
    while True:
        if ispalindrome(i) and ispalindrome(format(i, 'b')) and ispalindrome(format(i, 'o')):
            break
        i += 2
    print(i)


def main():
    question1()


if __name__ == "__main__":
    main()
