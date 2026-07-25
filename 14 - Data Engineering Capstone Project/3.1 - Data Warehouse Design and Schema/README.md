# 3.1 - Data Warehouse Design and Schema

## Tujuan
Merancang skema data warehouse (Star Schema) untuk platform e-commerce SoftCart menggunakan pgAdmin ERD Tool, kemudian membuat schema tersebut di database PostgreSQL bernama `staging`. Modul ini adalah bagian dari Modul 3 - Data Engineering Capstone Project (IBM Data Engineering Professional Certificate).

Data warehouse ini akan menjadi target ETL (Modul 5) dari sumber data OLTP (Modul 1 - MySQL) dan NoSQL (Modul 2 - MongoDB), serta sumber data untuk dashboard BI (Modul 4).

## Environment
- **OS:** Windows 11
- **Database:** PostgreSQL 18
- **Tools:** pgAdmin 4 (ERD Design Tool, Query Tool)

## Struktur Project
```
3.1 - Data Warehouse Design and Schema/
├── screenshots/
│   ├── task1-softcartDimDate-erd.png
│   ├── task2-4-dimension-tables-erd.png
│   ├── task5-softcartFactSales-erd.png
│   ├── task6-full-erd-relationships.png
│   └── task7-schema-creation-success.png
├── softcart_schema.sql
└── README.md
```

## Materi yang Dipelajari
- Konsep **Star Schema**: 1 tabel fact (measure/angka transaksi) dikelilingi beberapa tabel dimension (atribut deskriptif) — desain yang sengaja didenormalisasi demi kecepatan query analitik, berbeda total dari skema ternormalisasi di OLTP (Modul 1)
- Desain ERD visual menggunakan pgAdmin ERD Tool: penambahan tabel, kolom, tipe data, dan primary key
- Pemilihan tipe data string yang tepat (`varchar(n)` untuk field kategorikal pendek, dibanding `char(n)` yang memaksa padding, atau `text` yang tanpa batas)
- Pembuatan relasi one-to-many antar tabel di ERD tool, termasuk pemahaman **arah foreign key** yang benar (Local Table = tabel "many"/anak, Referenced Table = tabel "one"/induk)
- Generate SQL DDL otomatis dari desain ERD visual
- Eksekusi script SQL bertransaksi (`BEGIN ... COMMIT`) dan penanganan error transaksi macet menggunakan `ROLLBACK`

## Desain Skema

**Fact Table:**
- `softcartFactSales` — `salesid` (PK), `dateid`, `itemid`, `countryid`, `quantity`, `price numeric(10,2)`

**Dimension Tables:**
- `softcartDimDate` — `dateid` (PK), `date`, `year`, `quarter`, `month`, `monthname`, `week`, `weekday`
- `softcartDimCategory` — `categoryid` (PK), `categoryname`
- `softcartDimItem` — `itemid` (PK), `itemname`, `categoryid` (FK → DimCategory)
- `softcartDimCountry` — `countryid` (PK), `countryname`

**Relasi:**
- `softcartFactSales.dateid` → `softcartDimDate.dateid`
- `softcartFactSales.itemid` → `softcartDimItem.itemid`
- `softcartFactSales.countryid` → `softcartDimCountry.countryid`
- `softcartDimItem.categoryid` → `softcartDimCategory.categoryid`

`softcartFactSales` memiliki **3 koneksi langsung** ke tabel lain (Date, Item, Country). Koneksi ke `softcartDimCategory` bersifat tidak langsung, melalui `softcartDimItem`.

## Command Penting

**Generate schema (hasil ERD Tool) — dijalankan di database `staging`:**
```sql
BEGIN;

CREATE TABLE IF NOT EXISTS public."softcartDimDate" (
    dateid integer NOT NULL,
    date date,
    year integer,
    quarter integer,
    month integer,
    monthname character varying(20),
    week integer,
    weekday character varying(20),
    PRIMARY KEY (dateid)
);

-- ... (softcartDimCategory, softcartDimItem, softcartDimCountry, softcartFactSales)

ALTER TABLE IF EXISTS public."softcartFactSales"
    ADD FOREIGN KEY (dateid)
    REFERENCES public."softcartDimDate" (dateid) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

-- ... (foreign key lainnya)

END;
```

**Verifikasi tabel:**
```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;
```

## Relevansi terhadap Data Engineering
Modul ini melatih kemampuan inti data engineer dalam merancang data warehouse yang siap pakai untuk kebutuhan analitik bisnis (laporan penjualan per bulan, kategori, dan negara). Skema Star Schema yang dibangun di sini menjadi fondasi bagi Modul 3.2 (query aggregation: grouping sets, rollup, cube), Modul 4 (dashboard BI), dan Modul 5 (target ETL dari OLTP/NoSQL).

## Catatan Pribadi
- Kesalahan paling signifikan di modul ini adalah **arah foreign key terbalik** saat menggambar relasi di ERD Tool — pgAdmin menentukan arah berdasarkan urutan klik (klik pertama = "Local Table"/tabel anak, bukan tabel induk). Kesalahan ini menyebabkan error `no unique constraint matching given keys`.
- Setelah transaksi SQL gagal di tengah jalan, sesi PostgreSQL tertahan dalam status "aborted" dan butuh perintah `ROLLBACK;` eksplisit sebelum bisa menjalankan query baru.
- Selalu verifikasi field "Local Table" dan "Referenced Table" di dialog relasi ERD Tool sebelum menyimpan — jangan asumsikan urutan klik otomatis benar.