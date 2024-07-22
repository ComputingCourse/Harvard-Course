def main():
    fraction = input("Enter fraction: ")
    print(gauge(convert(fraction)))


def convert(fraction):
    num1 = 0
    num2 = 0
    for i in range(len(fraction)):
        if fraction[i] == "/":
            for j in range(i):
                num1 += int(fraction[j]) * 10**(i-j-1)
            for k in range(i+1, len(fraction)):
                num2 += int(fraction[k]) * 10**(len(fraction)-1-k)
    percent = int(round(num1/num2 * 100,0))
    if not percent <=100:
        percent = int("hello")
    return percent


def gauge(percentage):
    if percentage <= 1:
        ret = "E"
    elif percentage >= 99:
        ret = "F"
    else:
        ret = f"{percentage}%"
    return ret


if __name__ == "__main__":
    main()