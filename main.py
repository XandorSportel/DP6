from src.classes.Recept import Recept
from src.classes.Receptenboek import Receptenboek
from src.classes.Ingredient import Ingredient
from src.classes.Stap import Stap

# Globals
mijn_receptenboek = None

def init():
    global mijn_receptenboek

    # Maak een receptenboek aan
    mijn_receptenboek = Receptenboek()

    # Recept 1: Pannenkoeken
    pannenkoeken = Recept("Pannenkoeken", "Heerlijke Nederlandse pannenkoeken")
    pannenkoeken.voeg_ingredient_toe(Ingredient("Bloem", 200, "gram"))
    pannenkoeken.voeg_ingredient_toe(Ingredient("Melk", 300, "ml"))
    pannenkoeken.voeg_ingredient_toe(Ingredient("Eieren", 2, "stuks"))
    pannenkoeken.voeg_stap_toe(Stap("Meng de bloem, melk en eieren tot een glad beslag."))
    pannenkoeken.voeg_stap_toe(Stap("Verhit een beetje olie in een pan en bak de pannenkoeken aan beide kanten goudbruin."))

    mijn_receptenboek.voeg_recept_toe(pannenkoeken)

    # Recept 2:


    # Recept 3:

def main():
    init()

    print(mijn_receptenboek.get_recepten())

main()