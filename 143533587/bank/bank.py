Greeting = input("Greeting: ")
Greeting = Greeting.replace(" ","")
if Greeting[:5].lower() == "hello":
    print("$0")
elif Greeting[0].lower() == "h":
    print("$20")
else:
    print("$100")