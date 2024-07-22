import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    src = False
    for i in range(5,len(s)):
        if s[i-4:i] == "src=":
            src = True
            start = i
        if src == True and s[i] == '"' and i > start:
            end = i
            src = False

            url = s[start+1:end]
            url = url.split("/")
            url = url[-1]
            ret_url = f"https://youtu.be/{url}"
            return ret_url if url !="python" else None




if __name__ == "__main__":
    main()