# Lab: MySQL Configuration, Storage Engines, and System Tables

## Tujuan
Memahami dan mempraktikkan storage engine alternatif di MySQL (selain InnoDB default),
serta belajar menavigasi tabel sistem (`mysql`, `information_schema`) untuk mengambil
metadata objek database.

## Environment
- MySQL 8.0.43 (MySQL Community Server) — terinstall native di **Windows**, dijalankan
  sebagai Windows Service (`MySQL80`)
- Dijalankan via **CMD** (bukan WSL), karena tidak ada kebutuhan Linux-specific di lab ini
- Dataset: `world_mysql_script.sql` (database sample MySQL, berisi tabel `city`,
  `country`, `countrylanguage`)

## Materi yang Dipelajari

| Command / Konsep | Kegunaan |
|---|---|
| `CREATE DATABASE world;` | Membuat database baru |
| `USE world;` | Berpindah/memilih database aktif |
| `SOURCE world_mysql_script.sql;` | Menjalankan script SQL untuk populate data |
| `SHOW TABLES;` | Melihat daftar tabel dalam database aktif |
| `SHOW ENGINES;` | Melihat storage engine yang didukung server & mana yang default |
| `CREATE TABLE ... ENGINE = CSV;` | Membuat tabel dengan storage engine non-default (CSV) |
| `CREATE TABLE ... ENGINE = MYISAM;` | Membuat tabel dengan storage engine MyISAM |
| `SHOW DATABASES;` | Melihat semua database di server |
| `SELECT User FROM user;` | Query tabel sistem `mysql.user` untuk lihat daftar user |
| `CREATE USER test_user;` | Membuat user baru (otomatis tercatat di tabel sistem) |
| `SELECT COLUMN_NAME FROM COLUMNS WHERE TABLE_NAME = '...' AND TABLE_SCHEMA = '...';` | Query metadata kolom tabel via `INFORMATION_SCHEMA` |
| `SELECT table_name, engine FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = '...';` | Query metadata engine tiap tabel |

## Relevansi ke Data Engineering
- **Storage engine** menentukan trade-off performa vs fitur (transaksi, indexing) —
  penting saat merancang tabel staging/temporary (MEMORY/CSV) vs tabel transaksional (InnoDB).
- **INFORMATION_SCHEMA** adalah cara standar untuk melakukan *data profiling* otomatis
  (misalnya, script yang mengecek skema tabel sebelum pipeline ETL jalan) — konsep yang
  sama dipakai di banyak tools katalog data modern (Data Catalog, dbt, Airflow sensors).
- Filter `TABLE_SCHEMA` wajib di lingkungan multi-database — kesalahan umum yang bisa
  bikin pipeline salah ambil metadata dari database yang salah.
- Tabel sistem **tidak boleh diedit manual** — prinsip ini juga berlaku di data warehouse
  modern (jangan pernah modifikasi catalog/metadata table secara langsung).

## Catatan Pribadi
- Environment lokal: MySQL native Windows (bukan WSL), karena lab ini tidak butuh
  perintah Linux-specific.
- Sempat ada typo `'wrold'` alih-alih `'world'` di query — reminder untuk selalu
  double check nama schema saat filter `WHERE table_schema = '...'`.
  