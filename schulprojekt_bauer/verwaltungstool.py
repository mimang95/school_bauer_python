import pandas as pd
import ipaddress
from sqlalchemy import create_engine
import csv
import pymysql
from datetime import datetime
import os
import re

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

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def is_valid_mac(mac):
    mac_pattern = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
    return bool(mac_pattern.match(mac))

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

    # Extrahiere die letzte Zahl in der IP-Adresse
    letzte_zahl_ip = int(IP.split('.')[-1])

    # Erstelle den Hostnamen basierend auf der Raumnummer und der letzten Zahl in der IP-Adresse
    hostname = f"{raumnummer}nb{letzte_zahl_ip}"
    hostname = input("Geben Sie den Hostnamen ein: ")
    hardwaregruppe = input("Geben Sie die Hardwaregruppe ein: ")
    lupp = None
    li = 1
    la = 1
    lala = 'classroom-studentcomputer'
    lu = 1
    opsi = 3
    if 'WLAN' in hostname:
        opsi = 0
    else:
        opsi = 3
    
    # Neuen Eintrag erstellen
    neuer_eintrag = pd.DataFrame({
        'Raumnummer': [raumnummer],
        'Hostname': [hostname],
        'blubb': [hardwaregruppe],
        'MAC': [MAC],
        'IP': [IP],
        'lupp': [lupp],
        'li': [li],
        'la': [la],
        'lala': [lala],
        'lu': [lu],
        'opsi': [opsi]
    })

    # Eintrag zur bestehenden Hostliste hinzufügen
    hostliste = get_hostliste_from_db()
    hostliste = pd.concat([hostliste, neuer_eintrag], ignore_index=True)

    # Eintrag in die Datenbank einfügen
    neuer_eintrag.to_sql('hostliste', engine, if_exists='append', index=False)

    print(f"Eintrag für Raum {raumnummer} wurde hinzugefügt. Hostname: {hostname}")

def pc_erfassungs_csv_laden():
    # Pfad zur CSV-Datei eingeben
    pfad = input("Geben Sie den Pfad zur CSV-Datei an: ")

    # CSV-Datei einlesen und in pandas DataFrame speichern
    df = pd.read_csv(pfad, delimiter=';', header=None)

    # Daten für die Datenbank vorbereiten
    entries = []
    raumnummer = input("Geben Sie die Raumnummer ein: ")
    hardwaregruppe = input("Geben Sie die Hardwaregruppe ein: ")
    hostnamenerweiterung = input("Geben Sie, falls gewünscht, eine Erweitung des Hostnamens ein: ")
    for index in range(0, len(df), 2):
        pc_data = df.iloc[index]
        wlan_data = df.iloc[index + 1]
        nana, pc_nummer = pc_data[0].split("PC")
        mac = pc_data[1]

        # IP-Adresse zusammensetzen
        numerische_raumnummer = ''.join(filter(str.isdigit, raumnummer))
        
        ip = f"10.1.{int(numerische_raumnummer)}.{''.join(filter(str.isdigit, pc_nummer))}"

        # Werte für die restlichen Spalten festsetzen
        hostname = f"{raumnummer}PC{pc_nummer}{hostnamenerweiterung}"
        blubb = hardwaregruppe
        lupp = None
        li = 1.0
        la = 1.0
        lala = 'classroom-studentcomputer'
        lu = 1.0
        opsi = 0 if "WLAN" in pc_data[0] else 3.0

        # Eintrag für die Datenbank vorbereiten
        entry = {
            'Raumnummer': raumnummer,
            'Hostname': hostname,
            'blubb': blubb,
            'MAC': mac,
            'IP': ip,
            'lupp': lupp,
            'li': li,
            'la': la,
            'lala': lala,
            'lu': lu,
            'opsi': opsi
        }
        entries.append(entry)

    # Einträge zur Datenbank hinzufügen
    new_entries_df = pd.DataFrame(entries)
    print(new_entries_df)
    new_entries_df.to_sql('hostliste', engine, if_exists='append', index=False)

    print(f"Einträge aus CSV-Datei in die Datenbank geladen.")

