import pandas as pd
import ipaddress
from sqlalchemy import create_engine
import pymysql

# Verbindung zur MySQL-Datenbank herstellen
db_user = 'root'
db_password = ''
db_host = 'localhost'
db_name = 'schulverwaltung'

# Erstelle eine SQLAlchemy-Engine
engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

# Dateinamen der CSV-Dateien
pfad_hostliste = 'hostliste.csv'

# Spalten, die ausgewählt werden sollen
desired_columns = ['Raumnummer', 'MAC', 'IP', 'Hostname']

def get_hostliste_from_db():
    # SQL-Abfrage zum Abrufen der Hostliste
    sql_query = "SELECT * FROM hostliste"
    hostliste = pd.read_sql(sql_query, engine)
    return hostliste

def filter_by_ip_range(dataframe, ip_start, ip_end):
    filtered_data = dataframe[dataframe['IP'].between(ip_start, ip_end)]
    return filtered_data

def show_important_data():
    hostliste = get_hostliste_from_db()
    formatted_data = hostliste[desired_columns].to_string(index=False)
    print(formatted_data)

def show_raum_data(raum):
    hostliste = get_hostliste_from_db()
    filtered_data = hostliste[hostliste['Raumnummer'] == raum][desired_columns]
    formatted_data = filtered_data.to_string(index=False)
    print(formatted_data)

def geraete_in_adressbereich(netzwerkpräfix):
    hostliste = get_hostliste_from_db()
    filtered_data = hostliste[hostliste['IP'].str.startswith(netzwerkpräfix)][desired_columns]
    formatted_data = filtered_data.to_string(index=False)
    print(formatted_data)

def get_freie_ip(adressbereich):
    hostliste = get_hostliste_from_db()

    ip_start, ip_end = map(str.strip, adressbereich.split('-'))

    # Konvertiere IP-Adressen in Objekte des Typs ipaddress.IPv4Address
    start_ip = ipaddress.IPv4Address(ip_start)
    end_ip = ipaddress.IPv4Address(ip_end)

    # Filtern der vorhandenen IP-Adressen im angegebenen Bereich
    vorhandene_ips = set(hostliste[
        hostliste['IP'].apply(lambda ip: start_ip <= ipaddress.IPv4Address(ip) <= end_ip)
    ]['IP'].astype(str))

    # Erstellen einer Menge aller IP-Adressen im Bereich
    alle_ips = set(ipaddress.IPv4Address(ip) for ip in range(int(start_ip), int(end_ip) + 1))

    # Finden der ersten freien IP-Adresse
    freie_ips = sorted(alle_ips - set(map(ipaddress.IPv4Address, vorhandene_ips)))

    if freie_ips:
        return str(freie_ips[0])
    else:
        return None

def neuer_eintrag(raumnummer, MAC, IP):
    # Angenommene Werte für die restlichen Spalten
    sql_query = "SELECT * FROM hostliste LIMIT 1"
    sample_entry = pd.read_sql(sql_query, engine)

    # Neuen Eintrag erstellen
    neuer_eintrag = pd.DataFrame({
        'Raumnummer': [raumnummer],
        'Hostname': [sample_entry['Hostname'][0]],
        'blubb': [sample_entry['blubb'][0]],
        'MAC': [MAC],
        'IP': [IP],
        'lupp': [sample_entry['lupp'][0]],
        'li': [sample_entry['li'][0]],
        'la': [sample_entry['la'][0]],
        'lala': [sample_entry['lala'][0]],
        'lu': [sample_entry['lu'][0]],
        'opsi': [sample_entry['opsi'][0]]
    })

    # Eintrag zur bestehenden Hostliste hinzufügen
    hostliste = get_hostliste_from_db()
    hostliste = pd.concat([hostliste, neuer_eintrag], ignore_index=True)

    # Eintrag in die Datenbank einfügen
    neuer_eintrag.to_sql('hostliste', engine, if_exists='append', index=False)

    print(f"Eintrag für Raum {raumnummer} wurde hinzugefügt.")

def eintraege_aus_csv_in_db_laden():
    pfad = input("Geben Sie den Pfad zur csv an")
    
    # CSV-Datei einlesen
    neue_eintraege = pd.read_csv(pfad, delimiter=';')

    # Einträge zur Datenbank hinzufügen
    neue_eintraege.to_sql('hostliste', engine, if_exists='append', index=False)

    print("Einträge aus CSV-Datei in die Datenbank geladen.")

def csv_hostliste_aus_db_generieren():
    # Daten aus der Datenbank abrufen
    hostliste = get_hostliste_from_db()

    # Sortieren nach Raumnummer
    hostliste_sorted = hostliste.sort_values(by='Raumnummer')

    # CSV-Datei erstellen und speichern
    hostliste_sorted.to_csv('hostliste_sorted.csv', sep=';', index=False)

    print("CSV-Datei aus der Datenbank generiert und nach Raumnummer sortiert.")

while True:
    eingabe = input('''
          Wählen Sie, was Sie tun möchten:
          a -> Anzeige aller Daten
          b -> Anzeige aller Geräte eines Raumes
          c -> Anzeige aller Geräte eines bestimmten Adressbereichs
          d -> Ermittlung freier IP-Adresse bei einem vorgegebenen Adressbereich
          e -> Erzeugen Sie einen neuen Eintrag durch Eingabe von Raumnummer, MAC-Adresse und IP-Adresse
          f -> Erzeugen Sie mehrere Einträge durch Einlesen einer CSV-Datei, welche die entsprechenden Daten enthält
          g -> Erzeugen Sie eine neue Hostliste aus der Datenbank sortiert nach der Raumnummer. 
          h -> quit
          ''')
    if eingabe == 'a':
        show_important_data()
    if eingabe == 'b':
        raum = input("Geben Sie den gewünschten Raum ein: ")
        show_raum_data(raum)
    if eingabe == 'c':
        adressbereich = input("Geben Sie den Adressbereich an: ")
        geraete_in_adressbereich(adressbereich)
    if eingabe == 'd':
        print("Geben Sie den Adressbereich im Format 'start_ip-end_ip' ein.")
        adressbereich = input("Beispiel: 192.168.1.1-192.168.1.255\nGeben Sie den Adressbereich an: ")

        freie_ip = get_freie_ip(adressbereich)

        if freie_ip:
            print(f"Die erste freie IP-Adresse im Adressbereich {adressbereich} ist: {freie_ip}")
        else:
            print(f"Es gibt keine freien IP-Adressen im Adressbereich {adressbereich}")
    if eingabe == 'e':
        raumnummer = input("Geben Sie die Raumnummer ein: ")
        MAC = input("Geben Sie die MAC-Adresse ein: ")
        IP = input("Geben Sie die IP-Adresse ein: ")

        neuer_eintrag(raumnummer, MAC, IP)
    if eingabe == 'f':
        eintraege_aus_csv_in_db_laden()
    if eingabe == 'g':
        csv_hostliste_aus_db_generieren()
    if eingabe == 'h':
        break

# Verbindung zur Datenbank schließen
engine.dispose()
