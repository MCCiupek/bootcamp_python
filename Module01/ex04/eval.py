import sys

class Evaluator:
    @staticmethod
    def zip_evaluate(coef, words):
        if (len(words) != len(coef)):
            return -1
        return sum([len(word) * coef for word, coef in zip(words, coef)])
    
    @staticmethod
    def enumerate_evaluate(coef, words):
        if (len(words) != len(coef)):
            return -1
        return sum([len(words[i]) * coef for i, coef in enumerate(coef, start=0)])