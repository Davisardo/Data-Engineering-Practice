# Create Tables and Load Data in MySQL using phpMyAdmin

**Course:** 04 - Relational Databases Fundamentals (Introduction to Relational Databases (RDBMS) — IBM/Coursera)
**Module:** 3 — Lab 3.2

## Tujuan Lab Ini

- Membuat database menggunakan MySQL
- Membuat tabel di dalam database
- Memuat data ke dalam tabel secara manual lewat GUI
- Memuat data ke dalam tabel menggunakan file script SQL

## Struktur Folder

```
3.2 - Create Tables and Load Data in MySQL using phpMyAdmin/
├── mysql_table-myauthors_insert-data.sql   # script SQL berisi data tambahan (1376 baris)
└── README.md
```

*(Catatan: database `Books` tersimpan di dalam MySQL Server lokal, bukan file di folder ini)*

## Materi yang Dipelajari

- Membuat database & tabel lewat GUI client (MySQL Workbench) sebagai pengganti phpMyAdmin
- Mendesain skema tabel sederhana dengan `AUTO_INCREMENT` + `PRIMARY KEY` sebagai best practice standar
- Insert data manual lewat SQL Editor (setara fitur "Insert" GUI di phpMyAdmin)
- Import/load data massal dari file `.sql` menggunakan **File → Open SQL Script → Execute** (setara fitur "Import" di phpMyAdmin)
- Verifikasi integritas data pakai `COUNT(*)`, `COUNT(DISTINCT kolom)`, dan `MAX(kolom)` — cara cepat memastikan tidak ada duplikat/data hilang setelah proses import besar

## Cara Menjalankan

1. Buka MySQL Workbench, connect ke MySQL lokal (`127.0.0.1:3306`, user `root`)
2. Jalankan di SQL Editor:
```sql
   CREATE DATABASE Books;
   USE Books;

   CREATE TABLE myauthors (
       author_id INT NOT NULL AUTO_INCREMENT,
       first_name VARCHAR(100),
       middle_name VARCHAR(50),
       last_name VARCHAR(100),
       PRIMARY KEY (author_id)
   );

   INSERT INTO myauthors (first_name, middle_name, last_name) VALUES
   ('Martin', NULL, 'Fowler'),
   ('Robert', 'Cecil', 'Martin');
```
3. Download script data tambahan:
```cmd
   curl -o mysql_table-myauthors_insert-data.sql https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/Books/mysql_table-myauthors_insert-data.sql
```
4. Di MySQL Workbench: **File → Open SQL Script...** → pilih file di atas → klik **Execute** (⚡)
5. Verifikasi:
```sql
   SELECT COUNT(*) FROM myauthors;
```

## Cheat Sheet: MySQL GUI Client untuk Data Engineering

| phpMyAdmin (versi cloud IBM) | MySQL Workbench (versi lokal) | Fungsi |
|---|---|---|
| Tombol "New" di tree database | `CREATE DATABASE` di SQL Editor | Bikin database baru |
| Tab "Insert" | `INSERT INTO ... VALUES` di SQL Editor | Insert data manual |
| Tab "Import" + Choose File | **File → Open SQL Script** + Execute | Load data massal dari file `.sql` |
| Tab "Browse" | `SELECT * FROM tabel` | Lihat isi tabel |

**Koneksi ke project ETL sebelumnya:**

Proses **load data massal dari file eksternal** ini adalah pola umum tahap **Load** di pipeline ETL — baik lewat GUI (seperti di lab ini) maupun terprogram (`sqlite-utils`, `mysqldump`/`source` di lab-lab sebelumnya, atau `pandas.to_sql()` untuk pipeline Python). Prinsipnya sama: pastikan skema tujuan sudah benar sebelum load, lalu verifikasi jumlah baris & keunikan data setelahnya — jangan asumsikan proses import selalu sukses tanpa dicek.

**Perangkap umum:**
- **Jangan klik Execute berkali-kali** pada script `INSERT` yang sama tanpa `ON DUPLICATE KEY` atau pengecekan — bisa menyebabkan data ter-insert ulang. Di lab ini sempat terlihat gejala serupa (jumlah baris tidak sesuai ekspektasi awal), tapi setelah dicek dengan `COUNT(DISTINCT author_id)` ternyata semua data unik — file sumbernya memang berisi ribuan baris, bukan karena eksekusi ganda
- Selalu verifikasi hasil import dengan `COUNT(*)` + `COUNT(DISTINCT primary_key)` — kalau kedua angka itu sama, data dipastikan bebas duplikat
- phpMyAdmin adalah aplikasi web (butuh Apache+PHP), tidak built-in di instalasi MySQL Server standar — MySQL Workbench jadi alternatif desktop native yang lebih ringan untuk dipakai jangka panjang

## Catatan Pribadi

Insight paling berkesan: waktu jumlah baris hasil import (1378) nggak sama persis dengan ekspektasi awal (16), reaksi pertama adalah curiga ada duplikat. Tapi setelah dicek pakai `COUNT(DISTINCT)`, ternyata itu cuma salah asumsi soal ukuran file sumbernya (dikira cuma 14 baris data padahal ribuan). Ini pelajaran penting: **jangan langsung asumsikan ada bug** kalau angka tidak sesuai ekspektasi — verifikasi dulu dengan query yang tepat sebelum menyimpulkan sesuatu salah.