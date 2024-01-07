# Wortliste, Wort, Wort mit lücke, Wortpuzzle, 
from abc import ABC, abstractmethod
from random import randint, shuffle
class WortListe:
    def __init__(self, aAnzahlWoerter, aldxGewaehltesWort, dasWort: list):
        self.__aAnzahlWoerter = aAnzahlWoerter
        self.__aldxGewaehltesWort = aldxGewaehltesWort
        self.dasWort = dasWort
    
    def testeLoesung(self, pWort):
        for wort in self.dasWort:
            if wort == pWort:
                pass

    def auswaehlenWort(self):
        rand_num = randint(0, len(self.__aAnzahlWoerter))
        wort_wahl = self.dasWort[rand_num]
        return wort_wahl
    
    def gibAufgabe():
        pass

class Wort(ABC):
    def __init__(self, aWort, aStatus):
        self._aWort = aWort
        self._aStatus = aStatus
    
    def setzeStatusAufNie(self):
        self._aStatus = 0
    def gibWort(self):
        return self._aWort
    def pruefeLoesung(self, pWort):
        if pWort == self._aWort:
            return True
        else:
            return False
    
    @abstractmethod
    def gibBuchstaben():
        pass

    def gibStatus(self):
        return self._aStatus

class WortMitLuecke(Wort):
    def __init__(self, pWort):
        self.pWort = pWort
    def gibBuchstaben():
        pass

class WortPuzzle(Wort):
    def __init__(self, pWort):
        self.pWort = pWort
    def gibBuchstaben(self):
        shuffled_word = shuffle(self.pWort)
        return shuffled_word       


shuffle(["H", "a", "l", "l", "o"])