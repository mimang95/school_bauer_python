from abc import ABC, abstractmethod

class SymmetrischeCodierverfahren(ABC):
    def __init__(self):
        self._klarText = ""
        self._privateKey = ""
    
    def setPivateKey(self, key):
        self._privateKey = key
    
    def getKlarText(self):
        return self._klarText

    def setKlarText(self, text):
        self._klarText = text

    @abstractmethod
    def codieren():
        pass

class Vigenere(SymmetrischeCodierverfahren):
    
    def codieren(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        code_word = ""
        i = 0
        while len(code_word)<len(self._klarText):
            code_word += self._privateKey[i%len(self._privateKey)]
            i += 1

        kodiertes_wort = ""
        for i in range(len(self.getKlarText())):
            num = (alphabet.index(self.getKlarText()[i]) + alphabet.index(code_word[i]))%26
            kodiertes_wort += alphabet[num]
        return kodiertes_wort


vigenere = Vigenere()
vigenere.setKlarText("DERADLERISTGELANDET")
vigenere.setPivateKey("PRUEFUNG")
print(vigenere.codieren())