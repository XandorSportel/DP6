from src.classes.Recept import Recept
from src.classes.Receptenboek import Receptenboek
from src.classes.Ingredient import Ingredient
from src.classes.Stap import Stap

from src.helpers.formatter import color
from src.console.Colors import Colors

# Globals
mijn_receptenboek = None

def init():
    global mijn_receptenboek

    # Maak een receptenboek aan
    mijn_receptenboek = Receptenboek()

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

def vraag_recept_index():
    while True:
        try:
            keuze = int(input(f"Welk recept wil je zien? (Typ het nummer): "))
            return keuze - 1
        except ValueError:
            print(f"Voer alstublieft een geldig nummer in.")

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

    print(mijn_receptenboek.get_recepten())

    index = vraag_recept_index()
    recept_namen = list(mijn_receptenboek.recepten.keys())

    if 0 <= index < len(recept_namen):
        gekozen_recept = mijn_receptenboek.get_recept(recept_namen[index])

        personen = vraag_aantal_personen()
        gekozen_recept.set_aantal_personen(personen)

        plantaardig = vraag_plantaardig()
        gekozen_recept.set_plantaardig(plantaardig)

        print("\n" + str(gekozen_recept))
    else:
        print(f"{Colors.ERROR}Ongeldige keuze.{Colors.RESET}")

main()