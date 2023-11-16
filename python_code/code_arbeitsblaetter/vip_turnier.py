from abc import ABC, abstractmethod

class Karte:
    def __init__(self, grundPreis, kaufTag, spielTag):
        self.__grundPreis = grundPreis
        self.__kaufTag = kaufTag
        self.__spielTag = spielTag
    
class Kunde(ABC):
    def __init__(self, name):
        self.__name = name
        self.__karten = []
    def berechneKartenPreis():
        pass
    def kaufeKarte():
        pass

class VIPKunde(Kunde):
    def __init__(self, name, telefonNummer):
        super().__init__(name)
        self.__telefonN = telefonNummer
    
    def __init__(self, name, telefonNummer, VIPFreunde):
        super().__init__(name)
        self.__telefonN = telefonNummer
        self.__VIPFreunde = VIPFreunde

    def berechneKartenPreis():
        pass