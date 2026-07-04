# 1.4 - Accessing Databases using Python

**Lab: Mengakses Database menggunakan Python Script**
Course 3 - Python Project for Data Engineering (IBM Data Engineering Professional Certificate)

## Tujuan Lab Ini

- Membuat database menggunakan Python.
- Memuat data dari file CSV menjadi tabel di database.
- Menjalankan query dasar (SELECT, COUNT) untuk mengakses data.

## Skenario

Data karyawan (instruktur) dalam file CSV dimuat ke database `STAFF`, tabel `INSTRUCTOR`, lalu dijalankan beberapa query untuk melihat isi tabel.

## Struktur Folder

1.4 - Accessing Databases using Python/
├── db_code.py         # Script utama
├── INSTRUCTOR.csv      # Data sumber
└── STAFF.db            # Database hasil (SQLite)

## Alur Program

1. **Koneksi database** — buat/koneksi ke `STAFF.db` pakai `sqlite3`.
2. **Baca CSV** — baca `INSTRUCTOR.csv` pakai `pandas`, kasih nama kolom manual karena csv-nya tanpa header.
3. **Load ke tabel** — simpan dataframe jadi tabel `INSTRUCTOR` di database (`if_exists='replace'`, supaya tidak dobel tiap dijalankan ulang).
4. **Query data** — jalankan 3 query: lihat semua data, lihat kolom FNAME saja, hitung jumlah baris.
5. **Tambah data (append)** — masukkan 1 baris data baru (John Doe), lalu hitung ulang jumlah baris untuk memastikan bertambah.
6. **Tutup koneksi** — `conn.close()` di akhir program.

## Cara Menjalankan

pip install pandas
python db_code.py

Hasil query akan tampil di terminal, dan file `STAFF.db` akan terbentuk di folder ini.

## Catatan Pribadi

Path file CSV di kode ini dibuat relatif (`INSTRUCTOR.csv`), bukan `/home/project/...` seperti di instruksi asli — karena path itu khusus environment IDE cloud IBM, sedangkan di lokal cukup nama file saja asal berada di folder yang sama dengan `db_code.py`.
