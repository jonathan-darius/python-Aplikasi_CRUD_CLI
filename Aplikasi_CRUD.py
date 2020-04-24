import mysql.connector

nama_database = 'test_crud'

db = mysql.connector.connect(
    host='localhost',
    user='root',
    database= nama_database,
    password=''
)

def insert_data(db):
    nama = input("Masukan nama: ")
    alamat = input("Masukan alamat: ")
    val = (nama, alamat)
    cursor = db.cursor()
    sql = "INSERT INTO pelanggan (nama, alamat) VALUES (%s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data sudah disimpan".format(cursor.rowcount))

def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM pelanggan"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        print("==================================")
        print("List Data Pada Tabel")
        for data in results:
            print(data)
        print("==================================")


def update_data(db):
    cursor = db.cursor()
    show_data(db)
    id = input("Pilih ID Pelanggan> ")
    nama = input("Nama baru: ")
    alamat = input("Alamat baru: ")

    sql = "UPDATE pelanggan SET nama=%s, alamat=%s WHERE id=%s"
    val = (nama, alamat, id)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))

def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    id = input("pilih id pelanggan> ")
    sql = "DELETE FROM pelanggan WHERE id=%s"
    val = (id,)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))

def cari_data(db):
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM pelanggan WHERE nama LIKE %s OR alamat LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        print("==================================")
        print("Hasil Pencarian : ")
        for data in results:
            print(data)
        print("==================================")

def main(db):
    print("=== CRUD DATABASE VERSI PYTHON ===")
    print("1. Memasukan Data")
    print("2. Menampilkan Data")
    print("3. Memperbaharui Data")
    print("4. Menghapus Data")
    print("5. Mencari Data")
    print("0. Keluar")
    print("==================================")
    menu = input("Masukkan Nomor Perintah>")


    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        cari_data(db)
    elif menu == "0":
        exit()
    else:
        print("Perintah Salah!!! Tolong Dicoba Kembali")

if __name__ == '__main__':
    while(True):
        main(db)