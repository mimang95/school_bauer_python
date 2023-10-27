from abc import ABC, abstractmethod
class Adresse():
    def __init__(self, plz, ort, strasse):
        self.__plz = plz
        self.__ort = ort
        self.__strasse = strasse
    
    def GetAdressdaten(self):
        return f"Postleitzahl: {self.__plz} Ort: {self.__ort} Straße: {self.__strasse}"

class Wohngebaeude(ABC):
    def __init__(self, baujahr, adresse):
        self.__baujahr = baujahr
        self.__adresse = adresse
    def GetGebaeudedaten(self):
        return f"Baujahr: {self.__baujahr}, {self.__adresse.GetAdressdaten()}"
    
    @abstractmethod
    def BerechneMietpreis():
        pass

class Mehrfamilienhaus(Wohngebaeude):
    def __init__(self, anzahlEtagen, anzahlWohneinheiten, wohneinheitenliste, adresse, baujahr):
        super().__init__(baujahr, adresse)
        self.__anzahlEtagen = anzahlEtagen
        self.__anzahlWohneinheiten = anzahlWohneinheiten
        self.__wohneinheitenliste = wohneinheitenliste
    
    def getAnzahlEtagen(self):
        return self.__anzahlEtagen
    def getAnzahlWohneinheiten(self):
        return self.__anzahlWohneinheiten
    def addWohneinheit(self, etage, wohnung):
        if etage > 0 and etage <= self.getAnzahlEtagen():
            self.__wohneinheitenliste.append(wohnung)
            self.__anzahlWohneinheiten += 1
    def BerechneMietpreis(self):
        mietpreis = 0
        for wohnung in self.__wohneinheitenliste:
            mietpreis += wohnung.MietpreisWohneinheit()
        return mietpreis
    
class Wohneinheit():
    def __init__(self, anzahlZimmer, preisProQM, anzahlQM):
        self.__anzahlZimmer = anzahlZimmer
        self.__preisProQM = preisProQM
        self.__anzahlQM = anzahlQM
    
    def MietpreisWohneinheit(self):
        mietpreis = self.__anzahlQM * self.__preisProQM
        if self.__anzahlZimmer > 2:
            mietpreis + 50 * (self.__anzahlZimmer - 2)
        return mietpreis

class Einfamilienhaus(Wohngebaeude):
    def __init__(self, baujahr, adresse, wohneinheit):
        super().__init__(baujahr, adresse)
        self.__wohneinheit = wohneinheit
    def BerechneMietpreis(self):
        return self.__wohneinheit.MietpreisWohneinheit()

class Gebaeudeverwaltung():
    def __init__(self, name, gebaeudeListe):
        self.__name = name
        self.__gebaeudeListe = gebaeudeListe
    
    def AddGebaeude(self, gebaeude):
        self.__gebaeudeListe.append(gebaeude)

    def AusgabeMietGebaeudedaten(self):
        gebaeudedaten = ""
        for gebaeude in self.__gebaeudeListe:
            gebaeudedaten += gebaeude.GetGebaeudedaten() + " \n"
        return gebaeudedaten

    def BerechneGesamtMiete(self):
        gesamtMietPreis = 0
        for gebaeude in self.__gebaeudeListe:
            gesamtMietPreis += gebaeude.BerechneMietpreis()
        return gesamtMietPreis

if __name__ == "__main__":
    adresse1 = Adresse("70178", "Stuttgart", "Sindelfingerstr. 128")
    adresse2 = Adresse("71106", "Leonberg", "Stuttgarterstr. 87")
    mehrfamilienhaus = Mehrfamilienhaus(4, 0, [], adresse1, "01.01.1995")
    wohneinheit1 = Wohneinheit(3, 9.5, 80)
    wohneinheit2 = Wohneinheit(4, 10.5, 120)
    mehrfamilienhaus.addWohneinheit(1, wohneinheit1)
    mehrfamilienhaus.addWohneinheit(1, wohneinheit2)
    mehrfamilienhaus.addWohneinheit(2, wohneinheit1)
    mehrfamilienhaus.addWohneinheit(2, wohneinheit1)
    mehrfamilienhaus.addWohneinheit(3, wohneinheit1)
    mehrfamilienhaus.addWohneinheit(3, wohneinheit2)
    mehrfamilienhaus.addWohneinheit(4, wohneinheit1)
    mehrfamilienhaus.addWohneinheit(4, wohneinheit2)
    wohneinheit3 = Wohneinheit(5, 11.5, 140)
    einfamilienhaus = Einfamilienhaus("01.01.2005", adresse2, wohneinheit3)
    gebaeudeverwaltung = Gebaeudeverwaltung("RentYourHome", [])
    gebaeudeverwaltung.AddGebaeude(einfamilienhaus)
    gebaeudeverwaltung.AddGebaeude(mehrfamilienhaus)
    print(gebaeudeverwaltung.AusgabeMietGebaeudedaten())
    print(gebaeudeverwaltung.BerechneGesamtMiete())
    