import urllib.request  # buat download file dari URL

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/PET_Tables/PETSHOP.csv"
urllib.request.urlretrieve(url, "PETSHOP.csv")  # simpan CSV ke folder lab ini

print("Download selesai!")

import subprocess  # buat jalankan command sqlite-utils dari dalam Python

# insert CSV ke database petshop.db, otomatis bikin tabel PETSHOP + infer tipe data
subprocess.run(["sqlite-utils", "insert", "petshop.db", "PETSHOP", "PETSHOP.csv", "--csv"])

print("PETSHOP.csv berhasil dimuat ke petshop.db")

url_sql = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/Datasetteoptionallabs/Week2/data/BookShop-CREATE-INSERT.sql"
urllib.request.urlretrieve(url_sql, "BookShop-CREATE-INSERT.sql")

print("File SQL script berhasil didownload!")

# baca isi file .sql lalu eksekusi ke database yang sama (petshop.db)
with open("BookShop-CREATE-INSERT.sql", "r") as f:
    sql_script = f.read()  # baca semua isi script SQL

import sqlite3  # modul database bawaan Python, tidak perlu install

conn = sqlite3.connect("petshop.db")  # connect ke database yang sudah ada
conn.executescript(sql_script)         # eksekusi seluruh script (CREATE + INSERT sekaligus)
conn.commit()                          # simpan perubahan
conn.close()                           # tutup koneksi

print("BookShop berhasil dibuat & dimuat ke petshop.db")