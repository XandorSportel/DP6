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
    # Zet load_from_db op True om recepten uit de database te laden, of op False om met lege receptenboek te starten en handmatig recepten toe te voegen
    laad_uit_db = False
    mijn_receptenboek = Receptenboek(load_from_db=laad_uit_db)

    if laad_uit_db == False:
        # Recept 1: Pannenkoeken
        recept1 = Recept("Pannenkoeken", "Heerlijke Nederlandse pannenkoeken")
        recept1.voeg_ingredient_toe(Ingredient("Koopmans Pannenkoekmeel Kabouter", 500, "gram", 890))
        recept1.voeg_ingredient_toe(Ingredient("Melk", 1000, "ml", 650))
        recept1.voeg_ingredient_toe(Ingredient("Eieren", 2, "stuks", 140))
        recept1.voeg_ingredient_toe(Ingredient("Zout", 1, "snufje", 0))

        recept1.voeg_stap_toe(Stap("Doe 500 gram van het meel in een beslagkom en voeg de melk, de eieren en het zout toe.", "Je kunt ook een beetje kaneel toevoegen voor extra smaak!"))
        recept1.voeg_stap_toe(Stap("Roer het geheel met een garde of mixer tot een glad beslag."))
        recept1.voeg_stap_toe(Stap("Verhit een klontje boter of een scheutje olie in een koekenpan."))
        recept1.voeg_stap_toe(Stap("Giet wat beslag in de pan, laat het uitlopen over de bodem en bak de pannenkoeken aan beide zijden goudbruin."))
        recept1.voeg_stap_toe(Stap("Herhaal dit totdat al het beslag op is."))

        mijn_receptenboek.voeg_recept_toe(recept1)

        # Recept 2: Kip Rendang
        recept2 = Recept("Kip Rendang", "Een smaakvol Indonesisch gerecht")

        # Vegetarisch alternatief voor kip
        kip = Ingredient("Kip", 300, "gram", 600)
        veg_kip = Ingredient("Vegetarische kipstukjes", 300, "gram", 450)

        kip.set_plantaardig_alternatief(veg_kip)

        recept2.voeg_ingredient_toe(kip)
        recept2.voeg_ingredient_toe(Ingredient("Kokosmelk", 200, "ml", 400))
        recept2.voeg_ingredient_toe(Ingredient("Stengel citroengras", 1, "stuk", 5))
        recept2.voeg_ingredient_toe(Ingredient("Ui", 1, "stuk", 40))
        recept2.voeg_ingredient_toe(Ingredient("Knoflook", 2, "tenen", 10))
        recept2.voeg_ingredient_toe(Ingredient("Gember", 1, "stuk", 5))
        recept2.voeg_ingredient_toe(Ingredient("Ketjap manis", 25, "ml", 70))
        recept2.voeg_ingredient_toe(Ingredient("Komijn", 1, "tl", 8))
        recept2.voeg_ingredient_toe(Ingredient("Koriander", 1, "tl", 5))
        recept2.voeg_ingredient_toe(Ingredient("Zout en peper", 1, "snufje", 0))

        recept2.voeg_stap_toe(Stap("Schil de gember en snijd vervolgens in kleine stukjes. Snipper de uit, snijd de tenen knoflook fijn en snijd de sereh in stukken."))
        recept2.voeg_stap_toe(Stap("Doe vervolgens de gember, ui, knoflook en sereh samen met de rode peper, koriander, komijn en een scheutje olijfolie in een keukenmachine. Hak alles tot er een soort kruidenpasta overblijft."))
        recept2.voeg_stap_toe(Stap("Snijd vervolgens de kipfilet in stukjes en breng op smaak met een klein beetje zout en peper."))
        recept2.voeg_stap_toe(Stap("Doe een klein klontje boter in een braadpan en bak de kruidenpasta voor een minuut of 2-3."))
        recept2.voeg_stap_toe(Stap("Voeg vervolgens de kip toe en bak deze rondom bruin."))
        recept2.voeg_stap_toe(Stap("Voeg de kokosmelk en de ketjap toe. Zet een deksel schuin op de pan en laat de rendang ajam zachtjes pruttelen, ongeveer 30-45 minuten totdat de ‘saus’ is ingedikt."))
        recept2.voeg_stap_toe(Stap("Kook ondertussen nog lekker wat rijst en groente."))

        mijn_receptenboek.voeg_recept_toe(recept2)

        # Recept 3: Broodje Hamburger
        recept3 = Recept("Broodje Hamburger", "Een lekker broodje hamburger")
        recept3.voeg_ingredient_toe(Ingredient("Hamburgerbroodje", 2, "stuks", 300))
        recept3.voeg_ingredient_toe(Ingredient("Hamburger", 2, "stuks", 500))
        recept3.voeg_ingredient_toe(Ingredient("Mayo", 1, "el", 100))
        recept3.voeg_ingredient_toe(Ingredient("Curry", 1, "el", 50))
        recept3.voeg_ingredient_toe(Ingredient("Ui", 0.5, "stuk", 40))

        recept3.voeg_stap_toe(Stap("Snijd de ui in ringen en bak deze in een pan met een beetje olie totdat ze goudbruin zijn."))
        recept3.voeg_stap_toe(Stap("Bak de hamburgers in een pan of op de grill totdat ze gaar zijn."))
        recept3.voeg_stap_toe(Stap("Meng de mayo en curry door elkaar om een saus te maken."))
        recept3.voeg_stap_toe(Stap("Snijd de hamburgerbroodjes doormidden en rooster ze lichtjes."))
        recept3.voeg_stap_toe(Stap("Beleg de onderste helft van het broodje met de hamburger, ui en saus. Leg de bovenste helft van het broodje erop en serveer."))

        mijn_receptenboek.voeg_recept_toe(recept3)

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