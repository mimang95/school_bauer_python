class Laeufer:
    def __init__(self, startnummer, name, lauf):
        self.startnummer = startnummer
        self.name = name
        self.lauf = lauf
        self.zielzeit = None

# Liste zur Verwaltung der Läuferobjekte
laufteilnehmer = []

def Anmeldung():
    startnummer = input("Bitte geben Sie die Startnummer des Teilnehmers ein: ")
    name = input("Bitte geben Sie den Namen des Teilnehmers ein: ")
    lauf = input("Bitte geben Sie den Lauf des Teilnehmers ein (3km, 5km, 10km, 21km): ")
    
    if lauf not in ["3km", "5km", "10km", "21km"]:
        print("Ungültiger Lauf! Bitte geben Sie einen der folgenden Läufe ein: 3km, 5km, 10km, 21km")
        return
    
    teilnehmer = Laeufer(startnummer, name, lauf)
    laufteilnehmer.append(teilnehmer)
    print(f"{name} wurde erfolgreich für den {lauf} Lauf angemeldet.")

def Zielzeit():
    startnummer = input("Bitte geben Sie die Startnummer des Teilnehmers ein: ")
    zielzeit = input("Bitte geben Sie die Zielzeit des Teilnehmers in Minuten und Sekunden ein (z.B. 45:30): ")
    
    for teilnehmer in laufteilnehmer:
        if teilnehmer.startnummer == startnummer:
            teilnehmer.zielzeit = zielzeit
            print(f"Zielzeit für {teilnehmer.name} ({teilnehmer.lauf} Lauf) wurde erfasst: {zielzeit}")
            return
    
    print("Teilnehmer mit dieser Startnummer wurde nicht gefunden.")

def Statistik():
    laufanzahl = {"3km": 0, "5km": 0, "10km": 0, "21km": 0}
    
    for teilnehmer in laufteilnehmer:
        laufanzahl[teilnehmer.lauf] += 1
    
    gesamtanzahl = len(laufteilnehmer)
    
    print("Statistik der Anmeldungen:")
    for lauf, anzahl in laufanzahl.items():
        print(f"{lauf} Lauf: {anzahl} Teilnehmer")
    
    print(f"Gesamtanzahl der Anmeldungen: {gesamtanzahl}")

def Ergebnisse():
    print("Ergebnisse der Teilnehmer:")
    for teilnehmer in laufteilnehmer:
        print(f"Startnummer: {teilnehmer.startnummer}, Zielzeit: {teilnehmer.zielzeit}")

while True:
    print("\n1. Anmeldung\n2. Zielzeit erfassen\n3. Statistik\n4. Ergebnisse anzeigen\n5. Beenden")
    auswahl = input("Bitte wählen Sie eine Option (1/2/3/4/5): ")
    
    if auswahl == "1":
        Anmeldung()
    elif auswahl == "2":
        Zielzeit()
    elif auswahl == "3":
        Statistik()
    elif auswahl == "4":
        Ergebnisse()
    elif auswahl == "5":
        print("Das Programm wird beendet.")
        break
    else:
        print("Ungültige Auswahl! Bitte wählen Sie eine der verfügbaren Optionen (1/2/3/4/5).")