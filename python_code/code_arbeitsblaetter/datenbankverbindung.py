import mysql.connector
from mysql.connector import errorcode



try:
  cnx = mysql.connector.connect(user='root',
                                database='obsthandel')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    query = ('SELECT Vorname FROM kunde WHERE Hausnummer = 33')
    add_kunde = ("INSERT INTO kunde "
               "(Kd_ID, Vorname, Name, Strasse, Hausnummer, OID) "
               "VALUES (%s, %s, %s, %s, %s, %s)")
    data_kunde = (200, 'Geert', 'Vanderkelen', "Holzweg", 3, 1)
    cursor = cnx.cursor()
    cursor.execute(add_kunde, data_kunde)
    for kunde in cursor:
        print(kunde)
    cursor.close()
    cnx.close()

