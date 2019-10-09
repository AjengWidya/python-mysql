# Referensi: https://www.petanikode.com/python-mysql/

import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "",
  database = "akademik"
)

def home(mydb):
    print("=================================================")
    print("\t\tDaftar Mahasiswa")
    print("=================================================")

    cursor = mydb.cursor()
    query = "SELECT * FROM mahasiswa"
    cursor.execute(query)
    results = cursor.fetchall()

    for data in results:
        print(data)

    print("1. Tambah")
    print("2. Sunting")
    print("3. Hapus")
    print("0. Keluar")
    menu = int(input("Pilih menu (tuliskan angka tanpa titik): "))

    if menu == 1:
        create(mydb)
    elif menu == 2:
        update(mydb)
    elif menu == 3:
        delete(mydb)
    elif menu == 0:
        print("Terima kasih telah mencoba aplikasi CRUD!")
        exit()
    else:
        print("Invalid!")

def create(mydb):
    nim = input("NIM: ")
    nama = input("Nama Lengkap: ")
    prodi = input("Program Studi: ")
    data = (nim, nama, prodi)
    cursor = mydb.cursor()
    query = "INSERT INTO mahasiswa (nim, nama, prodi) VALUES (%s, %s, %s)"
    cursor.execute(query, data)
    mydb.commit()

    print("Berhasil menyimpan data!")

def update(mydb):
    cursor = mydb.cursor()
    print("1. Ubah Nama")
    print("2. Ubah Program Studi")
    print("3. Ubah Nama dan Program Studi")
    menu = int(input("Pilih menu (tuliskan angka tanpa titik): "))
    
    if menu == 1:
        nim_input = input("Masukkan NIM: ")
        nama_new = input("Nama Lengkap (Baru): ")
        data = (nama_new, nim_input)
        query = "UPDATE mahasiswa SET nama = %s WHERE nim = %s"
        cursor.execute(query, data)
        mydb.commit()
    elif menu == 2:
        nim_input = input("Masukkan NIM: ")
        prodi_new = input("Program Studi (Baru): ")
        data = (prodi_new, nim_input)
        query = "UPDATE mahasiswa SET prodi = %s WHERE nim = %s"
        cursor.execute(query, data)
        mydb.commit()
    elif menu == 3:
        nim_input = input("Masukkan NIM: ")
        nama_new = input("Nama Lengkap (Baru): ")
        prodi_new = input("Program Studi (Baru): ")
        data = (nama_new, prodi_new, nim_input)
        query = "UPDATE mahasiswa SET nama = %s, prodi = %s WHERE nim = %s"
        cursor.execute(query, data)
        mydb.commit()
    
    print("Data berhasil diubah!")

def delete(mydb):
    cursor = mydb.cursor()
    nim_input = input("Masukkan NIM: ")
    data = (nim_input, )
    query = "DELETE FROM mahasiswa WHERE nim = %s"
    cursor.execute(query, data)
    mydb.commit()
    print("Data berhasil dihapus!")


# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == "__main__":
  while(True):
    home(mydb)