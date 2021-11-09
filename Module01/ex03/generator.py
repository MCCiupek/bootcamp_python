import sys
import random

available_opt = ["shuffle", "unique", "ordered"]


def generator(text, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""
    try:
        if not isinstance(text, str):
            raise ValueError
        words = text.split(sep)
        if option is None:
            for word in words:
                yield word
        elif option is "shuffle":
            while len(words) > 0:
                word = words[random.randint(0, len(words) - 1)]
                words.remove(word)
                yield word
        elif option is "unique":
            found_words = []
            for word in words:
                if word not in found_words:
                    yield word
                    found_words.append(word)
        elif option is "ordered":
            words = sorted(words, key=str.lower)
            for word in words:
                yield word
        else:
            raise ValueError
    except ValueError as err:
        print("ERROR")
        return
