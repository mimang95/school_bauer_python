import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# MySQL-Datenbankkonfiguration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'schulverwaltung'
}

# CSV-Dateipfad
csv_file_path = 'schulprojekt_bauer/hostliste.csv'

# Daten aus CSV-Datei lesen und den Header automatisch erkennen
data = pd.read_csv(csv_file_path, sep=';', header=0, skiprows=[])

# Mit MySQL-Datenbank verbinden
engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")
conn = engine.connect()

# Tabelle erstellen (falls sie nicht bereits existiert)
data.to_sql(name='hostliste', con=engine, if_exists='replace', index=False)

# Verbindung schließen
conn.close()

print("Die Tabelle 'hostliste' wurde erfolgreich erstellt und mit Daten aus der CSV-Datei gefüllt.")
