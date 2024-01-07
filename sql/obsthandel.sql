'a)'
SELECT ware.WID, Bezeichnung, Menge, Preis AS Einzelpreis, (Menge*Preis) AS Gesamtpreis
FROM ware
INNER JOIN warenbestellung ON ware.WID = warenbestellung.WID
WHERE warenbestellung.BID = 1

'b'
SELECT BID, datum, kunde.Kd_ID, kunde.Vorname, kunde.Name, kunde.Strasse, kunde.Hausnummer FROM bestellung
INNER JOIN kunde ON kunde.Kd_ID = bestellung.KID 
WHERE bezahlt = 0

'c'
SELECT BID, Sum(menge*preis) as 'Rechnungsbetrag'
FROM warenbestellung
INNER JOIN ware ON warenbestellung.WID = ware.WID
GROUP BY BID

'd'
SELECT SUM(preis*warenbestellung.Menge) as 'Umsatz', kunde.Vorname, kunde.Name
FROM ware
INNER JOIN warenbestellung ON ware.WID = warenbestellung.WID
INNER JOIN bestellung ON bestellung.BID = warenbestellung.BID
INNER JOIN kunde ON kunde.Kd_ID = bestellung.KID
GROUP BY(KID)
ORDER BY Umsatz desc

'e'
SELECT 

'f'
SELECT bezeichnung, COUNT(*) AS Anzahl
FROM ware
INNER JOIN warenbestellung ON ware.WID = warenbestellung.WID
GROUP BY ware.WID
HAVING COUNT(*) > 3

'g'
INSERT INTO ware(preis, Verpackungseinheit, Bezeichnung) VALUES(3.99,"schale","Himbeere")

'h'
INSERT INTO bestellung(KID, Datum, bezahlt) VALUES(5, '2023-12-01', 0)
INSERT INTO warenbestellung(WID, BID, Menge) VALUES(9, 5, 3)

'i'
CREATE TABLE verpackung(VP_ID INT AUTO_INCREMENT, bezeichnung VARCHAR(45), material VARCHAR(45), PRIMARY KEY(VP_ID)) 

'j'
ALTER TABLE ware DROP COLUMN Verpackungseinheit
ALTER TABLE ware ADD COLUMN(VP_ID INT)