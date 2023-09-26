# Berechnung des Geldbestandes
wert = [10, 20, 50, 100, 200]
anzahl = [3, 5, 0, 0, 2]
while True:
    eingabe = int(input("Geben Sie eine Zahl aus [0, 1, 2, 3, 4, 99] ein: "))
    if eingabe == 0 or eingabe == 1 or eingabe == 2 or eingabe == 3 or eingabe == 4 or eingabe == 99:
        break
    else:
        print("Falsche Eingabe! Noch mal bitte:")

def geld_in_Magazin(num):
    if 0 <= num <= 5:
        return anzahl[num] * wert[num]
    elif num == 99:
        summe = 0
        for i in range(5):
            summe += anzahl[i] * wert[i]
        return summe
    else:
        return "Falsche Eingabe"

print(geld_in_Magazin(eingabe))

# Geldrückgabe
muenzWert = [5, 10, 20, 50, 100, 200, 500, 1000]
muenzAnzahl = [5, 10, 10, 10, 10, 5, 5, 5]

def vorhandene_muenzen():
    print("Vorhandene Münzen: ")
    for i in range(len(muenzWert)):
        print(f"{muenzWert[i]} Cent: {muenzAnzahl[i]}")

def rueckgabebetrag_optimieren(betrag):
    rueckgabe = {}
    
    # Durchlaufen der Münz- und Scheinwerte rückwärts, um größere Werte zuerst zu verwenden
    for i in range(len(muenzWert) - 1, -1, -1):
        wert = muenzWert[i]
        anzahl = betrag // wert  # Berechnen der max. Anzahl  dieser Münzen, die zurückgegeben werden kann
        
        # Überprüfen, ob genügend Münzen/Scheine vorhanden sind
        if anzahl > muenzAnzahl[i]:
            anzahl = muenzAnzahl[i]
        
        if anzahl > 0:
            rueckgabe[wert] = anzahl # Hinzufügen der Anzahl an Münzen zu dem Dictionary
            betrag -= wert * anzahl
        
        if betrag == 0:
            break
    
    if betrag == 0:
        print("Rückgabebetrag in Münzen/Scheinen:")
        for wert, anzahl in rueckgabe.items():
            print(f"{anzahl} x {wert} Cent")
    else:
        print("Es sind nicht genügend Münzen/Scheine verfügbar, um den Betrag zurückzugeben.")
        vorhandene_muenzen()

fahrpreis = int(input("Geben Sie den Fahrpreis ein"))
eingeworfener_betrag = int(input("Geben Sie den eingeworfenen Betrag ein: "))

wechselbetrag = eingeworfener_betrag - fahrpreis

rueckgabebetrag_optimieren(wechselbetrag)


# Berechnung der Ausleihdauer
a_jahr = int(input("Geben Sie ein Ausleihjahr ein: "))
r_jahr = int(input("Geben Sie ein Rueckgabejahr ein: "))
a_monat = int(input("Geben Sie den Ausleihmonat als int an (Bsp. Januar = 1, Februar = 2, ...): "))
a_tag = int(input("Geben Sie den Ausleihtag ein: "))
r_monat = int(input("Geben Sie den Rückgabemonat als int an (Bsp. Januar = 1, Februar = 2, ...): "))
r_tag = ausleihtag = int(input("Geben Sie den Rückgabetag ein: "))

monat = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def calculate_length(ausleihmonat, ausleihtag, rueckgabemonat, rueckgabetag, ausleihjahr, rueckgabejahr):
    days = 0
    if ausleihjahr == rueckgabejahr:
        if ausleihmonat == rueckgabemonat:
            days += (rueckgabetag - ausleihtag)
        else:
            days += (monat[rueckgabemonat] - ausleihtag)
        for i in range(ausleihmonat, rueckgabemonat):
            days += monat[i]
        if ausleihmonat != rueckgabemonat:
            days += rueckgabetag
    else:
        # erstes Jahr
        days += (monat[ausleihmonat] - ausleihtag)
        if ausleihmonat < 12:
            for i in range(ausleihmonat + 1, 13):
                days += monat[i]
        
        # volle Jahre zwischendrin
        ganze_jahre = rueckgabejahr - ausleihjahr - 1
        if ganze_jahre >= 1:
            days += 365 * ganze_jahre

        # letztes Jahr
        for i in range(1, rueckgabemonat):
            days += monat[i]
        days += rueckgabetag
    return days

print(calculate_length(a_monat, a_tag, r_monat, r_tag, a_jahr, r_jahr))

# Messreihe
messwert = []
error = 0
minimum = float('inf')
maximum = float('-inf')

print("Geben Sie die Messwerte nacheinander ein. Drücken Sie die ENTER-Taste, um jeden Messwert zu bestätigen.")
print("Geben Sie 'q' ein und drücken Sie ENTER, wenn Sie die Eingabe beenden möchten.")

while True:
    eingabe = input("Messwert (V): ")
    
    if eingabe == 'q':
        break
    
    try:
        messwert_v = float(eingabe)
        if 3.5 <= messwert_v <= 5.0:
            messwert.append(messwert_v)
            if messwert_v > maximum:
                maximum = messwert_v
            if messwert_v < minimum:
                minimum = messwert_v
        else:
            error += 1
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine Dezimalzahl im Bereich von 3.5 bis 5.0 ein.")


print(f"Anzahl der Messwerte außerhalb des zulässigen Bereichs: {error}")
print(f"Größter Messwert innerhalb des zulässigen Bereichs: {maximum} V")
print(f"Kleinster Messwert innerhalb des zulässigen Bereichs: {minimum} V")