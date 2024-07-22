import validators

def main():
    email = input("What's your email address? ")
    print(validate(email))

def validate(email):
    parts = email.split("@")
    if len(parts) !=  2:
        return "Invalid"
    if len(parts[0]) < 4:
        return "Invalid"
    parts = parts[1].split(".")
    if len(parts) != 2 :
        for part in parts:
            if len(part) < 3:
                return "Invalid"
    if len(parts[0]) < 3 or len(parts[1]) < 3:
        return "Invalid"
    return "Valid"

if __name__ == "__main__":
    main()