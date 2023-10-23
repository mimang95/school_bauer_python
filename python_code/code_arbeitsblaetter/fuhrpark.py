import os
from datetime import datetime

class Fahrzeug:
	def __init__(self, ID, Modell, Kennzeichen, Hersteller):
		self._aID = ID
		self._aModell = Modell
		self._aKennzeichen = Kennzeichen
		self._aHersteller = Hersteller

	def gibID(self):
		return self._aID
	def gibAlleDatenAlsText(self):
		return [self._aID, self._aModell, self._aKennzeichen, self._aHersteller]
	
class Pkw(Fahrzeug):
	def __init__(self, ID, Modell, Kennzeichen, Hersteller, anzahlKindersitze, hatAutomatik):	
		super().__init__(ID, Modell, Kennzeichen, Hersteller)
		self.__anzahlKindersitze = anzahlKindersitze
		self.__hatAutomatik= hatAutomatik
	
	def getAutomatik(self):
		return self.__hatAutomatik
	
	def getKindersitze(self):
		return self.__anzahlKindersitze

class Lkw(Fahrzeug):
	def __init__(self, ID, Modell, Kennzeichen, Hersteller, Nutzlast, Nutzvolumen):
		super().__init__(ID, Modell, Kennzeichen, Hersteller)
		self.__nutzlast = Nutzlast
		self.__nutzvolumen= Nutzvolumen

class Buchung():
	def __init__(self, id, von, bis, name):
		self.__aKfzId = id
		self.__vonZeitPkt = von
		self.__bisZeitPkt = bis
		self.__aMitglied = name
	
	def gibAlleDatenAlsText(self):
		return f"{self.__aKfzId}, {self.__vonZeitPkt}, {self.__bisZeitPkt}, Mitglied: {self.__aMitglied}"
	
	def pruefeBelegt(self, pKfzId, pVon, pBis):
		if pKfzId == self.__aKfzId and not(pVon >= self.__bisZeitPkt or pBis <= self.__vonZeitPkt):
			return True
		else:
			pass

class Steuerung():
	def __init__(self):
		self.aAnzKfz = 0
		self.aAnzBuchungen = 0
		self.__fahrzeuge = []
		self.__buchungen = []
		self.__buchungen.append(Buchung(1, datetime(2023, 10, 20), datetime(2023, 10, 25), "Max Mustermann"))

	def suchen(self, pKat, pAutomatik, pAnzKindersitze):
		for fahrzeug in self.__fahrzeuge:
			if isinstance(fahrzeug, pKat):
				if fahrzeug.getAutomatik() == pAutomatik and fahrzeug.getKindersitze() >= pAnzKindersitze:
					print(fahrzeug.gibAlleDatenAlsText())

	def buchen(self, pKfzID, pVon, pBis, pMitglied):
		belegt = False
		for buchung in self.__buchungen:
			if buchung.pruefeBelegt(pKfzID, pVon, pBis):
				belegt = True
				print("Fahrzeug ist bereits für den angegebenen Zeitraum gebucht.")
				break

		if not belegt:
			gefundenes_fahrzeug = None
			for fahrzeug in self.__fahrzeuge:
				if fahrzeug.gibID() == pKfzID:
					gefundenes_fahrzeug = fahrzeug
					break

			if gefundenes_fahrzeug is not None:
				neue_buchung = Buchung(pKfzID, pVon, pBis, pMitglied)
				self.__buchungen.append(neue_buchung)
				print("Buchung erfolgreich erstellt.")
			else:
				print("Fahrzeug mit der angegebenen ID wurde nicht gefunden.")
		

	def laden(self):
		stream = open("./python_code/code_arbeitsblaetter/fuhrparkdaten.csv",mode = "rt")
		daten = {}
		daten = stream.readlines()
		for i in daten:
			teilstring = i.split(";")
			id = teilstring[0]
			modell = teilstring[1]
			typ = teilstring[2]
			hersteller = teilstring[3]
			kennzeichen = teilstring[4]

			if typ == "Pkw":
				kindersitze = teilstring[5]
				isAutomatik = teilstring[6]
				self.__fahrzeuge.append(Pkw(id, modell, kennzeichen, hersteller, kindersitze, isAutomatik))
			else:
				nutzlast =  teilstring[5]
				nutzvolumen =  teilstring[6]
				self.__fahrzeuge.append(Lkw(id, modell, kennzeichen, hersteller, nutzlast,  nutzvolumen))
	
	def AlleAnzeigen(self):
		for f in self.__fahrzeuge:
			print(f.__dict__)
			
einFuhrpark = Steuerung()
einFuhrpark.laden()
einFuhrpark.AlleAnzeigen()
einFuhrpark.suchen(Pkw, "1", "1")
einFuhrpark.buchen(1, datetime(2023, 10, 20), datetime(2023, 10, 25), "Heinz")
einFuhrpark.buchen(2, datetime(2022, 10, 20), datetime(2022, 10, 25), "Charly")
einFuhrpark.buchen(3, datetime(2022, 10, 20), datetime(2022, 10, 25), "Charly")
einFuhrpark.AlleAnzeigen()