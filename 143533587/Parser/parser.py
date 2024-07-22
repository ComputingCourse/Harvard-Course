import nltk
from nltk.tree import Tree
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were" | "walk"
"""

NONTERMINALS = """
S -> NP VP | NP VP Conj NP VP | NP VP Conj VP | NP VP PP VP |N V Det Adj N P N Conj V N P Det Adj N
NP -> N | Detp | Adjp | NP PP
VP -> V | V NP | Advp NP | V PP | Adjp
Detp -> Det N | Det adjp
Adjp -> Adj Adjp | Adj Conj Adjp | Adj NP
Advp -> VP Adv | Adv VP | V NP Adv
PP -> P NP


"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    sentence = nltk.tokenize.word_tokenize(sentence)
    new  =[]
    for word in sentence:
        alphabetic = False
        for letter in word:
            if letter.isalpha():
                alphabetic = True
        if alphabetic:
            new.append(word.lower())
    return new


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    np =[]
    sub = tree.subtrees()
    for each in sub:
        if each.label() == "NP":
            sub_sub = each.subtrees()
            check = []
            for every in sub_sub:
                check.append(every.label())
            check = check[1:]
            if not "NP" in check:
                np.append(each)

    return np


if __name__ == "__main__":
    main()
#t = Tree.fromstring("(S (NP (D the) (N dog)) (VP (V chased) (NP (D the) (N cat))))")
#print(np_chunk(t))
