class Stap:
    def __init__(self, beschrijving, tip=None):
        self.__beschrijving = beschrijving
        self.__tip = tip

    def __str__(self):
        if self.__tip:
            return f"{self.__beschrijving} (Tip: {self.__tip})"
        return self.__beschrijving