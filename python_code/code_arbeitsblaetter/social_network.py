class Person:
    def __init__(self):
        pass
    def __init__(self, nn, vn):
        self.__nachname = nn
        self.__vorname = vn

    def getNachname(self):
        return self.__nachname
    
    def getVorname(self):
        return self.__vorname


mitglieder = []
nachrichten = []
class SozialesNetzwerk:
    def hinzufuegenMitglied(self, person):
        mitglieder.append(person)

    def hinzufuegenNachricht(self, nachricht):
        nachrichten.append(nachricht)
    
    def getAlleNachrichten(self):
        for nachricht in nachrichten:
            print(nachricht, " ")

class Nachricht:
    def __init__(self):
        pass
    def __init__(self, likes):
        self._likes = likes
    def hinzufuegenLike(self):
        self.likes += 1
    

class Textnachricht(Nachricht):
    pass