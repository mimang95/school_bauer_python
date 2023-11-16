from abc import ABC

class Medium(ABC):
    def __init__(self, bibNr, titel):
        self._bibNr=bibNr
        self._titel=titel
        self._zustand="neu"

    def getBibNr(self):
              return self._bibNr
   
class Hoerbuch(Medium):
     def __init__(self, bibNr, titel,dauer):
        super().__init__(bibNr,titel)
        self._dauer=dauer
    
class Buch(Medium):
    def __init__(self, bibNr, titel,seitenzahl):
        super().__init__(bibNr,titel)
        self._seitenzahl=seitenzahl
   
class Leser():
    def __init__(self, nr, name, vorname):
        self._leserNr=nr
        self._name=name
        self._vorname=vorname
        self.__vormerkliste = [] #Medium
        self.__ausleihliste = [] #Medium
    def getAusleihliste(self):
        return self.__ausleihliste
    def getVormerkliste(self):
        return self.__vormerkliste
    def hatAusgeliehen(self,bibNr):
        ausgeliehen=False
        for m in self.__ausleihliste:
            if m.getBibNr() == bibNr:
                ausgeliehen=True
        return ausgeliehen
    def ausleihen(self,pMedium):
        self.__ausleihliste.append(pMedium)
    def vormerken(self,pMedium):
        self.__vormerkliste.append(pMedium)
    def getLeserNr(self):
        return self._leserNr

    
class Bibliothek():
    def __init__(self):    
        self.__leserliste = [] #Leser
        self.__medienliste = [] #Medium
    def ermittleVormerkungen(self,bibNr):
        for l in self.__leserliste:
            vormerkliste = l.getVormerkliste()
            for m in vormerkliste:
                if m.getBibNr() == bibNr:
                    anzahl = anzahl + 1

        return anzahl
    
    def erstelleBuch(self,pNr, pTitel, pSeitenzahl):
        buch = Buch(pNr, pTitel, pSeitenzahl)
        self.__medienliste.append(buch)
    def erstelleHoerbuch(self,pNr, pTitel, pDauer):
        hoerbuch = Hoerbuch(pNr, pTitel, pDauer)
        self.__medienliste.append(hoerbuch)
    def erstelleLeser(self,pNr, pName, pVorname):
        leser = Leser(pNr, pName, pVorname)
        self.__leserliste.append(leser)
    def ausleihenMedium(self,bibNr,leserNr):
        for l in self.__leserliste:
            if l.getLeserNr() == leserNr:  
                for m in self.__medienliste:
                    if m.getBibNr() == bibNr:
                            l.ausleihen(m)

    def vormerkenMedium(self,bibNr,leserNr):
        for l in self.__leserliste:
            if l.getLeserNr() == leserNr:  
                for m in self.__medienliste:
                    if m.getBibNr() == bibNr:
                            l.vormerken(m)

    def anzeigenAusleihe(self,bibNr,leserNr):
        r = False
        for l in self.__leserliste:
            if l.getLeserNr()==leserNr:
                if l.hatAusgeliehen(bibNr) == True:
                    r=True
        return r
    def anzeigenAusgeliehenHoerbuecher(self):
        z = 0
        for l in self.__leserliste:
            ausleihliste = l.getAusleihliste()
            for m in ausleihliste:
                if isinstance(m, Hoerbuch) == True:
                    z=z+1
        return z
    
    def ermittleVormerkungen(self,bibNr):
        anzahl = 0
        for l in self.__leserliste:
            medien = ""
            eineVormerkliste = l.getVormerkliste()
            for m in eineVormerkliste:
                if m.getBibNr() == bibNr:
                    anzahl += 1
        return anzahl
        


    def zeigeAlleVormerkungen(self):
        rueckgabe = ""
        for l in self.__leserliste:
            medien = ""
            eineVormerkliste = l.getVormerkliste()
            for m in eineVormerkliste:
                medien = medien  + str(m.getBibNr()) + ","
            lnr = l.getLeserNr()
            leserzeile = str(lnr) + " : " + str(medien)
            rueckgabe = rueckgabe +leserzeile + "\n"
        return rueckgabe


      



class Main():
    def __init__(self):  
        self._stadtbibliothek=Bibliothek()
        
    def erstelleMedien(self):
        self._stadtbibliothek.erstelleBuch(1,"Harry Potter",523)
        self._stadtbibliothek.erstelleBuch(2,"Die Glocke",523)
        self._stadtbibliothek.erstelleHoerbuch(3,"Harry Potter I",62)
        self._stadtbibliothek.erstelleHoerbuch(4,"Harry Potter II",64)
    def erstelleLeser(self):
        self._stadtbibliothek.erstelleLeser(1,"Huber","Hans")
        self._stadtbibliothek.erstelleLeser(2,"Lehmann","Franz")
    def ausleihen(self):
        self._stadtbibliothek.ausleihenMedium(1,1) #(bibNr, LeserNr)
        self._stadtbibliothek.ausleihenMedium(3,1)
        self._stadtbibliothek.ausleihenMedium(4,1)
    def hatGeliehen(self):
        r=self._stadtbibliothek.anzeigenAusleihe(1,1) #(bibNr, LeserNr)
        if r: print("ausgeliehen")
        else : print("nicht ausgeliehen")
    def verlieheneHoerbuecher(self):
        z=self._stadtbibliothek.anzeigenAusgeliehenHoerbuecher()
        print("Verliehene Hörbücher: "+str(z))
    def vormerken(self):
        self._stadtbibliothek.vormerkenMedium(1,1) #(bibNr, LeserNr)
        self._stadtbibliothek.vormerkenMedium(3,1)
        self._stadtbibliothek.vormerkenMedium(4,1)
        self._stadtbibliothek.vormerkenMedium(4,2)
        self._stadtbibliothek.vormerkenMedium(2,2)
    def anzeigenVormerkungen(self):
        v=self._stadtbibliothek.zeigeAlleVormerkungen()
        print("Vormerkungen: \n"+v)
    def ermittleVormerkungen(self):
        print(str(self._stadtbibliothek.ermittleVormerkungen(4)))
    
        

main = Main()
main.erstelleMedien()
main.erstelleLeser()
main.ausleihen()
main.hatGeliehen()
main.verlieheneHoerbuecher()
main.vormerken()
main.ermittleVormerkungen()