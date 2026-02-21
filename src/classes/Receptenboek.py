class Receptenboek:
    def __init__(self):
        self.recepten = {}

    def voeg_recept_toe(self, recept):
        self.recepten[recept.get_naam()] = recept

    def get_recept(self, naam):
        return self.recepten.get(naam, "Recept niet gevonden")
    
    def get_recepten(self):
        recepten = "\n".join(f"[{index+1}] {recept.get_naam()} - {recept.get_omschrijving()}" for index, recept in enumerate(self.recepten.values()))
        return f"Recepten in het boek:\n{recepten}"

    def verwijder_recept(self, naam):
        if naam in self.recepten:
            del self.recepten[naam]
            return f"Recept '{naam}' verwijderd."
        else:
            return "Recept niet gevonden"