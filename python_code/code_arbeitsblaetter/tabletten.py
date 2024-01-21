from abc import ABC, abstractmethod


'''
Polymorphie bedeutet, dass unterschiedliche Klassen die gleiche Methode(eine Methode mit dem gleichen Namen) unterschiedlich implementieren können.
In diesem Beispiel ist die Methode wirkstofffreisetzung in der Klasse Tablettenform und der Klasse Kapselform implementiert. 
Allerdings funktionieren die Methoden möglicherweise in beiden Klassen etwas unterschiedlich. 
'''
class Medikament:
    def __init__(self, haltbarkeitsdatum, name, wirksamkeit, formInfos):
        self.__haltbarkeitsdatum = haltbarkeitsdatum
        self.__name = name
        self.__wirksamkeit = wirksamkeit
        self.__arzneiForm = formInfos
    
    def getHaltbarkeitsdatum(self):
        return self.__haltbarkeitsdatum
    def setHaltbarkeitsdatum(self, x):
        self.__haltbarkeitsdatum = x
    def getName(self):
        return self.__name
    def setName(self, x):
        self.__name = x
    def getWirksamkeit(self):
        return self.__wirksamkeit
    def setWirksamkeit(self, x):
        self.__wirksamkeit = x
    def getArzneiForm(self):
        return self.__arzneiForm
    def setArzneiForm(self, x):
        self.__arzneiForm = x
        
# spalten = 5
# reihen = 2

# blister = [[True for j in range(spalten)] for i in range(reihen)]

class Blister:
    def __init__(self, anzahlReihen, anzahlSpalten, id, produzierteMedikamente):
        self.__anzahlMulden = anzahlReihen * anzahlSpalten
        self.__anzahlReihen = anzahlReihen
        self.__anzahlSpalten = anzahlSpalten
        self.__id = id
        self.__bestandInfo = [[True for j in range(anzahlSpalten)] for i in range(anzahlReihen)]
        self.__medikamente: list = produzierteMedikamente

    def getAnzahlMulden(self):
        return self.anzahlMulden
    def setAnzahlMulden(self, x):
        self.__anzahlMulden = x
    def getAnzahlReihen(self):
        return self.__anzahlReihen
    def setAnzahlReihen(self, x):
        self.__anzahlReihen = x
    def getAnzahlSpalten(self):
        return self.__anzahlSpalten
    def setAnzahlSpalten(self, x):
        self.__anzahlSpalten = x
    def getId(self):
        return self.__id
    def setId(self, x):
        self.__id = x
    def getBestandInfo(self):
        return self.__bestandInfo
    def setBestandInfo(self, x):
        self.__bestandInfo = x
    def getMedikamente(self):
        return self.__medikamente
    def setMedikamente(self, x):
        self.__medikamente = x


    def entnehmen(self, IndexReihe, IndexSpalte):
        if self.__bestandInfo[IndexReihe][IndexSpalte]:
            self.__bestandInfo[IndexReihe][IndexSpalte] = False
            return True
        else:
            return False
        
    
    def druckeBestandInfo(self):
        string = ""
        for i in range(self.__anzahlReihen):
            for mulde in self.__bestandInfo[i]:
                if mulde:
                    string += "O"
                else:
                    string += "X"
            string += "\n"
        print(string)



class Medikamentenform(ABC):
    def __init__(self, gewichtInG, laengeInMm, breiteInMm):
        self.__gewichtInG = gewichtInG
        self.__laengeInMm = laengeInMm
        self.__breiteInMm = breiteInMm
        self.__id = id

    def getGewichtInG(self):
        return self.__gewichtInG
    def setGewichtInG(self, x):
        self.__gewichtInG = x
    def getLaengeInMm(self):
        return self.__laengeInMm
    def setLaengeInMm(self, x):
        self.__laengeInMm = x
    def getBreiteInMm(self):
        return self.__breiteInMm
    def setBreiteInMm(self, x):
        self.__breiteInMm = x
    def getId(self):
        return self.__id
    def setId(self, x):
        self.id = x

    @abstractmethod
    def wirkstofffreisetzung(self):
        pass

class Tablettenform(Medikamentenform):
    def __init__(self, gewichtInG, laengeInMm, breiteInMm, id, pulverKoernung):
        super().__init__(gewichtInG, laengeInMm, breiteInMm)
        self.__pulverKoernungInUm = pulverKoernung

    def wirkstofffreisetzung(self):
        return "Freisetzung des Wirkstoffes durch Zersetzung der Tablette. Pulverkoernung in Mikrometer: " + self.__pulverKoernungInUm
    
tablette = Tablettenform(2, 8, 3, 1508, 200)
medikamenteliste = []
for i in range(60):
    medikament = Medikament("15.08.2025", "Eucaliptum", "Zur Schmerzlinderung bei Bronchialbeschwerden", 3101)
    medikamenteliste.append(medikament)

abgepackte_medikamente = []
for i in range(12):
    abgepackte_medikamente.append(medikamenteliste[i])

blister = Blister(2, 6, 2015, abgepackte_medikamente)
blister.entnehmen(0, 0)
blister.entnehmen(1, 4)
blister.druckeBestandInfo()

