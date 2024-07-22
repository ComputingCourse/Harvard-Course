phrase = input("Enter your phrase: ")
new_phrase = []
for letter in phrase:
    if letter == " ":
        new_phrase.append("...")
    else:
        new_phrase.append(letter)
print(*new_phrase, sep="")