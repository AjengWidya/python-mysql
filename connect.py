# Referensi: https://www.petanikode.com/python-mysql/

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "",
  database = "akademik"
)

if mydb.is_connected():
    print("Berhasil terhubung ke database")