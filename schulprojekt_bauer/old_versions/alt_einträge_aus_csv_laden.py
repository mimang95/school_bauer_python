# def eintraege_aus_csv_in_db_laden():
#     pfad = input("Geben Sie den Pfad zur CSV-Datei an: ")

#     # CSV-Datei einlesen
#     neue_eintraege = pd.read_csv(pfad, delimiter=';')

#     # Angenommene Werte für die restlichen Spalten
#     sql_query = "SELECT * FROM hostliste LIMIT 1"
#     sample_entry = pd.read_sql(sql_query, engine)

#     # Extrahiere die letzte Zahl in der IP-Adresse und erstelle den Hostnamen
#     neue_eintraege['letzte_zahl_ip'] = neue_eintraege['IP'].apply(lambda x: int(x.split('.')[-1]))
#     neue_eintraege['Hostname'] = neue_eintraege.apply(lambda row: f"{row['Raumnummer']}nb{row['letzte_zahl_ip']}", axis=1)

#     # Setze den festen Wert für 'lala'
#     neue_eintraege['lala'] = 'classroom-studentcomputer'

#     # Wähle nur die relevanten Spalten aus, die in der Datenbank vorhanden sind
#     relevante_spalten = ['Raumnummer', 'Hostname', 'MAC', 'IP', 'lala']
#     neue_eintraege = neue_eintraege[relevante_spalten]

#     # Einträge zur Datenbank hinzufügen
#     neue_eintraege.to_sql('hostliste', engine, if_exists='append', index=False)

#     print(f"Einträge aus CSV-Datei in die Datenbank geladen. Hostnamen wurden entsprechend generiert.")