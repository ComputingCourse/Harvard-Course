def main():
    time = input("What time is it?: ")
    time = convert(time)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    time = time.replace(" ", "")
    if len(time) == 4:
        ret = int(time[0]) + (int(time[2])*10 + int(time[3]))/60
    elif len(time) == 5:
        ret = int(time[0])*10 + int(time[1])+ (int(time[3])*10 + int(time[4]))/60
    elif len(time) == 8:

        if time[-4] == "a":
            ret = int(time[0]) + (int(time[2])*10 + int(time[3]))/60
        else:
            ret = int(time[0]) + (int(time[2])*10 + int(time[3]))/60 + 12
    elif len(time) == 9:
        if time[-4] == "a":
            ret = int(time[0])*10 + int(time[1])+ (int(time[3])*10 + int(time[4]))/60
        else:
            ret = int(time[0])*10 + int(time[1])+ (int(time[3])*10 + int(time[4]))/60 + 12
    else:
        ret = 0

    return ret

if __name__ == "__main__":
    main()