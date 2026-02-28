from src.console.Colors import Colors
from src.database.recept_repository import ReceptRepository
from src.helpers.formatter import color

class Receptenboek:
    def __init__(self, load_from_db=False):
        self.repository = ReceptRepository()
        self.recepten = {}
        self.load_from_db = load_from_db
        if load_from_db:
            self.load_from_database()

    def load_from_database(self):
        recepten = self.repository.get_all()
        for recept in recepten:
            self.recepten[recept.get_naam()] = recept

    def voeg_recept_toe(self, recept):
        if recept.get_naam() not in self.recepten:
            if self.load_from_db:
                self.repository.save(recept)
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
        success = self.repository.delete(naam)

        if success:
            if naam in self.recepten:
                del self.recepten[naam]
            return f"Recept '{naam}' verwijderd."
        else:
            return color("Recept niet gevonden in database.", Colors.WARNING)