def csv_hostliste_aus_db_generieren():
    # Daten aus der Datenbank abrufen
    hostliste = get_hostliste_from_db()

    # Sortieren nach Raumnummer
    hostliste_sorted = hostliste.sort_values(by='Raumnummer')

    # CSV-Datei erstellen und speichern
    hostliste_sorted.to_csv('hostliste_sorted.csv', sep=';', index=False)

    print("CSV-Datei aus der Datenbank generiert und nach Raumnummer sortiert.")

def office_365_massenimport(path):
    csv_dateipfad = path
    bearbeitete_daten = []

    with open(csv_dateipfad, 'r', encoding= 'utf-8') as csvdatei:
        csv_reader_object = csv.reader(csvdatei, delimiter=";")
        
        for row in csv_reader_object:
            anlagedatum = "2023"
            name = row[0]
            print(name)
            vorname, nachname = name.split(' ')
            benutzername = row[2] + "@gsmgh.net"
            positition = "schüler"
            abteilung = (row[1]+"-"+anlagedatum)
            telefon = "110"
            telefonGeschäftlich ="0815"
            telefonMobil = "112"
            fax = "ABCDEFG"
            alternativeEmail =benutzername
            adresse ="Seegartenstraße 16"
            ort = "MGH"
            bundesstaat = "Badenwürttemberg"
            postleitzahl = "97980"
            land ="Germania"
        
            bearbeitete_zeile = [
                benutzername,
                vorname,
                nachname,
                name,  
                positition,  
                abteilung,
                telefon, 
                telefonGeschäftlich,  
                telefonMobil,  
                fax,  
                alternativeEmail, 
                adresse,  
                ort,  
                bundesstaat, 
                postleitzahl, 
                land 
            ]
            bearbeitete_daten.append(bearbeitete_zeile)


    for bearbeitete_zeile in bearbeitete_daten:
        print(bearbeitete_zeile)


    neue_csv_datei = "./schulprojekt_bauer/csv_files/bearbeitete_e3fi1-admin.csv"
    with open(neue_csv_datei, 'w', newline='', encoding='utf-8') as neue_csv:
        csv_writer = csv.writer(neue_csv)
        csv_writer.writerows(bearbeitete_daten)

