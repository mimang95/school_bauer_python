# 2.1. Stichwort: Datenbanktransaktionen
# 2.2 -> leicht

# 2.3
ALTER TABLE Termin ADD COLUMN Link VARCHAR(255)

# 2.4
SELECT teilnehmer.tnr, name, vorname
FROM teilnehmer 
INNER JOIN Anmeldung ON teilnehmer.tnr = anmeldung.tnr
INNER JOIN Fortbidung ON fortbildung.fid = anmeldung.fid
INNER JOIN Termin ON fortbildung.fid = termin.fid
WHERE titel = 'Java' AND Untertitel = 'Grundkurs' AND Datum = '14.06.2023'

# 2.5
SELECT anmeldung.fid, titel, untertitel, COUNT(*) AS 'Anzahl'
FROM Fortbidung INNER JOIN Anmeldung ON Fortbildung.fid = Anmeldung.fid
GROUP BY(anmeldung.fid, titel, untertitel)
