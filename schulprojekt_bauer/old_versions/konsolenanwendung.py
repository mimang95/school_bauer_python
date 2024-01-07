import pandas as pd
import ipaddress

# Dateinamen der CSV-Dateien
pfad_hostliste = './schulprojekt_bauer/hostliste.csv'

# Einlesen der CSV-Dateien
hostliste = pd.read_csv(pfad_hostliste, delimiter=';')

# Spalten, die ausgewählt werden sollen
desired_columns = ['Raumnummer', 'MAC', 'IP', 'Hostname']

# Ausgabe der ausgewählten Daten
print(hostliste[desired_columns])

def filter_by_ip_range(dataframe, ip_start, ip_end):
    filtered_data = dataframe[dataframe['IP'].between(ip_start, ip_end)]
    return filtered_data

# def show_important_data():
#     print(hostliste[desired_columns])

def show_important_data():
    formatted_data = hostliste[desired_columns].to_string(index=False)
    print(formatted_data)

# def show_raum_data(raum):
#     print(hostliste[hostliste['Raumnummer'] == raum])

# def geraete_in_adressbereich(netzwerkpräfix):
#     print(hostliste[hostliste['IP'].str.startswith(netzwerkpräfix)])

def show_raum_data(raum):
    filtered_data = hostliste[hostliste['Raumnummer'] == raum][desired_columns]
    formatted_data = filtered_data.to_string(index=False)
    print(formatted_data)

def geraete_in_adressbereich(netzwerkpräfix):
    filtered_data = hostliste[hostliste['IP'].str.startswith(netzwerkpräfix)][desired_columns]
    formatted_data = filtered_data.to_string(index=False)
    print(formatted_data)

def get_freie_ip(adressbereich):
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
    global hostliste  # Hier wird nicht neu deklariert, sondern auf die bereits global deklarierte Variable zugegriffen

    # Angenommene Werte für die restlichen Spalten
    hostname = hostliste.iloc[0]['Hostname']
    blubb = hostliste.iloc[0]['blubb']
    lupp = hostliste.iloc[0]['lupp']
    li = hostliste.iloc[0]['li']
    la = hostliste.iloc[0]['la']
    lala = hostliste.iloc[0]['lala']
    lu = hostliste.iloc[0]['lu']
    opsi = hostliste.iloc[0]['opsi']

    # Neuen Eintrag erstellen
    neuer_eintrag = pd.DataFrame({
        'Raumnummer': [raumnummer],
        'Hostname': [hostname],
        'blubb': [blubb],
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
    hostliste = pd.concat([hostliste, neuer_eintrag], ignore_index=True)

    # CSV-Datei aktualisieren
    hostliste.to_csv(pfad_hostliste, sep=';', index=False)

    print(f"Eintrag für Raum {raumnummer} wurde hinzugefügt.")

def mehrere_eintraege_aus_csv(csv_dateipfad):
    global hostliste

    try:
        # CSV-Datei einlesen
        neue_eintraege = pd.read_csv(csv_dateipfad, delimiter=';')

        # Angenommene Werte für fehlende Spalten in den neuen Einträgen
        ang_nom_hostname = hostliste.iloc[0]['Hostname']
        ang_nom_blubb = hostliste.iloc[0]['blubb']
        ang_nom_lupp = hostliste.iloc[0]['lupp']
        ang_nom_li = hostliste.iloc[0]['li']
        ang_nom_la = hostliste.iloc[0]['la']
        ang_nom_lala = hostliste.iloc[0]['lala']
        ang_nom_lu = hostliste.iloc[0]['lu']
        ang_nom_opsi = hostliste.iloc[0]['opsi']

        # Fehlende Spalten hinzufügen
        neue_eintraege['Hostname'] = ang_nom_hostname
        neue_eintraege['blubb'] = ang_nom_blubb
        neue_eintraege['lupp'] = ang_nom_lupp
        neue_eintraege['li'] = ang_nom_li
        neue_eintraege['la'] = ang_nom_la
        neue_eintraege['lala'] = ang_nom_lala
        neue_eintraege['lu'] = ang_nom_lu
        neue_eintraege['opsi'] = ang_nom_opsi

        # Einträge zur bestehenden Hostliste hinzufügen
        hostliste = pd.concat([hostliste, neue_eintraege], ignore_index=True)

        # CSV-Datei aktualisieren
        hostliste.to_csv(pfad_hostliste, sep=';', index=False)

        print(f"Einträge aus {csv_dateipfad} wurden hinzugefügt.")

    except FileNotFoundError:
        print(f"Die Datei {csv_dateipfad} wurde nicht gefunden.")
    except pd.errors.EmptyDataError:
        print(f"Die Datei {csv_dateipfad} enthält keine Daten.")
    except Exception as e:
        print(f"Fehler beim Einlesen der Datei {csv_dateipfad}: {e}")

while True:
    eingabe = input('''
          Wählen Sie was sie tun möchten:
          a -> Anzeige aller Daten
          b -> Anzeige aller Geräte eines Raumes
          c -> Anzeige aller Geräte eines bestimmten Adressbereichs
          d -> Ermittlung freier IP-Adresse bei einem vorgegebenen Adressbereich
          e -> Erzeugen Sie einen neuen Eintrag durch Eingabe von Raumnummer, MAC-Adresse und IP-Adresse (für ein Gerät)
          f -> Erzeugen Sie mehrere Einträge durch Einlesen einer CSV-Datei, welche die entsprechenden Daten enthält
          g -> Erzeugen Sie eine neue CSV-Hostliste aus der Datenbank sortiert nach der Raumnummer. 
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
        csv_dateipfad = input("Geben Sie den Pfad zur CSV-Datei ein: ")
        mehrere_eintraege_aus_csv(csv_dateipfad)
    if eingabe == 'g':
        pass
    break