def umwandeln_csv(input_datei, output_datei):
    with open(input_datei, 'r', encoding='utf-8') as csv_input, open(output_datei, 'w', encoding='utf-8', newline='') as csv_output:
        reader = csv.DictReader(csv_input, delimiter=';')

        # Überprüfe, ob 'ID' im Header vorhanden ist, ansonsten benutze den ersten Schlüssel im Header
        id_field = 'ID' if 'ID' in reader.fieldnames else next(iter(reader.fieldnames))

        fieldnames = ['Klasse', 'Nachname', 'Vornamen', 'Geburtsdatum mit Gültigkeit', id_field]
        writer = csv.DictWriter(csv_output, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()

        for row in reader:
            # Datum umformatieren
            geburtsdatum = datetime.strptime(row['Geburtsdatum mit Gültigkeit'], '%d.%m.%Y').strftime('%d.%m.%Y')

            # Schreibe umgeordnete Daten in die Ausgabedatei
            writer.writerow({
                'Klasse': row['Klasse'],
                'Nachname': row['Nachname'],
                'Vornamen': row['Vornamen'],
                'Geburtsdatum mit Gültigkeit': geburtsdatum,
                id_field: row[id_field]
            })

def abgleich_abteilungsname(csv_files):
    # Einlesen der CSV-Dateien mit Leerzeichen als Delimiter
    dataframes = [pd.read_csv(file, delimiter=' ', skipinitialspace=True) for file in csv_files]

    # Extrahieren der Spalte 'Klasse' aus jedem DataFrame
    klassen_spalten = [df['Klasse'] for df in dataframes]

    # Erstellen eines neuen DataFrames mit den extrahierten Klassen-Spalten
    merged_df = pd.concat(klassen_spalten, axis=1)

    # Benennung der Spalten entsprechend der Dateipfade ohne Dateiendungen
    column_names = [os.path.splitext(os.path.split(file)[-1])[0] for file in csv_files]
    merged_df.columns = column_names

    # Entfernen von doppelten Zeilen
    merged_df = merged_df.drop_duplicates()

    # Speichern des Ergebnisses in einer neuen CSV-Datei
    merged_csv_path = 'abgleich_abteilungsname_result.csv'
    merged_df.to_csv(merged_csv_path, sep=';', index=False)

    print(f"Abgleich der Abteilungsnamen abgeschlossen. Ergebnisse in '{merged_csv_path}' gespeichert.")

while True:
    obermenue = input('''
        Wählen Sie, was Sie tun möchten:
        1 -> Hostliste
        2 -> Abgleich Abteilungsname
        3 -> Office365 Massenimport
        4 -> Benutzerkonten anlegen

        9 -> quit
        ''')
    
    if obermenue == '1':
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
            elif eingabe == 'b':
                raum = input("Geben Sie den gewünschten Raum ein: ")
                show_raum_data(raum)
            elif eingabe == 'c':
                adressbereich = input("Geben Sie den Adressbereich an: ")
                geraete_in_adressbereich(adressbereich)
            elif eingabe == 'd':
                print("Geben Sie den Adressbereich im Format 'start_ip-end_ip' ein.")
                adressbereich = input("Beispiel: 192.168.1.1-192.168.1.255\nGeben Sie den Adressbereich an: ")

                freie_ip = get_freie_ip(adressbereich)

                if freie_ip:
                    print(f"Die erste freie IP-Adresse im Adressbereich {adressbereich} ist: {freie_ip}")
                else:
                    print(f"Es gibt keine freien IP-Adressen im Adressbereich {adressbereich}")
            elif eingabe == 'e':
                raumnummer = input("Geben Sie die Raumnummer ein: ")
                MAC = input("Geben Sie die MAC-Adresse ein: ")
                IP = input("Geben Sie die IP-Adresse ein: ")
                neuer_eintrag(raumnummer, MAC, IP)
            elif eingabe == 'f':
                try:
                    pc_erfassungs_csv_laden()
                except FileNotFoundError as e:
                    print(f"Fehler beim Laden der CSV-Datei: {e}")
            elif eingabe == 'g':
                try:
                    csv_hostliste_aus_db_generieren()
                except FileNotFoundError as e:
                    print(f"Fehler beim Generieren der CSV-Datei: {e}")
            elif eingabe == 'h':
                break
            else:
                print("Ungültige Eingabe! ")
    elif obermenue == '2':
        # CSV-Dateien auswählen
        csv_files = []
        for _ in range(3):
            file_path = input("Geben Sie den Pfad zu einer CSV-Datei an: ")
            csv_files.append(file_path)

        # Abgleich der Abteilungsnamen durchführen
        try:
            abgleich_abteilungsname(csv_files)
        except FileNotFoundError as e:
            print(f"Fehler beim Abgleich der Abteilungsnamen: {e}")
    elif obermenue == '3':
        path = input("Geben Sie den Pfad zu der zu bearbeitenden CSV-Datei an: ")
        try:
            office_365_massenimport(path)
        except FileNotFoundError as e:
            print(f"Fehler beim Massenimport: {e}")
    elif obermenue == '4':
        eingabedatei = input("Pfad der Datei die umgewandelt werden soll")
        ausgabedatei = input("Name der Datei, die ausgegeben werden soll")
        try:
            umwandeln_csv(eingabedatei, ausgabedatei)
        except FileNotFoundError as e:
            print(f"Fehler beim Umwandeln der CSV-Datei: {e}")
    elif obermenue == '9':
        break
    else:
        print("Ungültige Eingabe. Bitte geben Sie 1, 2, 3, 4 oder 9 ein")

# Verbindung zur Datenbank schließen
engine.dispose()
