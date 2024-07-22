answer = input("What is the answer to the Great Question of Life, the Universe and Everything?: ")
answer = answer.replace(" ","")
if answer.lower() == "forty-two" or answer.lower() == "fortytwo" or answer == "42":
    print("Yes")
else:
    print("No")