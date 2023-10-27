from abc import ABC, abstractmethod

class Patient():
    def __init__(self, kvNummer, name, vorname):
        self.__kvNummer = kvNummer
        self.__name = name
        self.__vorname = vorname

        def getKvNummer(self):
            return self.__kvNummer
        
        def getName(self):
            return self.__name
        
        def getVorname(self):
            return self.__vorname
        
class Behandlung(ABC):
    def __init__(self):
        pass
    def __init__(self, kvNummer, beschreibung, kostensatz):
        self.__kvNummer = kvNummer
        self.__beschreibung = beschreibung
        self.__kostensatz = kostensatz

    def getKvNummer(self):
        return self.__kvNummer
    def getBeschreibung(self):
        return self.__beschreibung
    def getKostensatz(self):
        return self.__kostensatz

    @abstractmethod
    def getKosten():
        pass

class Standardbehandlung(Behandlung):
    def __init__(self):
        pass
    def __init__(self, kvNummer, beschreibung, kostensatz):
        super().__init__(kvNummer, beschreibung, kostensatz)
        
    def getKosten(self):
        return self.getKostensatz()

class Physiobehandlung(Behandlung):
    def __init__(self):
        pass
    def __init__(self, kvNummer, beschreibung, kostensatz):
        super().__init__(kvNummer, beschreibung, kostensatz)
        
    def getKosten(self):
        return self.getKostensatz() * 1.5

class Praxis():
    def __init__(self):
        pass
    def __init__(self, patienten, behandlungen):
        self.__patienten = patienten
        self.__behandlungen = behandlungen
    
    def getPatient(self, name):
        patient_name = []
        for patient in self.__patienten:
            if patient.name == name:
                patient_name.append(patient)
        return patient_name
    
    def getBehandlungen(self, kvNummer):
        behandlungsliste = []
        for behandlung in self.__behandlungen:
            if behandlung.getKvNr() == kvNummer:
                behandlungsliste.append(behandlung)
        return behandlungsliste
        
    def anzBehandlungen(self, kvNummer):
        behandlungen = self.getBehandlungen(kvNummer)
        return len(behandlungen)
    
    def zeigePatienten(self, anzBehandlungen):
        patienten = []
        string = ""
        for patient in self.__patienten:
            if patient.anzBehandlungen(patient.getKvNr()) >= anzBehandlungen:
                patienten.append(patient)
        for patient in patienten:
            string += patient.getName()
            string += ";"

    def addBehandlung(self, b):
        self.__behandlungen.append(b)
    
    def ermittleKosten(self):
        kosten = 0
        for behandlung in self.__behandlungen:
            kosten += behandlung.getKosten()
        return kosten

if __name__ == "__main__":
    p1 = Patient("A12345", "Schwammkopf", "SpongeBob")
    b1 = Physiobehandlung("A12345", "Chirogymnastik", 12.87)
    b2 = Physiobehandlung("A12345", "Wärmeanwendung", 4.23)
    b3 = Standardbehandlung("A12345", "Arthrose", 45.12)
    b4 = Standardbehandlung("A12345", "Ultraschall", 26.80)
    praxis = Praxis([], [])
    praxis.addBehandlung(b1)
    praxis.addBehandlung(b2)
    praxis.addBehandlung(b3)
    praxis.addBehandlung(b4)
    print(praxis.ermittleKosten())

# Lösung: 97.57 -> korrekt