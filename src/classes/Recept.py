class Recept:
    def __init__(self, naam, omschrijving):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredienten = []
        self.__stappen = []

    def get_naam(self):
        return self.__naam
    
    def get_ingredienten(self):
        return self.__ingredienten
    
    def get_stappen(self):
        return self.__stappen
    
    def voeg_ingredient_toe(self, ingredient):
        self.__ingredienten.append(ingredient)

    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)

    def __str__(self):
        return f"Recept: {self.__naam}\nOmschrijving: {self.__omschrijving}\nIngredienten: {', '.join(self.__ingredienten)}\nStappen: {'; '.join(self.__stappen)}"