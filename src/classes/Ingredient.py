class Ingredient:
    def __init__(self, naam, hoeveelheid, eenheid, kcal):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__kcal = kcal
        self.__plantaardig_alternatief = None

    def get_naam(self):
        return self.__naam

    def get_hoeveelheid(self):
        return self.__hoeveelheid
    
    def get_eenheid(self):
        return self.__eenheid
    
    def get_kcal(self):
        return self.__kcal
    
    def heeft_plantaardig_alternatief(self):
        return self.__plantaardig_alternatief
    
    def get_ingredient(self, plantaardig):
        if plantaardig and self.__plantaardig_alternatief is not None:
            return self.__plantaardig_alternatief
        return self
    
    def set_hoeveelheid(self, hoeveelheid):
        self.__hoeveelheid = hoeveelheid

    def set_plantaardig_alternatief(self, alternatief):
        self.__plantaardig_alternatief = alternatief

    def set_kcal(self, kcal):
        self.__kcal = kcal

    def __str__(self):
        eenheid = self.__eenheid
        if (self.__eenheid == 'stuk' or self.__eenheid == 'snufje') and self.__hoeveelheid > 1:
            eenheid = self.__eenheid + 's'

        return f"{self.__hoeveelheid} {eenheid} {self.__naam} ({self.__kcal} kcal)"