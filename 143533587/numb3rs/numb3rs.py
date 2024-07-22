import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    numbers = ip.split(".")
    if len(numbers) != 4:
        return False
    else:
        for num in numbers:
            if not int(num) <= 255 or not int(num) >= 0 :
                return False
        return True


if __name__ == "__main__":
    main()