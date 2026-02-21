from src.console.Colors import Colors

class Receptenboek:
    def __init__(self):
        self.recepten = {}

    def voeg_recept_toe(self, recept):
        self.recepten[recept.get_naam()] = recept

    def get_recept(self, naam):
        return self.recepten.get(naam, Colors.WARNING + "Recept niet gevonden" + Colors.RESET)
    
    def get_recepten(self):
        recepten = "\n".join(f"{Colors.OK}{Colors.BOLD}[{index+1}]{Colors.RESET} {recept.get_naam()} - {recept.get_omschrijving()}" for index, recept in enumerate(self.recepten.values()))
        return f"{Colors.HEADER}Recepten in het boek:{Colors.RESET}\n{recepten}"

    def verwijder_recept(self, naam):
        if naam in self.recepten:
            del self.recepten[naam]
            return f"Recept '{naam}' verwijderd."
        else:
            return Colors.WARNING + "Recept niet gevonden" + Colors.RESET