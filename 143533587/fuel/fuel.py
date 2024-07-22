done = False
while not done:
    num1 = 0
    num2 = 0
    fraction = input("Fraction: ")
    for i in range(len(fraction)):
        if fraction[i] == "/":
            try:
                for j in range(i):
                    num1 += int(fraction[j]) * 10**(i-j-1)
                for k in range(i+1, len(fraction)):
                    num2 += int(fraction[k]) * 10**(len(fraction)-1-k)#
                try:
                    percentage = int(round(num1 / num2 * 100, 0))
                    if percentage > 100:
                        break
                    elif percentage >= 99:
                        percentage = "F"
                    elif percentage <= 1:
                        percentage = "E"
                    else:
                        percentage = str(percentage)+"%"
                    print(percentage)
                    done = True
                except ZeroDivisionError:
                    break
            except ValueError:
                break

