from abc import ABC,abstractmethod
class Werkzeug(ABC):
    def __init__(self, art, verschleiss):
        self.__art=art
        if verschleiss >= 0 and verschleiss <= 100:
            self._verschleiss = verschleiss
        else:
            self._verschleiss = 0

    @abstractmethod
    def ausgeben(self):
        pass

class Bohrer(Werkzeug):
    def __init__(self,art, verschleiss, groesse):
        super().__init__(art,verschleiss)
        self.__groesse = groesse
    def ausgeben(self):
            print("Bohrer mit Größe "+str(self.__groesse)+" (Verschleiß "+str(self._verschleiss)+" %)")

class Industrieroboter:
    def __init__(self):
        self.__maxAnzahlWerkzeuge = 10
        self.__werkzeugKasten = []
        for i in range(self.__maxAnzahlWerkzeuge):
             self.__werkzeugKasten.append(None)

    def werkzeugHinzufuegen(self,platz, neu):
            if platz >= 0 and platz < self.__maxAnzahlWerkzeuge:
                if self.__werkzeugKasten[platz] == None:
                    self.__werkzeugKasten[platz] = neu
                    print("Hinzugefügtes Werkzeug auf Platz " + str(platz) + ": ")
                    neu.ausgeben()
                    return True
                else:
                    print("Hinzufügen nicht möglich, da Platz " + str(platz) + " belegt ist.")
            else:
                print("Hinzufügen nicht möglich, da Platz " + str(platz) + " nicht existiert.");
            return False
    
    def werkzeugEntfernen(self, platz):
            if platz >= 0 and platz < self.__maxAnzahlWerkzeuge:
                if self.__werkzeugKasten[platz] != None:
                    print("Entferntes Werkzeug auf Platz " + str(platz) + ": ")
                    self.__werkzeugKasten[platz].ausgeben()
                    self.__werkzeugKasten[platz] = None
                    return True
                else:
                    print("Entfernen nicht möglich, da Platz " + str(platz) + " belegt ist.")
            else:
                print("Entfernen nicht möglich, da Platz " + str(platz) + " nicht existiert.")
            return False
    
r1 = Industrieroboter()
b1 = Bohrer("Bohrer", 0, 10)
b2 = Bohrer("Bohrer", 0, 10)

r1.werkzeugHinzufuegen(5,b1)
r1.werkzeugHinzufuegen(5,b2)
r1.werkzeugHinzufuegen(10, b2)
r1.werkzeugHinzufuegen(-1, b2)
r1.werkzeugEntfernen(5)
r1.werkzeugEntfernen(5)
r1.werkzeugEntfernen(10)
r1.werkzeugEntfernen(-1)

        

    