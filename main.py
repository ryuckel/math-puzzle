import re
import itertools
import sys

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

# question2


def question2():

    OP = ["+", "-", "*", "/", ""]

    for val in range(1000, 10000):
        c = str(val)

        for op1, op2, op3 in itertools.product(OP, repeat=3):
            form = c[3] + op1 + c[2] + op2 + c[1] + op3 + c[0]

            # 数値の先頭の0は消す
            form = re.sub(r'(^|\W+)0+(\d)', r'\1\2', form)

            # 0割りを除外する
            if not re.search(r'/0', form):
                if len(form) > 4:
                    if val == eval(form):
                        print(form, " = ", val)


def main():
    question2()


if __name__ == "__main__":
    main()
