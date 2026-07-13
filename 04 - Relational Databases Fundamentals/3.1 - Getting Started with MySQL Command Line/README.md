# Getting Started with MySQL Command Line

**Course:** 04 - Relational Databases Fundamentals (Introduction to Relational Databases (RDBMS) — IBM/Coursera)
**Module:** 3 — Lab 3.1

## Tujuan Lab Ini

- Membuat database menggunakan MySQL command line
- Merestore struktur dan data tabel dari file dump SQL
- Mengeksplorasi dan melakukan query terhadap tabel
- Melakukan dump/backup tabel dari database

## Struktur Folder

```
3.1 - Getting Started with MySQL Command Line/
├── sakila_mysql_dump.sql            # dump file awal (struktur + data seluruh database Sakila)
├── sakila_staff_mysql_dump.sql      # hasil backup tabel staff saja
└── README.md
```

*(Catatan: database `sakila` sendiri tersimpan di dalam MySQL Server lokal, bukan file di folder ini — beda dengan lab-lab sebelumnya yang pakai SQLite berbasis file)*

## Materi yang Dipelajari

- Membuat database baru lewat MySQL CLI: `create database sakila;`
- Merestore dump file (ratusan statement SQL sekaligus) menggunakan `source file.sql;` di dalam prompt MySQL
- Membedakan `BASE TABLE` (tabel data asli) dari `VIEW`/`SYSTEM VIEW` menggunakan `SHOW FULL TABLES WHERE table_type = 'BASE TABLE';`
- Membaca struktur tabel (kolom, tipe data, key, constraint) menggunakan `DESCRIBE nama_tabel;`
- Melakukan backup/export tabel individual menggunakan `mysqldump`, menghasilkan file `.sql` yang berisi `CREATE TABLE` + `INSERT` — pola standar untuk database backup & migration
- Memahami dataset Sakila: database contoh standar industri (rental video), terdiri dari 15 tabel relasional (actor, film, customer, rental, staff, dll) dengan banyak relasi Foreign Key antar tabel

## Cara Menjalankan

1. Pastikan MySQL Server sudah terinstall dan berjalan (`mysql --version` untuk cek)
2. Download dump file:
```cmd
   curl -o sakila_mysql_dump.sql https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/sakila/sakila_mysql_dump.sql
```
3. Masuk ke MySQL CLI:
```cmd
   mysql --host=localhost --port=3306 --user=root --password
```
4. Di dalam prompt `mysql>`, jalankan:
```sql
   create database sakila;
   use sakila;
   source sakila_mysql_dump.sql;
```
5. Backup tabel staff (dari CMD biasa, setelah keluar dari prompt MySQL dengan `\q`):
```cmd
   mysqldump --host=localhost --port=3306 --user=root --password sakila staff > sakila_staff_mysql_dump.sql
```

## Cheat Sheet: MySQL Command Line untuk Data Engineering

| Command | Fungsi | Kapan dipakai |
|---|---|---|
| `create database db_name;` | Bikin database baru | Setup awal environment/project baru |
| `source file.sql;` | Restore dump file di dalam prompt MySQL | Migrasi/restore database dari backup |
| `mysql ... db_name < file.sql` | Restore dump file dari CLI (di luar prompt) | Automation/scripting restore tanpa masuk prompt interaktif |
| `SHOW FULL TABLES WHERE table_type='BASE TABLE';` | List tabel asli (bukan view) | Eksplorasi awal database yang belum dikenal |
| `DESCRIBE table_name;` | Lihat struktur kolom + key | Cek skema sebelum menulis query/ETL |
| `mysqldump ... db_name table_name > file.sql` | Export/backup tabel jadi file .sql | Backup rutin, migrasi antar environment (dev→staging→prod) |

**Koneksi ke project ETL sebelumnya:**

Pola `mysqldump` di lab ini sama konsepnya dengan proses **Extract** di pipeline ETL yang sudah dikerjakan di Course 3 — bedanya di sini extract-nya berupa SQL dump utuh (struktur + data), bukan hasil `SELECT` yang diolah lewat Python/Pandas. Kombinasi keduanya sering dipakai bareng di real-world: `mysqldump` untuk snapshot/backup penuh, sedangkan script Python (`pandas`/`sqlalchemy`) untuk transformasi data yang lebih granular sebelum di-load ke sistem lain.

**Perangkap umum:**
- Instruksi lab asli pakai `--host=mysql` (hostname khusus container IBM Cloud IDE) — di lokal harus diganti `--host=localhost`
- `wget` tidak tersedia di Windows CMD secara default — gunakan `curl -o` sebagai gantinya
- Lupa titik koma (`;`) di akhir statement SQL bikin MySQL CLI menunggu input lanjutan (prompt berubah jadi `->`), bukan error — tinggal tambahkan `;` dan Enter
- Password MySQL di instruksi lab (dari environment cloud IBM) tidak sama dengan password root MySQL lokal — gunakan password yang di-set sendiri saat instalasi

## Catatan Pribadi

Insight paling berkesan: lab ini kontras banget sama lab-lab SQLite sebelumnya — MySQL adalah **client-server database** (perlu service/daemon yang jalan terus di background, otentikasi user/password, host/port), sedangkan SQLite adalah **embedded database** (cuma file, langsung diakses lewat library tanpa server terpisah). Ini perbedaan arsitektur fundamental yang penting dipahami saat milih database untuk suatu project — SQLite cocok untuk aplikasi kecil/lokal/testing, MySQL (atau Postgres) untuk aplikasi produksi dengan banyak concurrent user.