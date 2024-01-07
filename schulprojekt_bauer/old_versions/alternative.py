import pandas as pd
from sqlalchemy import create_engine

# MySQL Verbindungsinformationen
db_user = 'root'
db_password = ''
db_host = 'localhost'
db_name = 'schulverwaltung'

# SQLAlchemy Verbindung erstellen
engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}')

# Dateinamen der CSV-Dateien
pfad_hostliste = 'hostliste.csv'
table_name = 'hostliste'

# Einlesen der CSV-Dateien
hostliste = pd.read_csv(pfad_hostliste, delimiter=';')

# Extrahiere die Raumnummer und Hostname aus der Hostname-Spalte
hostliste[['Raumnummer', 'Hostname']] = hostliste['Hostname'].str.extract(r'(\D+)(\d+)', expand=True).fillna('unknown')

# Leere Werte in der gesamten DataFrame behandeln
hostliste.fillna('unknown', inplace=True)

# Überprüfen auf leere Werte
print("Leere Werte in DataFrame:")
print(hostliste.isnull().sum())

# Schreiben Sie den DataFrame in die MySQL-Datenbank
hostliste.to_sql(table_name, engine, if_exists='replace', index=False)

print(f"Die Daten wurden in die Tabelle {table_name} der Datenbank geschrieben.")
