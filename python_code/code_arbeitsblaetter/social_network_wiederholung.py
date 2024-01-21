# soziales netzwerk, person, nachricht, textnachricht

from abc import abstractmethod, ABC
class SozialesNetzwerk:
    def __init__(self):
        self.mitgliederliste=[]
        self.nachrichtenliste=[]
    
    def hinzufuegenMitglied(self, person):
        self.mitgliederliste.append(person)

    def hinzufuegenNachricht(self, nachricht):
        self.nachrichtenliste.append(nachricht)

    def getAlleNachrichten(self):
        gesamtnachricht = ""
        for nachricht in self.nachrichtenliste:
            gesamtnachricht += nachricht.getNachricht()
        return gesamtnachricht

    def getPassword(satz):
        password = ""
        password += satz[0]
        for i in range(len(satz)):
            if satz[i] == " ":
                password += satz[i+1]
        newPassword = ""
        for i in range(len(password)):
            if i % 2 == 0:
                newPassword += password[i].upper()
            else:
                newPassword += password[i].lower()
        
        return newPassword
        


class Person:
    def __init__(self):
        pass
    def __init__(self, nachname, vorname):
        self.__nachname = nachname
        self.__vorname = vorname
    def getNachname(self):
        return self.__nachname
    def getVorname(self):
        return self.__vorname
       
class Nachricht(ABC):
    def __init__(self):
        self._likes = 0
        self._absender = None
        self.__kommentare = []
    def __init__(self, absender):
        self._likes = 0
        self._absender = absender
        self.__kommentare = []
    
    def hinzufuegenLike(self):
        self._likes += 1
    def hinzufuegenKommentar(self, kommentar):
        self.__kommentare.append(kommentar)

    @abstractmethod
    def getNachricht():
        pass

class Textnachricht(Nachricht):
    def __init__(self):
        pass
    def __init__(self, nachricht, absender):
        super().__init__(absender)
        self.__nachricht = nachricht
    def getNachricht(self):
        return f"{self._absender.getNachname()} {self._absender.getVorname()}: {self.__nachricht} Likes: {self._likes}"

class Kommentar(Nachricht):
    def __init__(self, absender, kommentartext):
        super().__init__(absender)
        self.__kommentartext = kommentartext
    def getAbsender(self):
        return self.__absender
    def getKommentartext(self):
        return self.__kommentartext


    

# Netzwerk = SozialesNetzwerk()
# Person1 = Person("Vogl", "Elias")
# Person2 = Person("Ötzel", "Nico")
# Netzwerk.hinzufuegenMitglied(Person1)
# Netzwerk.hinzufuegenMitglied(Person2)
# Nachricht1 = Textnachricht("Halli", Person1)
# Nachricht2 = Textnachricht("Hallo", Person2)
# Nachricht1.hinzufuegenLike()
# Netzwerk.hinzufuegenNachricht(Nachricht1)
# Netzwerk.hinzufuegenNachricht(Nachricht2)
# print(Netzwerk.getAlleNachrichten())
Netzwerk = SozialesNetzwerk
print(Netzwerk.getPassword("HI i Bims DA MÜSCHA"))