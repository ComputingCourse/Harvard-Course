phrase = input("Input: ")
vowels = ["a","e","i","o","u"]
for vowel in vowels:
    phrase = phrase.replace(vowel,"")
    phrase = phrase.replace(vowel.upper(),"")
print(phrase)