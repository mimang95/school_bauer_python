import os
import csv
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="montage"
)

cursor = db_connection.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Artikel (
            Nr INT PRIMARY KEY,
            Bezeichnung VARCHAR(255),
            Preis DECIMAL(10, 2),
            GID INT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Gruppe (
            GID INT PRIMARY KEY,
            Bezeichnung VARCHAR(255)
        )
    """)

def insert_data(csv_path):
    with open(csv_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        next(csv_reader)
        for row in csv_reader:
            cleaned_row = [cell.strip() for cell in row]
            print(cleaned_row)
            nr, bezeichnung, preis, gruppe = cleaned_row
            print(nr)
            preis = preis.replace(' €', '').replace(',', '.')
            print(preis)
            cursor.execute("INSERT INTO Gruppe (Bezeichnung) VALUES (%s, %s)", (1, gruppe))
            cursor.execute("INSERT INTO Artikel (Nr, Bezeichnung, Preis, GID) VALUES (%s, %s, %s, %s)",
                           (int(nr), bezeichnung, preis, 1))

# def getGruppe(self, gruppe):
#     query = '''select gid
#     from gruppe
#     where bezeichnung = %s'''
#     cur.execute(query, (gruppe, ))
#     try:
#         gid = cur.fetchone(query, )

def main():
    create_table()
    csv_path = "./python_code/code_arbeitsblaetter/montage.csv"
    insert_data(csv_path)
    db_connection.commit()

    cursor.close()
    db_connection.close()

if __name__ == "__main__":
    main()
