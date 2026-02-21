from src.database.database import Database
from src.classes.Recept import Recept
from src.classes.Ingredient import Ingredient
from src.classes.Stap import Stap

class ReceptRepository:
    def __init__(self):
        self.db = Database()

    def save(self, recept):
        cursor = self.db.connection.cursor(dictionary=True)

        cursor.execute(
            "INSERT INTO recepten (naam, omschrijving) VALUES (%s, %s)",
            (recept.get_naam(), recept.get_omschrijving())
        )
        recept_id = cursor.lastrowid

        # Save ingredients
        for ingredient in recept.get_ingredienten():
            alternatief = ingredient.heeft_plantaardig_alternatief()

            cursor.execute("""
                INSERT INTO ingredienten 
                (recept_id, naam, hoeveelheid, eenheid, kcal,
                alternatief_naam, alternatief_hoeveelheid,
                alternatief_eenheid, alternatief_kcal)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                recept_id,
                ingredient.get_naam(),
                ingredient.get_hoeveelheid(),
                ingredient.get_eenheid(),
                ingredient.get_kcal(),
                alternatief.get_naam() if alternatief else None,
                alternatief.get_hoeveelheid() if alternatief else None,
                alternatief.get_eenheid() if alternatief else None,
                alternatief.get_kcal() if alternatief else None
            ))

        # Save steps
        for stap in recept.get_stappen():
            cursor.execute("""
                INSERT INTO stappen (recept_id, beschrijving, tip)
                VALUES (%s, %s, %s)
            """, (
                recept_id,
                stap.get_beschrijving(),
                stap.get_tip()
            ))

        self.db.connection.commit()

    def delete(self, naam: str):
        cursor = self.db.connection.cursor()

        cursor.execute(
            "DELETE FROM recepten WHERE naam = %s",
            (naam,)
        )

        self.db.connection.commit()

        return cursor.rowcount > 0

    def get_all(self):
        cursor = self.db.connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM recepten")
        recepten_data = cursor.fetchall()

        recepten = []

        for r in recepten_data:
            recept = Recept(r["naam"], r["omschrijving"])

            # Ingredients
            cursor.execute("SELECT * FROM ingredienten WHERE recept_id = %s", (r["id"],))
            ingredients = cursor.fetchall()

            for i in ingredients:
                ingredient = Ingredient(i["naam"], i["hoeveelheid"], i["eenheid"], i["kcal"])

                if i["alternatief_naam"]:
                    alternatief = Ingredient(
                        i["alternatief_naam"],
                        i["alternatief_hoeveelheid"],
                        i["alternatief_eenheid"],
                        i["alternatief_kcal"]
                    )
                    ingredient.set_plantaardig_alternatief(alternatief)

                recept.voeg_ingredient_toe(ingredient)

            # Steps
            cursor.execute("SELECT * FROM stappen WHERE recept_id = %s", (r["id"],))
            stappen = cursor.fetchall()

            for s in stappen:
                recept.voeg_stap_toe(Stap(s["beschrijving"], s["tip"]))

            recepten.append(recept)

        return recepten