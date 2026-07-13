# Normalization, Keys, and Constraints in Relational Database

**Course:** 04 - Relational Databases Fundamentals (Introduction to Relational Databases (RDBMS) — IBM/Coursera)
**Module:** 2 — Lab 2.2

## Tujuan Lab Ini

- Meminimalkan redundansi dan inkonsistensi data dalam database menggunakan normalisasi
- Menggunakan key untuk mengidentifikasi record secara unik, membangun relasi antar tabel, dan mengidentifikasi jenis relasinya
- Menjaga integritas data dalam model data relasional menggunakan constraint

## Struktur Folder

```
2.2 - Normalization, Keys, and Constraints/
├── setup_bookshop.py               # script Python: seluruh proses normalisasi, PK, FK, dan test constraint
├── BookShop-CREATE-INSERT.sql      # script SQL awal (tabel BookShop sebelum dinormalisasi)
├── bookshop_normalization.db       # database SQLite hasil akhir (2 tabel: BookShop, BookShop_AuthorDetails)
└── README.md
```

## Materi yang Dipelajari

- **First Normal Form (1NF)**: setiap kolom harus berisi nilai atomic (tunggal), dan setiap baris harus unik
- **Second Normal Form (2NF)**: tidak boleh ada partial dependency — data yang berulang (author info) dipisah ke tabel tersendiri (`BookShop_AuthorDetails`) menggunakan `SELECT DISTINCT`
- **Primary Key**: constraint yang menjamin setiap baris unik dan tidak null; diuji langsung dengan mencoba insert `BOOK_ID` duplikat → menghasilkan `IntegrityError: UNIQUE constraint failed`
- **Foreign Key**: constraint yang menghubungkan `AUTHOR_ID` di tabel `BookShop` ke `AUTHOR_ID` di tabel `BookShop_AuthorDetails`; diuji dengan mencoba insert `AUTHOR_ID` yang tidak ada → menghasilkan `IntegrityError: FOREIGN KEY constraint failed`
- **PRAGMA foreign_keys**: SQLite tidak menegakkan FK secara default, harus diaktifkan manual dengan `PRAGMA foreign_keys = ON`
- **Constraint integrity** (konseptual): Entity Integrity, Referential Integrity, dan Domain Integrity — semuanya terbukti lewat implementasi PK, FK, dan `CHECK(Price_USD>0)` di skema

## Cara Menjalankan

1. Pastikan `sqlite3` (modul bawaan Python) tersedia — tidak perlu install tambahan
2. Jalankan script:
```cmd
   python setup_bookshop.py
```
3. (Opsional) Buka hasilnya lewat Datasette:
```cmd
   datasette bookshop_normalization.db
```
   Lalu akses `http://127.0.0.1:8001` di browser untuk browse tabel `BookShop` dan `BookShop_AuthorDetails`.

## Cheat Sheet: Normalization, Keys & Constraints untuk Data Engineering

| Konsep | Fungsi | Contoh di lab ini |
|---|---|---|
| 1NF | Setiap cell atomic, setiap baris unik | Skema awal BookShop sudah 1NF |
| 2NF | Hilangkan partial dependency lewat tabel terpisah | `BookShop_AuthorDetails` dipisah dari `BookShop` |
| PRIMARY KEY | Unik + NOT NULL per baris | `BOOK_ID`, `AUTHOR_ID` |
| FOREIGN KEY | Cross-reference ke PK tabel lain | `BookShop.AUTHOR_ID` → `BookShop_AuthorDetails.AUTHOR_ID` |
| CHECK constraint | Validasi nilai kolom | `CHECK(Price_USD>0)` |

**Koneksi ke project ETL sebelumnya:**

```python
# Pola defensive insert seperti ini penting di tahap "Load" pipeline ETL
try:
    conn.execute("INSERT INTO table_name VALUES (...)")
    conn.commit()
except sqlite3.IntegrityError as e:
    # log error, skip row, atau kirim ke dead-letter queue
    print("Row ditolak karena constraint violation:", e)
```
Di real-world pipeline (misal load ke Postgres), constraint violation seperti ini adalah sinyal penting — bukan cuma error yang harus dihindari, tapi mekanisme **data quality gate** otomatis. Kalau kamu desain skema dengan PK/FK/CHECK yang tepat sejak awal, banyak masalah data kotor bisa tertangkap otomatis di level database, bukan cuma di level aplikasi.

**Perangkap umum:**
- Lupa `PRAGMA foreign_keys = ON` di SQLite → FK constraint tidak akan pernah tertegakkan meskipun sudah didefinisikan di skema, dan insert data "yatim" (orphan record) akan lolos begitu saja
- Normalisasi berlebihan (over-normalization) bisa bikin query jadi lambat karena banyak JOIN — perlu balance antara normalisasi dan performa query, tergantung kebutuhan (OLTP vs OLAP)
- `DROP TABLE IF EXISTS` yang dipanggil berulang tanpa backup bisa menghapus data penting kalau tidak hati-hati — selalu pastikan urutan drop child table dulu sebelum parent table kalau ada FK constraint aktif

## Catatan Pribadi

Insight paling berkesan: melihat langsung `IntegrityError` muncul di terminal saat sengaja insert data yang melanggar PK dan FK itu jauh lebih nempel dibanding cuma baca teori "primary key mencegah duplikat". Constraint bukan cuma dokumentasi skema di atas kertas — itu benar-benar aktif menjaga data di level engine database, bahkan kalau ada bug di kode aplikasi yang mencoba insert data salah.