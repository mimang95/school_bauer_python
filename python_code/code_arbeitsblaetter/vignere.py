# Vignere Verschlüsselung
def codieren(klartext, schluessel):
    verschluesselter_text = []

    for i in range(len(klartext)):
        klartextbuchstabe = ord(klartext[i]) - ord('A') # Bestimmt dem wievielten Buchstaben des Alphabets das aktuelle Zeichen entspricht 
        schluesselbuchstabe = ord(schluessel[i % len(schluessel)]) - ord('A') # Bestimmt dem wievielten Buchstaben des Alphabets das aktuelle Schlüsselzeichen entspricht
        verschluesselter_buchstabe = (klartextbuchstabe + schluesselbuchstabe) % 26 
        # Modulo 26, da die Buchstaben durch die Addition über das Ende des Alphabets (26 Buchstaben) hinausgehen können
        verschluesselter_buchstabe += ord('A')
        verschluesselter_text.append(chr(verschluesselter_buchstabe))
    return ''.join(verschluesselter_text)

klartext = input("Geben Sie den Klartext ein: ")
schluessel = input("Geben Sie den Schlüssel ein: ")

verschluesselter_text = codieren(klartext, schluessel)
print("Verschlüsselter Text:", verschluesselter_text)