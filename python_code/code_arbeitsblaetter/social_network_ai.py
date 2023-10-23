from abc import ABC, abstractmethod

class Person:
    def __init__(self, nachname='', vorname=''):
        self.nachname = nachname
        self.vorname = vorname

    def getNachname(self):
        return self.nachname

    def getVorname(self):
        return self.vorname
    
    def getPassword(self, sentence):
        word = ""
        for i in range(len(sentence)):
            if i == 0:
                word += sentence[i]
            if sentence[i] == " ":
                word += sentence[i + 1]
            word.lower()

        password = ""
        for i in range(len(word)):
            if i % 2 == 0:
                password += word[i].upper()
            else:
                password += word[i].lower()
        print(password)
        return password

class Nachricht(ABC):
    def __init__(self, absender):
        self.likes = 0
        self.absender = absender
        self.kommentare = []

    def hinzufuegenLike(self):
        self.likes += 1

    def hinzufuegenKommentar(self, kommentar):
        self.kommentare.append(kommentar)

    @abstractmethod
    def getNachricht(self):
        pass

class Textnachricht(Nachricht):
    def __init__(self, nachricht='', absender=''):
        super().__init__(absender)
        self.nachricht = nachricht

    def getNachricht(self):
        return self.nachricht

class SozialesNetzwerk:
    def __init__(self):
        self.mitglieder = []
        self.nachrichten = []

    def hinzufuegenMitglied(self, person):
        self.mitglieder.append(person)

    def hinzufuegenNachricht(self, nachricht):
        self.nachrichten.append(nachricht)

    def getAlleNachrichten(self):
        return self.nachrichten
    
class Kommentar:
    def __init__(self, absender, text):
        self.absender = absender
        self.text = text

    def getAbsender(self):
        return self.absender

    def getText(self):
        return self.text

if __name__ == "__main__":
    person1 = Person("Mustermann", "Max")
    person1.getPassword("Hi i bims und das ist mein Passwort")
    person2 = Person("Schmidt", "Maria")

    netzwerk = SozialesNetzwerk()
    netzwerk.hinzufuegenMitglied(person1)
    netzwerk.hinzufuegenMitglied(person2)

    nachricht1 = Textnachricht("Hallo, wie geht es euch?", person1)
    nachricht2 = Textnachricht("Gut, danke!", person2)
    nachricht1.hinzufuegenLike()
    nachricht1.hinzufuegenLike()
    nachricht2.hinzufuegenLike()
    nachricht2.hinzufuegenKommentar(Kommentar(Person("Schmidt", "Petra"), "Lüge!!11!"))

    netzwerk.hinzufuegenNachricht(nachricht1)
    netzwerk.hinzufuegenNachricht(nachricht2)

    for nachricht in netzwerk.getAlleNachrichten():
        print(f"{nachricht.absender.getVorname()} {nachricht.absender.getNachname()}: {nachricht.getNachricht()} Likes: {nachricht.likes}")
        for kommentar in nachricht.kommentare:
            print(f"Kommentar: {kommentar.getText()} Kommentator: {kommentar.getAbsender().getVorname()}")