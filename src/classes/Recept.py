class Recept:
    def __init__(self, naam, omschrijving):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredienten = []
        self.__stappen = []

    def get_naam(self):
        return self.__naam
    
    def get_beschrijving(self):
        return self.__omschrijving
    
    def get_ingredienten(self):
        return self.__ingredienten
    
    def get_stappen(self):
        return self.__stappen
    
    def voeg_ingredient_toe(self, ingredient):
        self.__ingredienten.append(ingredient)

    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)

    def __str__(self):
        ingredienten = "\n".join(f"• {str(i)}" for i in self.__ingredienten)
        stappen = "\n".join(f"{i+1}. {str(s)}" for i, s in enumerate(self.__stappen))
    
        return (
            f"Recept: {self.__naam}\n"
            f"Omschrijving: {self.__omschrijving}\n\n"
            f"Ingredienten: \n{ingredienten}\n\n"
            f"Stappen: \n{stappen}"
        )