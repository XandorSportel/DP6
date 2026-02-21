from src.console.Colors import Colors

class Recept:
    def __init__(self, naam, omschrijving, aantal_personen=1):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__aantal_personen = aantal_personen
        self.__ingredienten = []
        self.__stappen = []
        self.__plantaardig = False

    def get_naam(self):
        return self.__naam
    
    def get_omschrijving(self):
        return self.__omschrijving
    
    def get_aantal_personen(self):
        return self.__aantal_personen
    
    def get_ingredienten(self):
        return self.__ingredienten        
    
    def get_stappen(self):
        return self.__stappen
    
    def set_aantal_personen(self, personen):
        factor = personen / self.__aantal_personen

        for ingredient in self.__ingredienten:
            nieuwe_hoeveelheid = ingredient.get_hoeveelheid() * factor
            ingredient.set_hoeveelheid(nieuwe_hoeveelheid)

            nieuwe_kcal = ingredient.get_kcal() * factor
            ingredient.set_kcal(nieuwe_kcal)

        self.__aantal_personen = personen

    def set_plantaardig(self, plantaardig):
        self.__plantaardig = plantaardig
    
    def voeg_ingredient_toe(self, ingredient):
        self.__ingredienten.append(ingredient)

    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)

    def __str__(self):
        ingredienten = "\n".join(
            f"• {str(index.get_ingredient(self.__plantaardig))}"
            for index in self.__ingredienten
        )
        stappen = "\n".join(f"{index+1}. {str(stap)}" for index, stap in enumerate(self.__stappen))
    
        return (
            f"{Colors.INFO}Recept: {Colors.RESET}{self.__naam}\n"
            f"{Colors.INFO}Omschrijving: {Colors.RESET}{self.__omschrijving}\n"
            f"{Colors.INFO}Aantal personen: {Colors.RESET}{self.__aantal_personen}\n\n"
            f"{Colors.INFO}Ingredienten: {Colors.RESET}\n{ingredienten}\n\n"
            f"{Colors.INFO}Stappen: {Colors.RESET}\n{stappen}\n"
        )