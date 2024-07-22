import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    num1,num2,num3,num4 = 0,0,0,0
    correct1,correct2 = False,False
    for letter in s:
        if letter == "t":
            correct1 = True
        if letter == "M":
            correct2 = True
    if not correct1 or not correct2:
        num1 = int("hello")
    for i in range(len(s)):
        if s[i] == ":" and num1 == 0:
            num1 = int(s[:i])
            num2 = int(s[i+1:i+3])
            if s[i+4] == "P":
                num1+=12
        elif s[i] == ":" and num3 == 0:
            num3 = int(s[i-2:i]) if s[i-2].isnumeric() else int(s[i-1])
            num4 = int(s[i+1:i+3])
            if s[i+4] == "P":
                num3+=12
        elif s[i] == "M" and num1 == 0:
            num1 = int(s[:i-2])
            if s[i-1] == "P":
                num1 +=12
        elif s[i] == "M" and num3 == 0 and s[1] != ":":
            num3 = int(s[i-4:i-2]) if s[i-4].isnumeric() else int(s[i-3])
            if s[i-1] == "P":
                num3 +=12
    if num1 > 24 or num3 > 24 or num2 > 59 or num4 > 59:
        num1 = int("WRong")
    if num1 % 12 == 0:
        num1-=12
    if num3 % 12 == 0:
        num3-=12
    if num2 <10:
        num2 = f"0{num2}"
    if num4 <10:
        num4 = f"0{num4}"
    if num1 <10:
        num1 = f"0{num1}"
    if num3 <10:
        num3 = f"0{num3}"
    return(f"{num1}:{num2} to {num3}:{num4}")


...


if __name__ == "__main__":
    main()