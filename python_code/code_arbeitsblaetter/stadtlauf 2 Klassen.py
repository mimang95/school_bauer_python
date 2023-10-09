class Laeufer: # ma
	def __init__(self, name, startnummer, laufnummer): # ev
		self.__Name = name #von_Abdul
		self.__StartNummer = startnummer 
		self.__LaufNummer = laufnummer
		self.__zeit = "" #ev
	
	def getDaten(self):
		rueckgabe=f"{self.__StartNummer};{self.__Name};{self.__LaufNummer};{self.__zeit}"
		return rueckgabe
	def getStartnummer(self):
		return self.__StartNummer
	def setZeit(self,zeit):
		self.__zeit=zeit

class Stadtlauf:

    laufteilnehmer = [] # ma
    def Menue(self):
        while True: #ev
            auswahl = input("Anmeldung:1, Zeit: 2, Anzeige: 3, Beenden: 9")
            if auswahl == "1":
                self.Anmeldung()
            elif auswahl == "2":
                self.Zeit()
            elif auswahl == "9": break #ev
            else:
                self.Anzeige() #ma
        
    def Anmeldung(self):
        startnummer = int(input("Bitte geben sie die Startnummer ein: ")) #(NO)
        name = input("Bitte geben Sie den Namen ein") # ma
        lauf = int(input("Bitte geben Sie die Laufnummer ein: ")) #ev
        neuerLauefer = Laeufer(name, startnummer, lauf) #mm
        self.laufteilnehmer.append(neuerLauefer) # ev
	
    def Zeit(self):
        startnummer = int(input("Startnummer:")) #NO
        zeit = input("Zeit: ") #ma
        for e in self.laufteilnehmer: 
            if e.getStartnummer() == startnummer:
                e.setZeit(zeit)

    def Anzeige(self):
        for e in self.laufteilnehmer:
            print(e.getDaten())

if __name__ == "__main__":
	
    print("Stadtlauf")  # von bu
    stadtlaufmgh = Stadtlauf()
    stadtlaufmgh.Menue()



	
	
	



