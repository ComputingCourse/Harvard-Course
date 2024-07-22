def convert(phrase):
    new_phrase = []
    prev = False
    for i in  range (len(phrase)-1):
        if phrase[i] + phrase[i+1] == ":)":
            new_phrase.append("🙂")
            i += 1
            prev = True
        elif phrase[i] + phrase[i+1] == ":(":
            new_phrase.append("🙁")
            i += 1
            prev = True
        else:
            if not prev:
                new_phrase.append(phrase[i])
            else:
                prev = False
    if phrase[len(phrase)-1] != ")" and phrase[len(phrase)-1] != "(":
        new_phrase.append(phrase[len(phrase)-1])
    print(*new_phrase, sep="")

def main():
    phrase = input("Enter a phrase: ")
    convert(phrase)

main()