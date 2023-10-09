print("Stadtlauf")  # von bu


laufteilnehmer = [] # ma

class Laeufer: # ma
	def __init__(self, name, startnummer, laufnummer): # ev
		self.__Name = name #von_Abdul
		self.__StartNummer = startnummer 
		self.__LaufNummer = laufnummer
		self.__zeit = "" #ev
	
	def getDaten(self):
		return self.__Name, self.__StartNummer, self.__LaufNummer


def Anmeldung():
	startnummer = int(input("Bitte geben sie die Startnummer ein: ")) #(NO)
	name = input("Bitte geben Sie den Namen ein") # ma
	lauf = int(input("Bitte geben Sie die Laufnummer ein: ")) #ev
	neuerLauefer = Laeufer(name, startnummer, lauf) #mm
	laufteilnehmer.append(neuerLauefer) # ev
	
def Zeit():
	startnummer = int(input("Startnummer:")) #NO
	zeit = input("Zeit: ") #ma

	for e in laufteilnehmer: 
		if e.StartNummer == startnummer:
			e.zeit = zeit

def Anzeige():

	for e in laufteilnehmer:
		# print(e) #mm
		print(e.StartNummer)
		print(e.LaufNummer)
		print(e.Name)
		print(e.zeit)

if __name__ == "__main__":
	while True: #ev
		auswahl = input("Anmeldung:1, Zeit: 2, Anzeige: 3, Beenden: 9")
		if auswahl == "1":
			Anmeldung()
		elif auswahl == "2":
			Zeit()
		elif auswahl == "9": break #ev
		else:
			Anzeige() #ma
	
	



