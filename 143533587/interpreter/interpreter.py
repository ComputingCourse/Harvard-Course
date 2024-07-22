math = input("Expressionl: ")
num1 = 0
num2 = 0
for i in range(len(math)):
    if math[i] == " ":
        for j in range(i):
            num1 += int(math[i-j-1]) * 10**j
        symbol = math[i+1]
        break
for i in range(len(math)):
     if math[-i] == " ":
        for j in range (i-1):
             num2 += int(math[-(j+1)]) * 10**j
        break
if symbol == "+":
    print(round(float(num1+num2), 1))
elif symbol == "-":
    print(round(float(num1-num2), 1))
elif symbol == "*":
    print(round(float(num1*num2), 1))
else:
    print(round(float(num1/num2), 1))