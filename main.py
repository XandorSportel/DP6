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

    user_input = input("Welk recept wil je zien? (Typ het nummer): ")
    try:
        index = int(user_input) - 1
        recept_namen = list(mijn_receptenboek.recepten.keys())
        if 0 <= index < len(recept_namen):
            gekozen_recept = mijn_receptenboek.get_recept(recept_namen[index])
            print(gekozen_recept)
        else:
            print("Ongeldige keuze.")
    except ValueError:
        print("Voer alstublieft een geldig nummer in.")

main()