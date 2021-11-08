import string

def text_analyzer(s=None, s2=None):
    """This function counts the number of upper characters, \
lower characters, punctuation and spaces in a given text."""
    if s2 is not None:
        print("ERROR")
        return
    if s is None:
        s = input("What is the text to analyse?\n")
    print("The text contains {0} characters:".format(len(s)))
    print("-", sum(1 for c in s if c.isupper()), "upper letters")
    print("-", sum(1 for c in s if c.islower()), "lower letters")
    print("-", sum(1 for c in s if c in string.punctuation), "punctuation marks")
    print("-", sum(1 for c in s if c.isspace()), "spaces")