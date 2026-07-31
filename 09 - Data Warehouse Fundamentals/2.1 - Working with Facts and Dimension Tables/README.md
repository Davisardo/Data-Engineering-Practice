# 2.1 - Working with Facts and Dimension Tables

## Tujuan Lab
Merancang data warehouse untuk perusahaan cloud service provider menggunakan data billing pelanggan. Fokus pada desain star schema (fact table + dimension table) untuk mendukung pelaporan seperti rata-rata billing per customer/industry/country, top 10 customer/country, dan tren billing per tahun/bulan/kuartal.

## Environment
- PostgreSQL 15 (Docker container `course9-postgres`, port 5433)
- pgAdmin 4 untuk koneksi & eksekusi query
- Database: `billingDW`

## Materi yang Dipelajari
- Konsep fact table vs dimension table
- Star schema design
- Constraint `PRIMARY KEY` dan `FOREIGN KEY` (referential integrity)
- Kolom `SERIAL` untuk auto-generate ID saat sumber data tidak menyediakan ID unik

## Command & Code Penting

| Tahap | Code |
|---|---|
| Bikin container Postgres | `docker run --name course9-postgres -e POSTGRES_PASSWORD=postgres -p 5433:5432 -d postgres:15` |
| Bikin tabel dimensi customer | `CREATE TABLE DimCustomer (customerid INT PRIMARY KEY, category VARCHAR(50), country VARCHAR(50), industry VARCHAR(50));` |
| Bikin tabel dimensi bulan | `CREATE TABLE DimMonth (monthid INT PRIMARY KEY, year INT, month INT, monthname VARCHAR(20), quarter INT, quartername VARCHAR(10));` |
| Bikin tabel fakta billing | `CREATE TABLE FactBilling (billid SERIAL PRIMARY KEY, customerid INT REFERENCES DimCustomer(customerid), monthid INT REFERENCES DimMonth(monthid), billedamount NUMERIC(10,2));` |

**Practice exercise (dataset retail fashion):**
```sql
CREATE TABLE DimStore (
    storeid INT PRIMARY KEY,
    country VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE DimDate (
    dateid INT PRIMARY KEY,
    day INT,
    weekday INT,
    weekdayname VARCHAR(20),
    year INT,
    month INT,
    monthname VARCHAR(20),
    quarter INT,
    quartername VARCHAR(10)
);

CREATE TABLE FactSales (
    rowid SERIAL PRIMARY KEY,
    storeid INT REFERENCES DimStore(storeid),
    dateid INT REFERENCES DimDate(dateid),
    totalsales INT
);
```

## Relevansi terhadap Data Engineering
Fact & dimension table adalah fondasi star schema — pola desain paling umum di data warehouse untuk mendukung query analitik cepat (OLAP). Memahami kapan pakai `SERIAL` vs ID manual, serta cara kerja `REFERENCES` untuk menjaga konsistensi data antar tabel, adalah skill dasar yang dipakai di hampir semua project data warehousing di dunia kerja.

## Catatan Pribadi
- Sempat bingung soal kenapa `FactBilling` pakai `SERIAL` sedangkan `DimCustomer`/`DimMonth` pakai `INT PRIMARY KEY` manual — intinya: `SERIAL` dipakai kalau sumber data (CSV) tidak menyediakan ID unik sendiri, jadi Postgres yang generate otomatis. Kalau sumber data sudah punya ID (seperti customerid dari CSV), tinggal pakai `INT PRIMARY KEY` biasa.
- Sempat lupa syntax `PRIMARY KEY` harus didahului tipe data (`INT PRIMARY KEY`, bukan cuma `PRIMARY KEY`) — kesalahan kecil tapi penting diingat.
- Belajar bahwa `CREATE TABLE` yang dijalankan dua kali akan error (table already exists), bukan bikin data double — beda dengan `INSERT` yang memang bisa duplikat kalau dijalankan berulang. `CREATE TABLE IF NOT EXISTS` bisa jadi solusi untuk pipeline yang perlu idempotent.
- Practice exercise (DimStore, DimDate, FactSales) dikerjakan mandiri dan langsung benar dari percobaan pertama (kecuali kesalahan syntax kecil) — tanda konsep fact/dimension table sudah cukup nempel.