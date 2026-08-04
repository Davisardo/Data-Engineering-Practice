# 2.3 - Verifying Data Quality for a Data Warehouse

## Tujuan Lab
Membangun dan menjalankan framework pengecekan kualitas data berbasis Python untuk data warehouse `billingDW`, mencakup pengecekan null, duplikat, valid values, dan rentang min-max pada tabel dimension dan fact.

## Environment
- PostgreSQL 15 (Docker container `course9-postgres`, port 5433)
- Python 3.13 + `psycopg2-binary`, `pandas`, `tabulate` (dikelola via `uv`)
- Database: `billingDW`

## Materi yang Dipelajari
- 4 dimensi kualitas data: akurasi, kelengkapan, konsistensi, kekinian
- Framework testing Python yang memisahkan **logic pengecekan** (`dataqualitychecks.py`) dari **konfigurasi test** (`mytests.py`) — pola desain yang extensible tanpa mengubah kode inti
- 4 jenis test: `check_for_nulls`, `check_for_min_max`, `check_for_valid_values`, `check_for_duplicates`
- Crash recovery PostgreSQL (WAL) — container sempat exit tidak wajar, Postgres otomatis pulih tanpa kehilangan data

## Command & Code Penting

| Tahap | Command |
|---|---|
| Download file framework | `curl -o <nama_file>.py "<url>"` (4 file: dataqualitychecks.py, dbconnect.py, mytests.py, generate-data-quality-report.py) |
| Install dependency | `uv pip install psycopg2-binary --system` dan `uv pip install pandas tabulate --system` |
| Edit koneksi (dbconnect.py & generate-data-quality-report.py) | `host="localhost"`, `port="5433"`, `password="postgres"`, `database="billingDW"` |
| Test koneksi | `python dbconnect.py` |
| Jalankan laporan kualitas data | `python generate-data-quality-report.py` |

**Contoh test di `mytests.py`:**
```python
test9 = {
    "testname": "Check for valid values",
    "test": check_for_valid_values,
    "column": "quarter",
    "table": "DimMonth",
    "valid_values": {1, 2, 3, 4},
}
```

**Hasil akhir: 9 test, semua Passed = True**, mencakup pengecekan null (`monthid`, `year`), min-max (`month`, `quarter`), valid values (`category`, `quartername`, `quarter`), dan duplikat (`monthid`, `customerid`).

## Relevansi terhadap Data Engineering
Data quality check adalah lapisan wajib sebelum data dianggap siap dipakai untuk analisis bisnis — data warehouse tanpa verifikasi kualitas berisiko menghasilkan laporan yang salah tanpa disadari. Pola pemisahan logic vs konfigurasi test ini juga dasar dari tools data quality modern di industri (Great Expectations, dbt tests).

## Catatan Pribadi
- Sempat mengalami container Docker `Exited (255)` di tengah sesi (kemungkinan Docker Desktop restart) — belajar cara diagnosis pakai `docker ps -a` dan `docker logs`, serta memahami mekanisme crash recovery PostgreSQL (WAL) yang otomatis memulihkan database tanpa kehilangan data.
- Paham perbedaan `valid_values` bertipe string (`{'Q1','Q2','Q3','Q4'}`) vs integer (`{1,2,3,4}`) — harus cocok dengan tipe data kolom aslinya di database.
- Practice exercise soal 1-2 di-skip karena sama persis dengan test yang sudah dicoba di Exercise 5 & 8 (beda kolom saja); hanya soal 3 (valid_values dengan tipe integer) yang dikerjakan karena kasusnya berbeda.