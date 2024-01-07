import csv


csv_dateipfad = "./schulprojekt_bauer/csv_files/e3fi1-admin.csv"
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