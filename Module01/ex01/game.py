import sys


class GotCharacter:
    def __init__(self, first_name, is_alive=True):
        """Init GotCharacter Class"""
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        """Init Stark Class"""
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        """Prints to screen the House words"""
        print(self.house_words)

    def die(self):
        """Changes the value of is_alive to False"""
        self.is_alive = False
