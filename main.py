from src.classes.Recept import Recept
from src.classes.Receptenboek import Receptenboek
from src.classes.Ingredient import Ingredient
from src.classes.Stap import Stap

from src.console.Colors import Colors
from src.helpers.formatter import color
from src.helpers.pdf_generator import genereer_recept_pdf

# Globals
mijn_receptenboek = None

def init():
    global mijn_receptenboek

    # Maak een receptenboek aan
    mijn_receptenboek = Receptenboek()

def toon_keuzemenu():
    print("\n" + f"{color('='*20, Colors.INFO)} {color('Opties', Colors.HEADER)} {color('='*20, Colors.INFO)}")
    print(f"{color('1', Colors.OK)}. Toon overzicht recepten")
    print(f"{color('2', Colors.OK)}. Voeg nieuw recept toe")
    print(f"{color('3', Colors.OK)}. Exit")
    print(f"{color('='*48, Colors.INFO)}")

def toon_overzicht():
    print("\n" + mijn_receptenboek.get_recepten())

    index = vraag_recept_index()
    recept_namen = list(mijn_receptenboek.recepten.keys())

    if 0 <= index < len(recept_namen):
        gekozen_recept = mijn_receptenboek.get_recept(recept_namen[index])

        personen = vraag_aantal_personen()
        gekozen_recept.set_aantal_personen(personen)

        plantaardig = vraag_plantaardig()
        gekozen_recept.set_plantaardig(plantaardig)

        print("\n" + str(gekozen_recept))

        print("\n" + f"{color('='*20, Colors.INFO)} {color('Opties', Colors.HEADER)} {color('='*20, Colors.INFO)}")
        print(f"{color('1', Colors.ERROR)}. Verwijder dit recept")
        print(f"{color('2', Colors.INFO)}. Genereer PDF van dit recept")
        print(f"{color('3', Colors.OK)}. Terug naar overzicht")
        print(f"{color('='*48, Colors.INFO)}")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            bevestig = input(f"Weet je het zeker? ({color('ja', Colors.OK)}/{color('nee', Colors.ERROR)}): ").lower()
            if bevestig == "ja":
                mijn_receptenboek.verwijder_recept(gekozen_recept.get_naam())
                print(color("Recept verwijderd.", Colors.OK))

        elif keuze == "2":
            bestandnaam = f"{gekozen_recept.get_naam().replace(' ', '_')}.pdf"
            genereer_recept_pdf(gekozen_recept, bestandnaam)
            print(color(f"PDF gegenereerd: {bestandnaam}", Colors.OK))

    elif index == len(recept_namen):
        return
    
    else:
        print(color("Ongeldige keuze.", Colors.ERROR))

def voeg_recept_toe_via_input():
    print(f"\n{color('Nieuw recept toevoegen', Colors.HEADER)}")

    naam = input("Naam recept: ")
    omschrijving = input("Omschrijving: ")

    nieuw_recept = Recept(naam, omschrijving)

    # Ingredient loop
    while True:
        voeg_ingredient = input(f"Ingrediënt toevoegen? ({color('ja', Colors.OK)}/{color('nee', Colors.ERROR)}): ").lower()
        if voeg_ingredient != "ja":
            break

        ingredient_naam = input("Naam ingrediënt: ")
        hoeveelheid = None
        try:
            hoeveelheid = float(input("Hoeveelheid: "))
        except ValueError:
            print(color("Ongeldige hoeveelheid. Probeer het opnieuw.", Colors.ERROR))
            continue
        eenheid = input("Eenheid: ")
        kcal = None
        try:
            kcal = int(input("Aantal kcal: "))
        except ValueError:
            print(color("Ongeldige kcal waarde. Probeer het opnieuw.", Colors.ERROR))
            continue

        ingredient = Ingredient(ingredient_naam, hoeveelheid, eenheid, kcal)

        # Plantaardig alternatief
        alternatief_keuze = input(f"Plantaardig alternatief toevoegen? ({color('ja', Colors.OK)}/{color('nee', Colors.ERROR)}): ").lower()
        if alternatief_keuze == "ja":
            alternatief_naam = input("Naam alternatief: ")
            alternatief_hoeveelheid = None
            try:
                alternatief_hoeveelheid = float(input("Hoeveelheid alternatief: "))
            except ValueError:
                print(color("Ongeldige hoeveelheid. Probeer het opnieuw.", Colors.ERROR))
                continue
            alternatief_eenheid = input("Eenheid alternatief: ")
            alternatief_kcal = int(input("Aantal kcal alternatief: "))

            alternatief = Ingredient(alternatief_naam, alternatief_hoeveelheid, alternatief_eenheid, alternatief_kcal)
            ingredient.set_plantaardig_alternatief(alternatief)

        nieuw_recept.voeg_ingredient_toe(ingredient)

    # Steps loop
    while True:
        voeg_stap = input(f"Stap toevoegen? ({color('ja', Colors.OK)}/{color('nee', Colors.ERROR)}): ").lower()
        if voeg_stap != "ja":
            break

        beschrijving = input("Beschrijving stap: ")
        tip = input("Tip (optioneel, druk Enter om over te slaan): ")

        if tip == "":
            nieuw_recept.voeg_stap_toe(Stap(beschrijving))
        else:
            nieuw_recept.voeg_stap_toe(Stap(beschrijving, tip))

    mijn_receptenboek.voeg_recept_toe(nieuw_recept)

    print(color("Recept succesvol toegevoegd.", Colors.OK))
    print("\n" + str(nieuw_recept))

def vraag_recept_index():
    while True:
        try:
            keuze = int(input(f"Welk recept wil je zien? (Typ het nummer): "))
            return keuze - 1
        except ValueError:
            print(f"{color('Voer alstublieft een geldig nummer in.', Colors.ERROR)}")

def vraag_aantal_personen():
    invoer = input(
        f"Voor hoeveel personen wil je het recept aanpassen? "
        f"(Druk {color('Enter', Colors.WARNING)} voor {color('1', Colors.WARNING)} persoon): "
    )

    if invoer == "":
        return 1

    try:
        personen = int(invoer)
        if personen > 0:
            return personen
    except ValueError:
        pass

    print(f"{color('Ongeldige invoer. Recept wordt voor 1 persoon weergegeven.', Colors.WARNING)}")
    return 1

def vraag_plantaardig():
    while True:
        invoer = input(f"Wil je een plantaardig alternatief? ({color('ja', Colors.OK)}/{color('nee', Colors.ERROR)}): ").lower()

        if invoer in ["ja", "nee"]:
            return invoer == "ja"

        print(f"{color('Ongeldige invoer. Typ \'ja\' of \'nee\'.', Colors.WARNING)}")

def main():
    init()

    while True:
        toon_keuzemenu()
        keuze = input("Maak een keuze: ")

        if keuze == "1":
            toon_overzicht()
        elif keuze == "2":
            voeg_recept_toe_via_input()
        elif keuze == "3":
            print(f"{color('Programma afgesloten.', Colors.OK)}")
            break
        else:
            print(color("Ongeldige keuze.", Colors.ERROR))

main()