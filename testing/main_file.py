from random import random
from traceback import print_exc


def add_two_numbers(num1, num2):
    return num1 + num2


def multiply_two_numbers(num1, num2):
    return num1 * num2


def asset_an_error(num1, num2):
    try:
        return num1 / num2
    except Exception as e:
        return e.__class__.__name__


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return False


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if run_guess(guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue

print(asset_an_error(20, 0))
