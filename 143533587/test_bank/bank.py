def main():
    greeting = input("Enter your greeting: ")
    print(value(greeting))

def value(greeting):
    if greeting[:5].lower() == "hello":
        val = 0
    elif greeting[0].lower() == "h":
        val = 20
    else:
        val = 100
    return val

if __name__ == "__main__":
    main()