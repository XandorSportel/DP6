from src.helpers.formatter import color
from src.console.Colors import Colors

class Stap:
    def __init__(self, beschrijving, tip=None):
        self.__beschrijving = beschrijving
        self.__tip = tip

    def get_beschrijving(self):
        return self.__beschrijving
    
    def get_tip(self):
        return self.__tip

    def __str__(self):
        if self.__tip:
            return f"{self.__beschrijving} ({color('Tip:', Colors.INFO)} {self.__tip})"
        return self.__beschrijving