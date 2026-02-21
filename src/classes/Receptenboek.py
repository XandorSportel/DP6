from src.helpers.formatter import color
from src.console.Colors import Colors

class Receptenboek:
    def __init__(self):
        self.recepten = {}

    def voeg_recept_toe(self, recept):
        self.recepten[recept.get_naam()] = recept

    def get_recept(self, naam):
        return self.recepten.get(naam, color("Recept niet gevonden", Colors.WARNING))
    
    def get_recepten(self):
        recepten = "\n".join(f"{Colors.OK}{Colors.BOLD}[{index+1}]{Colors.RESET} {recept.get_naam()} - {recept.get_omschrijving()}" for index, recept in enumerate(self.recepten.values()))
        return (
            f"{color('Recepten in het boek:', Colors.HEADER)}\n{recepten}"
            f"\n{color('[' + str(len(self.recepten) + 1) + ']', Colors.WARNING)} Terug naar hoofdmenu"
        )

    def verwijder_recept(self, naam):
        if naam in self.recepten:
            del self.recepten[naam]
            return f"Recept '{naam}' verwijderd."
        else:
            return color("Recept niet gevonden", Colors.WARNING)