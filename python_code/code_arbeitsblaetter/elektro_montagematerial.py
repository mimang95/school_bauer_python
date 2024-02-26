import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:@localhost/montage')

csv_dateipfad = 'python_code/code_arbeitsblaetter/montage.csv'
artikel_tabelle = 'artikel'
gruppe_tabelle = 'gruppe'

data = pd.read_csv(csv_dateipfad, delimiter=';')

print(data.columns)

gruppen_data = data[['Gruppe']].rename(columns={'Gruppe': 'Bezeichnung'})
print(gruppen_data)

artikel_data = data[['Nr', 'Bezeichnung', 'Preis']].rename(columns={'Nr': 'Nr', 'Bezeichnung': 'Bezeichnung', 'Preis': 'Preis'})

# Tabelle 'gruppe' erstellen, wenn sie noch nicht existiert
engine.execute(f"CREATE TABLE IF NOT EXISTS {gruppe_tabelle} (GID INT AUTO_INCREMENT PRIMARY KEY, Bezeichnung VARCHAR(255));")

# Daten in die MySQL-Datenbank für 'gruppe' schreiben
gruppen_data.to_sql(gruppe_tabelle, con=engine, if_exists='append', index=False)

# Hole die GID-Werte für die Artikel-Daten
artikel_data['GID'] = artikel_data['Bezeichnung'].map(lambda x: engine.execute(f"SELECT GID FROM {gruppe_tabelle} WHERE Bezeichnung = '{x}'").scalar())

# Tabelle 'artikel' erstellen, wenn sie noch nicht existiert
engine.execute(f"CREATE TABLE IF NOT EXISTS {artikel_tabelle} (Nr INT, Bezeichnung VARCHAR(255), Preis FLOAT, GID INT, PRIMARY KEY (Nr));")

# Daten in die MySQL-Datenbank für 'artikel' schreiben
artikel_data.to_sql(artikel_tabelle, con=engine, if_exists='append', index=False)

engine.dispose()