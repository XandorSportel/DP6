import mysql.connector
import os
from dotenv import load_dotenv

class Database:
    def __init__(self):
        load_dotenv()

        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS recepten (
                id INT AUTO_INCREMENT PRIMARY KEY,
                naam VARCHAR(255) UNIQUE,
                omschrijving TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ingredienten (
                id INT AUTO_INCREMENT PRIMARY KEY,
                recept_id INT,
                naam VARCHAR(255),
                hoeveelheid FLOAT,
                eenheid VARCHAR(100),
                kcal INT,
                alternatief_naam VARCHAR(255),
                alternatief_hoeveelheid FLOAT,
                alternatief_eenheid VARCHAR(100),
                alternatief_kcal INT,
                FOREIGN KEY (recept_id) REFERENCES recepten(id)
                ON DELETE CASCADE
            )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS stappen (
            id INT AUTO_INCREMENT PRIMARY KEY,
            recept_id INT,
            beschrijving TEXT,
            tip TEXT,
            FOREIGN KEY (recept_id) REFERENCES recepten(id)
            ON DELETE CASCADE
        )
        """)

        self.connection.commit()
        