class Ingredient:
    def __init__(self, naam, hoeveelheid, eenheid):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid

    def __str__(self):
        return f"{self.__hoeveelheid} {self.__eenheid} {self.__naam}"