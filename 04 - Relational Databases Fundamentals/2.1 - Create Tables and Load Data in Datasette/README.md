# Create Tables and Load Data in Datasette

**Course:** 04 - Relational Databases Fundamentals (Introduction to Relational Databases (RDBMS) — IBM/Coursera)
**Module:** 2 — Lab 2.1

## Tujuan Lab Ini

- Membuat dan memuat data ke dalam tabel dari file CSV
- Membuat dan memuat data ke dalam tabel menggunakan file script SQL (CREATE + INSERT)

## Struktur Folder

```
2.1 - Create Tables and Load Data in Datasette/
├── load_data.py                    # script Python: download data + load ke SQLite
├── PETSHOP.csv                     # dataset CSV mentah
├── BookShop-CREATE-INSERT.sql      # script SQL mentah (DDL + DML)
├── petshop.db                      # database SQLite hasil akhir (2 tabel: PETSHOP, BookShop)
└── README.md
```

## Materi yang Dipelajari

- Perbedaan **schema-on-read** (CSV di-load langsung, skema di-infer otomatis) vs **schema-on-write** (skema didefinisikan manual lewat `CREATE TABLE`)
- Menggunakan `sqlite-utils` untuk convert CSV → tabel SQLite secara otomatis
- Menjalankan script SQL mentah (multi-statement) dari Python memakai modul `sqlite3` bawaan, lewat `executescript()`
- Menjalankan **Datasette** sebagai local web server untuk browse & query database SQLite lewat UI browser
- Query dasar SQL: `SELECT count(*)`, `SELECT *`

## Cara Menjalankan

1. Install dependency (sekali saja):
```cmd
   pip install datasette sqlite-utils --break-system-packages
```
2. Jalankan script untuk download data & load ke database:
```cmd
   python load_data.py
```
3. Buka Datasette UI untuk query:
```cmd
   datasette petshop.db
```
   Lalu akses `http://127.0.0.1:8001` di browser.

## Cheat Sheet: Datasette & SQLite untuk Data Engineering

| Tool | Fungsi | Kapan dipakai |
|---|---|---|
| `sqlite-utils insert` | Load CSV/JSON → tabel SQLite otomatis (infer schema) | Data eksploratif, prototyping cepat |
| `sqlite3` (modul Python) | Eksekusi SQL manual (DDL/DML) dari script | Butuh kontrol skema penuh (tipe data, constraint, PK) |
| `datasette` | Web UI + API read-only untuk browse/query SQLite | Sharing/eksplorasi data ke tim tanpa install DB client |

**Koneksi ke project ETL sebelumnya (Course 3):**

```python
# Pola yang sama seperti extract() di project ETL kamu,
# tapi load target-nya SQLite via sqlite-utils, bukan pandas.to_csv()
import subprocess
subprocess.run(["sqlite-utils", "insert", "db.db", "TABLE_NAME", "data.csv", "--csv"])
```

Ini bisa jadi alternatif ringan buat *staging area* lokal sebelum data masuk ke database "asli" (Postgres/MySQL) — cocok untuk testing pipeline ETL tanpa setup database server penuh.

**Perangkap umum:**
- Lupa flag `--csv` di `sqlite-utils insert` → format file salah ditebak, data korup
- `subprocess.run(["sqlite3", ...])` gagal di Windows kalau SQLite CLI belum ada di PATH → pakai modul `sqlite3` Python bawaan sebagai gantinya, lebih portable
- Server `datasette` blocking terminal — harus `Ctrl+C` dulu sebelum jalankan command Python lain di terminal yang sama

## Catatan Pribadi

Insight paling berkesan: instruksi lab resmi IBM asumsinya selalu environment cloud mereka (tombol "Add Dataset" di UI Datasette versi mereka nggak ada di install lokal) — jadi harus translate tiap step ke tool command-line yang setara (`sqlite-utils`, modul `sqlite3`). Latihan ini bagus buat biasa mikir "apa tujuan step ini secara konsep" bukan cuma ngikutin klik-klik UI.