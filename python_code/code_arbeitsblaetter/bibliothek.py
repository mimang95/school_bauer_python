# verwenden von IsInstance nötig
from abc import ABC, abstractmethod

class Bibliothek:
    def __init__(self, leserliste, medienliste):
        self.__leserliste = leserliste
        self.__medienliste = medienliste

    def getLeserliste(self):
        return self.__leserliste
    def getMedienliste(self):
        return self.__medienliste
    
    def ermittleVormerkungen(self, bibNr):
        vormerkungen = 0
        for leser in self.getLeserliste():
            for vormerkung in leser.getVormerkliste():
                if vormerkung.getBibNr() == bibNr:
                    vormerkungen += 1
        return vormerkungen
    
    def getHoerbuecher(self):
        hoerbuecher = 0
        for leser in self.getLeserliste():
            hoerbuecher += leser.countHoerbuecherLeser()
        return hoerbuecher

    def medienErstellen(self, medium):
        self.getMedienliste().append(medium)

    def leserErstellen(self, leser):
        self.getLeserliste().append(leser)
    
    def buchAusgeliehen(self, bibNr, leser):
        for leser in self.getLeserliste():
            for buch in leser.getAusleihliste():
                if buch.getBibNr() == bibNr:
                    return True
                else:
                    pass
    


class Medium(ABC):
    def __init__(self, bibNr, titel, zustand):
        self.__bibNr = bibNr
        self.__titel = titel
        self.__zustand = zustand
    
    def getBibNr(self):
        return self.__bibNr

class Buch(Medium):
    def __init__(self, seitenzahl, bibNr, titel, zustand):
        super().__init__(bibNr, titel, zustand)
        self.__seitenzahl = seitenzahl

class Hörbuch(Medium):
    def __init__(self, dauer, bibNr, titel, zustand):
        super().__init__(bibNr, titel, zustand)
        self.__dauer = dauer

class Leser:
    def __init__(self, leserNr, name, vorname, ausleihliste, vormerkliste):
        self.__leserNr = leserNr
        self.__name = name
        self.__vorname = vorname
        self.__ausleihliste = ausleihliste
        self.__vormerkliste = vormerkliste
    def getAusleihliste(self):
        return self.__ausleihliste
    def getVormerkliste(self):
        return self.__vormerkliste
    
    def medienAusleihen(self, medium):
        self.getAusleihliste().append(medium)
    
    def hatAusgeliehen(self,bibNr):
        for buch in self.getAusleihliste():
             if(bibNr == buch.getBibNr()):
                 return True
             else:
                 pass
        return False
             
    def countHoerbuecherLeser(self):
        count = 0
        for buch in self.getAusleihliste():
            if isinstance(buch, Hörbuch):
                count += 1
            else:
                pass
        return count
    
    def vormerkungAnlegen(self, medium):
        self.getVormerkliste().append(medium)

if __name__ == "__main__":
    bib = Bibliothek([], [])
    buch1 = Buch(250, 1, "Harry Potter and the philosophers stone", "gut")
    buch2 = Hörbuch(400, 2, "Harry Potter and the chamber of secrets", "schlecht")
    leser1 = Leser(1, "Timm", "Tim", [], [])
    leser2 = Leser(2, "Hans", "Dampf", [], [])
    bib.leserErstellen(leser1)
    bib.leserErstellen(leser2)
    bib.medienErstellen(buch1)
    bib.medienErstellen(buch2)
    leser1.vormerkungAnlegen(buch1)
    leser2.vormerkungAnlegen(buch2)
    leser1.medienAusleihen(buch2)
    print(f"Hat der leser1 das Buch 2 ausgeliehen?: {leser1.hatAusgeliehen(2)}")
    print(f"Hörbücher: {bib.getHoerbuecher()}")
    print(f"Anzahl Vormerkungen: {bib.ermittleVormerkungen(2)}")
    