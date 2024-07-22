def main():
    word = input("Enter your word: ")
    print(shorten(word))


def shorten(word):
    new_word = ""
    for letter in word:
        if not letter.upper() in["A","E","I","O","U"]:
            new_word+=letter
    return new_word


if __name__ == "__main__":
    main()