# Keys and Constraints in MySQL using phpMyAdmin

**Course:** 04 - Relational Databases Fundamentals (Introduction to Relational Databases (RDBMS) — IBM/Coursera)
**Module:** 3 — Lab 3.3

## Tujuan Lab Ini

- Menambahkan key untuk membangun relasi antar tabel di database MySQL
- Menggunakan constraint untuk menegakkan aturan pada data entry

## Struktur Folder

```
3.3 - Keys and Constraints in MySQL/
├── eBooks_mysql_dump.sql      # dump file database eBooks (struktur + data)
└── README.md
```

*(Catatan: database `ebooks` tersimpan di dalam MySQL Server lokal, bukan file di folder ini)*

## Materi yang Dipelajari

- Import dump database yang berisi banyak tabel saling berelasi menggunakan `SET FOREIGN_KEY_CHECKS=0` untuk menghindari error urutan restore
- Memverifikasi struktur tabel sebelum melakukan perubahan, menggunakan `DESCRIBE tabel;` dan `SHOW CREATE TABLE tabel;` — penting karena skema riil kadang sudah sebagian "lebih lengkap" dari asumsi awal instruksi lab
- Menambahkan Primary Key + Auto-increment lewat `ALTER TABLE ... MODIFY ... ADD PRIMARY KEY` (ternyata di lab ini kolom `author_id` sudah PK dari file dump, jadi langkah ini di-skip setelah verifikasi)
- Menambahkan NOT NULL constraint pada kolom yang sudah ada data menggunakan `ALTER TABLE ... MODIFY kolom tipe NOT NULL`
- Menambahkan Foreign Key ke tabel yang sudah berisi data & constraint lain menggunakan `ALTER TABLE ... ADD CONSTRAINT ... FOREIGN KEY ... REFERENCES ...`
- Memahami **Composite Primary Key** (Primary Key yang terdiri dari lebih dari satu kolom) pada tabel junction/penghubung seperti `book_authors` (`PRIMARY KEY (book_id, author_id)`)
- Memahami `ON DELETE CASCADE`: bila baris di tabel induk (`authors`/`books`) dihapus, baris terkait di tabel penghubung (`book_authors`) otomatis ikut terhapus

## Cara Menjalankan

1. Buka MySQL Workbench, connect ke MySQL lokal (`127.0.0.1:3306`, user `root`)
2. Download dump file:
```cmd
   curl -o eBooks_mysql_dump.sql https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/eBooks/eBooks_mysql_dump.sql
```
3. Buat database & import:
```sql
   CREATE DATABASE eBooks;
```
   Lalu **File → Open SQL Script...** → pilih `eBooks_mysql_dump.sql` → Execute (⚡)
4. Cek struktur tabel sebelum ubah apapun:
```sql
   DESCRIBE authors;
   SHOW CREATE TABLE book_authors;
```
5. Tambahkan NOT NULL constraint:
```sql
   ALTER TABLE authors
   MODIFY first_name VARCHAR(100) NOT NULL;
```
6. Tambahkan Foreign Key:
```sql
   ALTER TABLE book_authors
   ADD CONSTRAINT fk_author
   FOREIGN KEY (author_id)
   REFERENCES authors(author_id)
   ON DELETE CASCADE;
```

## Cheat Sheet: Keys & Constraints untuk Data Engineering

| Perintah | Fungsi |
|---|---|
| `ALTER TABLE t MODIFY kolom TIPE NOT NULL` | Ubah kolom yang sudah ada jadi wajib diisi |
| `ALTER TABLE t MODIFY kolom TIPE AUTO_INCREMENT, ADD PRIMARY KEY (kolom)` | Set kolom sebagai PK sekaligus auto-generate nilai |
| `ALTER TABLE t ADD CONSTRAINT nama FOREIGN KEY (kolom) REFERENCES t2(kolom2)` | Tambahkan relasi FK ke tabel yang sudah eksis |
| `SHOW CREATE TABLE t;` | Lihat definisi lengkap tabel (kolom, PK, FK, engine, charset) — lebih detail dari `DESCRIBE` |
| `SET FOREIGN_KEY_CHECKS=0;` | Matikan sementara validasi FK saat restore/import data massal |

**Koneksi ke project sebelumnya:**

Lab ini kelanjutan langsung dari konsep Primary Key & Foreign Key di lab 2.2 (SQLite), tapi di sini dipraktikkan pada **tabel yang sudah berisi data** (bukan tabel kosong) — skenario yang jauh lebih realistis di dunia kerja. Menambah constraint ke tabel produksi yang sudah punya data itu lebih berisiko: kalau ada data yang melanggar aturan baru (misal ada baris `first_name` kosong sebelum constraint ditambahkan), `ALTER TABLE` akan gagal. Makanya verifikasi struktur & data sebelum ubah skema itu wajib, bukan opsional.

**Perangkap umum:**
- Jangan asumsikan skema masih "polos" seperti di gambar instruksi lab — selalu `DESCRIBE`/`SHOW CREATE TABLE` dulu sebelum eksekusi `ALTER TABLE`, supaya tidak kena error seperti "Multiple primary key defined" yang terjadi saat lab ini (ternyata PK sudah ada dari dump file)
- `ALTER TABLE ... ADD PRIMARY KEY` akan gagal kalau tabel sudah punya PK — harus `DROP PRIMARY KEY` dulu kalau memang mau ganti definisinya
- Composite Primary Key (PK gabungan 2+ kolom) itu wajar di tabel junction/many-to-many, jangan bingung membedakannya dengan tabel yang PK-nya cuma 1 kolom

## Catatan Pribadi

Insight paling berkesan: pas coba jalankan `ADD PRIMARY KEY` dan malah kena error "Multiple primary key defined" — awalnya bingung, tapi ternyata itu sinyal penting: **jangan asumsikan kondisi awal skema sama persis dengan yang digambarkan di instruksi lab**. Selalu cek kondisi sebenarnya dulu (`DESCRIBE`, `SHOW CREATE TABLE`) sebelum eksekusi perubahan — pola ini juga relevan banget di kerjaan nyata data engineer, di mana skema database production sering sudah "hidup" dan berubah dari waktu ke waktu, beda dari dokumentasi yang mungkin sudah usang.