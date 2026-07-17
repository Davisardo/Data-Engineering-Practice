# Create Tables and Load Data in PostgreSQL using pgAdmin

**Course:** 04 - Relational Databases Fundamentals (Introduction to Relational Databases (RDBMS) — IBM/Coursera)
**Module:** 3 — Lab 3.5

## Tujuan Lab Ini

- Membuat database dan tabel di instance PostgreSQL menggunakan pgAdmin
- Memuat data ke dalam tabel secara manual lewat GUI pgAdmin
- Memuat data ke dalam tabel dari file CSV

## Struktur Folder

```
3.5 - PostgreSQL with pgAdmin/
├── myauthors.csv      # data tambahan untuk tabel myauthors
└── README.md
```

*(Catatan: database `Books` tersimpan di dalam PostgreSQL Server lokal, bukan file di folder ini)*

## Materi yang Dipelajari

- Menghubungkan pgAdmin ke PostgreSQL Server lokal (host `localhost`, port `5432`)
- Membuat database dan tabel sepenuhnya lewat form GUI (tanpa menulis SQL manual) — cocok untuk yang belum familiar sintaks DDL
- Tipe data **`serial`** di PostgreSQL sebagai pengganti `AUTO_INCREMENT` MySQL — otomatis membuat sequence generator terpisah untuk kolom tersebut
- Insert data manual lewat **View/Edit Data → All Rows**, termasuk konsep "staged changes" yang perlu di-*commit* eksplisit lewat Save (`F6`) sebelum benar-benar tersimpan ke database
- Import data massal dari file CSV lewat **Import/Export Data**, dengan opsi **Header** untuk memberi tahu PostgreSQL bahwa baris pertama file adalah nama kolom, bukan data

## Cara Menjalankan

1. Buka pgAdmin 4, connect ke server PostgreSQL lokal
2. Buat database:
   - Klik kanan **Databases** → **Create** → **Database...** → nama `Books` → Save
3. Buat tabel `myauthors` (klik kanan **Tables** → **Create** → **Table...**):

   | Name | Data type | Length | Not Null | Primary Key |
   |---|---|---|---|---|
   | `author_id` | `serial` | - | ✓ | ✓ |
   | `first_name` | `character varying` | 100 | | |
   | `middle_name` | `character varying` | 50 | | |
   | `last_name` | `character varying` | 100 | | |

4. Download data tambahan:
```cmd
   curl -o myauthors.csv https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/Books/myauthors.csv
```
5. Insert 2 baris manual lewat **View/Edit Data → All Rows**, lalu Save (`F6`)
6. Import CSV lewat klik kanan tabel → **Import/Export Data...** → pilih file, Format `csv`, aktifkan **Header** di tab Options → OK

## Cheat Sheet: pgAdmin untuk Data Engineering

| pgAdmin (GUI) | Setara SQL langsung | Fungsi |
|---|---|---|
| Create → Database... | `CREATE DATABASE nama;` | Bikin database baru |
| Create → Table... (tab Columns) | `CREATE TABLE ... (kolom tipe, ...)` | Bikin tabel + skema kolom |
| View/Edit Data → All Rows | `INSERT INTO ... VALUES (...)` | Insert data manual |
| Import/Export Data... | `\copy tabel FROM 'file.csv' CSV HEADER;` | Load data massal dari file |
| Tipe data `serial` | `INTEGER ... DEFAULT nextval('seq')` | Auto-increment PK |

**Koneksi ke project sebelumnya:**

Lab ini versi PostgreSQL dari lab 3.2 (MySQL + phpMyAdmin/Workbench) — database, tabel, dan skema kolomnya sengaja dibuat identik supaya bisa dibandingkan langsung. Perbedaan paling mencolok: PostgreSQL tidak punya `AUTO_INCREMENT`, melainkan tipe data khusus `serial` yang otomatis menghubungkan kolom ke sebuah *sequence* — konsep yang lebih eksplisit dan "terpisah" dibanding pendekatan MySQL.

**Perangkap umum:**
- Toggle **"Primary key?"** di form Create Table pgAdmin **tidak otomatis** mengaktifkan toggle **"Not NULL?"** — meski secara aturan database PK selalu NOT NULL, di form GUI ini harus diaktifkan manual, jangan asumsikan UI selalu mengikuti aturan database di baliknya
- Data yang diinput lewat grid **View/Edit Data** berstatus "staged" dulu (belum permanen) sampai tombol **Save Data Changes** (`F6`) ditekan — kalau lupa, perubahan akan hilang saat pindah tab/menutup grid
- Saat import CSV, **jangan lupa aktifkan opsi Header** di tab Options — kalau tidak, baris pertama (nama kolom) akan ikut ter-insert sebagai baris data biasa, menyebabkan error tipe data atau data kotor
- Sesi pgAdmin bisa "reset" ke halaman awal setelah idle lama — tapi data yang sudah tersimpan di database tetap aman, cuma perlu connect ulang ke server dan navigasi ulang ke objeknya

## Catatan Pribadi

Insight paling berkesan: perbandingan langsung antara MySQL Workbench (lab 3.2) dan pgAdmin untuk task yang identik (bikin database, tabel, import CSV) menunjukkan bahwa meskipun GUI-nya beda total tampilannya, **alur kerja konseptualnya sama**: buat skema dulu, definisikan constraint, baru masukkan data. Yang membedakan cuma detail teknis kecil seperti `AUTO_INCREMENT` vs `serial`, atau cara toggle constraint di form — bukan pola besarnya. Ini menguatkan bahwa skill inti yang perlu dikuasai adalah pemahaman relational database, bukan hafalan satu tool spesifik.
