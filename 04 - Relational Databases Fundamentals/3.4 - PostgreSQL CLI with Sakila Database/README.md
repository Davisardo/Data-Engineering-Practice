# Getting Started with the PostgreSQL Command Line

**Course:** 04 - Relational Databases Fundamentals (Introduction to Relational Databases (RDBMS) — IBM/Coursera)
**Module:** 3 — Lab 3.4

## Tujuan Lab Ini

- Membuat database menggunakan PostgreSQL command line
- Merestore struktur dan data tabel dari file dump
- Mengeksplorasi dan melakukan query terhadap tabel
- Melakukan dump/backup tabel dari database

## Struktur Folder

```
3.4 - PostgreSQL CLI with Sakila Database/
├── sakila_pgsql_dump.sql            # dump file awal (struktur + data seluruh database Sakila)
├── sakila_store_pgsql_dump.sql      # hasil backup tabel store saja
└── README.md
```

*(Catatan: database `sakila` tersimpan di dalam PostgreSQL Server lokal, bukan file di folder ini)*

## Materi yang Dipelajari

- Instalasi PostgreSQL Server di Windows + menambahkan `psql` ke PATH secara manual (Environment Variables)
- Membuat database baru lewat PostgreSQL CLI: `create database sakila;`
- Berpindah koneksi ke database lain dalam satu sesi menggunakan `\connect nama_db;` (setara `USE` di MySQL, tapi lebih terisolasi antar database)
- Merestore dump file menggunakan `\include file.sql;`
- Membaca list tabel dengan `\dt`, dan struktur tabel lengkap (kolom, PK, FK, index, trigger) dengan `\d nama_tabel;` — jauh lebih detail dibanding `DESCRIBE` di MySQL
- Melakukan backup/export tabel individual menggunakan `pg_dump`, setara `mysqldump` di MySQL
- Konsep **`search_path`**: variabel session yang menentukan schema mana yang dicari saat menulis nama tabel tanpa awalan schema — kalau kosong, tabel yang sebenarnya ada pun tidak akan ditemukan oleh query biasa

## Cara Menjalankan

1. Pastikan PostgreSQL Server sudah terinstall dan `psql` bisa dipanggil dari CMD (`psql --version`)
2. Download dump file:
```cmd
   curl -o sakila_pgsql_dump.sql https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/sakila/sakila_pgsql_dump.sql
```
3. Masuk ke PostgreSQL CLI:
```cmd
   psql --username=postgres --host=localhost
```
4. Di dalam prompt, jalankan:
```sql
   create database sakila;
   \connect sakila;
   \include sakila_pgsql_dump.sql;
```
5. **Kalau `\dt` menampilkan "Did not find any tables"** meskipun proses restore sukses, cek dan set search_path:
```sql
   SET search_path TO public;
```
6. Backup tabel store (dari CMD biasa, setelah keluar dari prompt dengan `\q`):
```cmd
   pg_dump --username=postgres --host=localhost --password --dbname=sakila --table=store --format=plain > sakila_store_pgsql_dump.sql
```

## Cheat Sheet: PostgreSQL CLI untuk Data Engineering

| Perintah | Fungsi | Setara di MySQL |
|---|---|---|
| `create database db_name;` | Bikin database baru | `create database db_name;` |
| `\connect db_name;` (atau `\c`) | Pindah koneksi ke database lain | `USE db_name;` |
| `\include file.sql;` | Restore dump file dari dalam prompt | `source file.sql;` |
| `\dt` | List semua tabel | `SHOW FULL TABLES;` |
| `\d nama_tabel;` | Lihat struktur tabel lengkap (kolom, PK, FK, index, trigger) | `DESCRIBE nama_tabel;` |
| `pg_dump ... --table=x > file.sql` | Export/backup tabel jadi file .sql | `mysqldump ... db table > file.sql` |
| `SET search_path TO public;` | Set schema default pencarian tabel | *(tidak ada konsep setara langsung — MySQL tidak punya schema search path)* |

**Koneksi ke project sebelumnya:**

Lab ini paralel dengan lab 3.1 (MySQL CLI) — dataset & alur kerjanya identik (Sakila database, create → restore → explore → backup), tapi mempraktikkan versi PostgreSQL. Perbandingan langsung ini membantu memahami bahwa **konsep relational database itu universal**, sementara detail sintaks CLI (`\dt` vs `SHOW TABLES`, `\connect` vs `USE`) itu spesifik per vendor — skill yang portable antar database adalah pemahaman konsepnya, bukan hafalan syntax satu tool saja.

**Perangkap umum:**
- Instruksi lab asli pakai `--host=postgres` (hostname khusus container IBM Cloud IDE) — di lokal harus diganti `--host=localhost`
- Installer PostgreSQL di Windows tidak selalu otomatis menambahkan `psql` ke PATH — kalau CMD tidak mengenali `psql`, cek folder `C:\Program Files\PostgreSQL\<versi>\bin` dan tambahkan manual lewat Environment Variables
- Kalau tabel "hilang" padahal restore terlihat sukses (`\dt` kosong tapi query lain bilang tabel "already exists"), cek `SHOW search_path;` — kemungkinan kosong dan perlu di-set manual ke `public`
- Menjalankan `\include` dua kali pada database yang sama akan memunculkan banyak error "already exists" / "duplicate key" — ini **aman**, bukan tanda kerusakan data, karena PostgreSQL menolak insert ulang data yang constraint-nya sudah terpenuhi

## Catatan Pribadi

Insight paling berkesan: kasus `search_path` kosong itu jadi pelajaran debugging yang bagus — errornya (`relation does not exist`) kelihatan seperti "data hilang", padahal sebenarnya datanya utuh, cuma **konfigurasi pencarian schema**-nya yang bermasalah. Ini mengingatkan pentingnya cek asumsi paling dasar dulu (di schema mana sebenarnya data itu berada) sebelum menyimpulkan ada masalah besar seperti restore gagal atau data korup.