import random, sys

def positive_num (text):
    num = 0
    while num <1:
        num = input(text)
        num = 0 if not num.isnumeric() else int(num)
    return num

level = positive_num("Level: ")
number = random.randint(1,level)
while True:
    guess = positive_num("Guess: ")
    if guess == number:
        sys.exit("Just right!")
    elif guess > number:
        print("Too large!")
    else:
        print("Too small!")