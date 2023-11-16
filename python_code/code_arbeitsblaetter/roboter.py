from abc import ABC, abstractmethod

class Industrieroboter:
    def __init__(self):
        self.__maxAnzWerkzeuge = 10
        self.__werkzeugKasten = [None for i in range(self.__maxAnzWerkzeuge)]
    def werkzeugHinzufügen(self, platz, neu):
        if platz < 0 or platz > self.__maxAnzWerkzeuge-1:
            print(f"Hinzufügen nicht möglich, da Platz {platz} nicht existiert")
            return False
        if self.__werkzeugKasten[platz]:
            print("Hinzufügen nicht möglich da Platz belegt")
            return False
        self.__werkzeugKasten[platz] = neu
        print(f"Werkzeug an Platz {platz} hinzugefügt")
        return True

    def werkzeugEntfernen(self, platz):
        if platz < 0 or platz > self.__maxAnzWerkzeuge-1:
            print(f"Löschen nicht möglich, da Platz {platz} nicht existiert")
            return False
        if not self.__werkzeugKasten[platz]:
            print("Löschen nicht möglich da Platz nicht belegt")
            return False
        self.__werkzeugKasten[platz] = None
        print(f"Werkzeug an Platz {platz} wurde entfernt")
        return True
                    

class Werkzeug(ABC):
    def __init__(self, art, verschleiss):
        self.__art = art
        self._verschleiss = verschleiss
    
    @abstractmethod
    def ausgeben():
        pass

class Bohrer(Werkzeug):
    def __init__(self, art, verschleiss, groesse):
        super().__init__(art, verschleiss)
        self.__groesse = groesse
    
    def ausgeben(self):
        print(f"Bohrer mit Groesse {self.__groesse} (Verschleiss {self._verschleiss}.)")

class Greifer(Werkzeug):
    def ausgeben(self):
        print(f"Greifer (Verschleiss {self._verschleiss}.)")

class Schweisser(Werkzeug):
    def ausgeben(self):
        print(f"Schweisser (Verschleiss {self._verschleiss}.)")


if __name__=="__main__":
    roboter = Industrieroboter()
    b1 = Bohrer(10, "Metallbohrer", 0 )
    b2 = Bohrer(10, "DiaBohrer", 0 )
    roboter.werkzeugHinzufügen(5,b1)
    roboter.werkzeugHinzufügen(5,b2)
    roboter.werkzeugHinzufügen(10,b2)
    roboter.werkzeugHinzufügen(-1,b2)
    roboter.werkzeugEntfernen(5)
    roboter.werkzeugEntfernen(5)
    roboter.werkzeugEntfernen(10)
    roboter.werkzeugEntfernen(-1)