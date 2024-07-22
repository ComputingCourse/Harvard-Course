import random,sys

def main():
    level = get_level()
    score = 0
    for i in range (10):
        num1,num2 = generate_integer(level)
        for j in range(3):
            ans = input(f"{num1} + {num2} = ")
            if ans == str(num1 + num2):
                score +=1
                break
            print("EEE")
            i+=1
            if j == 2:
                print(f"{num1} + {num2} = {num1+num2}")
    print(f"Score: {score}")

def get_level():
    level = ""
    while level != "1" and level != "2" and level != "3":
        level = input("Level: ")
    return int(level)

def generate_integer(level):
    num = 0 if level == 1 else 10**(level-1)
    num1 = random.randint(num,(10**level)-1)
    num2 = random.randint(num,(10**level)-1)
    return num1,num2

if __name__ == "__main__":
    main()