# Referensi: https://www.petanikode.com/python-mysql/

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "Ajgwdyayu05",
  database = "akademik"
)

mycursor = mydb.cursor()
query = """ CREATE TABLE mahasiswa (
              nim CHAR(9) PRIMARY KEY,
              nama VARCHAR(50),
              prodi VARCHAR(30)
            )
        """
mycursor.execute(query)

print("Tabel berhasil dibuat!")