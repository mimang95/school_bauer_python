class Teilnehmer:
    def __init__(self, email):
        self.__email = email
    def getEmail(self):
        return self.__email
    
class Fortbildung:
    def __init__(self):
        self.__teilnehmerliste = []

    def getTeilnehmerliste(self):
        return self.__teilnehmerliste

    def sendeEmail(self, emailadresse, nachricht):
        pass
    
class OnlienFortbildung(Fortbildung):
    def __init__(self):
        self.__link = "http://blabla"

# die folgende Methode ist die Lösung für die Aufgabe
    def sendeLink(self):
        teilnehmerliste = self.getTeilnehmerliste()
        for teilnehmer in teilnehmerliste:
            emailadresse = teilnehmer.getEmail()
            self.sendeEmail(emailadresse, self.__link)

# Entwurfsmuster sind bewährte Lösungsschablonen für wiederkehrende Entwurfsprogbleme in der Softwarearchitektur und -entwicklung.
# Sie stellen damit eine wiederverwendbare Vorlage ur Problemlösung dar, die in einem bestimmten Zusammenhang einsetzbar ist
# Observer Pattern: Der Beobachter reicht Änderung an einem Objekt an Strukturen weiter, die vom Ursprungsobjekt abhängen

