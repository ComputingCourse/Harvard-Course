import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    ums = 0
    s+=","
    for i in range(len(s)):
        if s[i].lower() == "u" and i < len(s)-2:
            if i == 0 and s[i+1].lower() == "m" and not s[i+2].isalpha():
                ums+=1
            elif s[i:i+2].lower() == "um" and not s[i-1].isalpha() and not s[i+2].isalpha():
                ums +=1

    return ums


if __name__ == "__main__":
    main()