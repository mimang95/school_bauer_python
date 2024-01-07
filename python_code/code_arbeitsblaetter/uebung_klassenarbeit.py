from abc import ABC
class Bibliothek:
    def __init__(self):
        self.__leserliste = []
        self.__medienliste = []
    def getLeserliste(self):
        return self.__leserliste
    def getMedienliste(self):
        return self.__medienliste

    def ermittleVormerkungen(self, bibNr):
        count = 0
        for leser in self.getLeserliste():
            for medium in leser.getVormerkliste():
                if medium.getBibNr() == bibNr:
                    count += 1
        return count

    def numberHoerbuecher(self):
        number = 0
        for leser in self.getLeserliste():
            for medium in leser.getAusleihliste():
                if isinstance(medium, Hörbuch):
                    number += 1
        return number
    
    def erstelleBuch(self, buch):
        self.getMedienliste().append(buch)
    def erstelleLeser(self, leser):
        self.getLeserliste().append(leser)
    
    def mediumAusgeliehen(self, lesernummer, bibNr):
        for leser in self.getLeserliste():
            if leser.getLeserNr() == lesernummer and leser.hatAusgeliehen(bibNr):
                print("Hat shizzle ausgeliehen")
                return True
        print("Hat shizzl nicht ausgeliehen")
    
    def showVormerkungen(self):
        for leser in self.getLeserliste():
            for medium in leser.getVormerkliste():
                print(medium.getTitel())
            
class Leser:
    def __init__(self, leserNr, name, vorname):
        self.__leserNr = leserNr
        self.__name = name
        self.__vorname = vorname
        self.__vormerkliste = []
        self.__ausleihliste = []
    
    def getLeserNr(self):
        return self.__leserNr
    def getAusleihliste(self):
        return self.__ausleihliste
    def getVormerkliste(self):
        return self.__vormerkliste
    
    def hatAusgeliehen(self, bibNr):
        for medium in self.getAusleihliste():
            if bibNr == medium.getBibNr():
                return True
    
    def medienAusleihen(self, medium):
        self.getAusleihliste().append(medium)

    def addVormerkung(self, medium):
        self.getVormerkliste().append(medium)
    
class Medium(ABC):
    def __init__(self, bibNr, titel, zustand):
        self.__bibNr = bibNr
        self.__titel = titel
        self.__zustand = zustand
    
    def getBibNr(self):
        return self.__bibNr
    
    def getTitel(self):
        return self.__titel
    
class Buch(Medium):
    def __init__(self, seitenzahl, bibNr, titel, zustand):
        super().__init__(bibNr, titel, zustand)
        self.__seitenzahl = seitenzahl

class Hörbuch(Medium):
    def __init__(self, dauer, bibNr, titel, zustand):
        super().__init__(bibNr, titel, zustand)
        self.__dauer = dauer

class Main:
    def __init__(self):
        self._stadtbibliothek = Bibliothek()
    def medienErstellen(self, medium):
        self._stadtbibliothek.erstelleBuch(medium)
    def leserErstellen(self, leser):
        self._stadtbibliothek.erstelleLeser(leser)
    def anzahlHoerbuecherAusgeliehen(self):
        print(self._stadtbibliothek.numberHoerbuecher())
    def vormerkungenAnlegen(self, medium, leser):
        for reader in self._stadtbibliothek.getLeserliste():
            if reader == leser:
                reader.addVormerkung(medium)
    def vormerkungenAnzeigen(self):
        self._stadtbibliothek.showVormerkungen()
    def medienAusleihen(self, leser, medium):
        for reader in self._stadtbibliothek.getLeserliste():
            if reader == leser:
                leser.medienAusleihen(medium)
    def mediumIstAusgeliehen(self, lesernummer, bibnr):
        self._stadtbibliothek.mediumAusgeliehen(lesernummer, bibnr) 

if __name__=="__main__":
    main = Main()
    medium1 = Buch(300, 1, "Titel1", "top")
    medium3 = Buch(300, 3, "Titel3", "top")
    medium4 = Hörbuch(50, 4, "Harry Potter", "top")
    medium2 = Hörbuch(100, 2, "Titel2", "schlecht")
    leser1 = Leser(1, "Schmidt", "Heinz")
    leser2 = Leser(2, "Müller", "Petra")

    main.medienErstellen(medium1)
    main.medienErstellen(medium2)
    main.medienErstellen(medium3)
    main.medienErstellen(medium4)
    main.leserErstellen(leser1)
    main.leserErstellen(leser2)
    main.medienAusleihen(leser1, medium1)
    main.medienAusleihen(leser2, medium2)
    main.medienAusleihen(leser1, medium4)
    main.mediumIstAusgeliehen(1, 3) # Lesernummer, Bibnummer
    main.anzahlHoerbuecherAusgeliehen()
    main.vormerkungenAnlegen(medium2, leser1)
    main.vormerkungenAnlegen(medium4, leser1)
    main.vormerkungenAnzeigen()

