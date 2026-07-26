# 3.2 - Data Warehouse Reporting

## Tujuan
Memuat data penjualan e-commerce SoftCart ke dalam data warehouse PostgreSQL (database `Test1`), kemudian melakukan query analitik lanjutan (Grouping Sets, Rollup, Cube) dan membuat Materialized View untuk mendukung kebutuhan pelaporan bisnis. Modul ini melanjutkan skema yang dirancang di Modul 3.1, dengan skema final yang "diimprove" (nama kolom dan struktur sedikit berbeda dari desain ERD awal).

## Environment
- **OS:** Windows 11
- **Database:** PostgreSQL 18, database `Test1`
- **Tools:** pgAdmin 4 (Query Tool, Import/Export Data GUI)

## Struktur Project
```
3.2 - Data Warehouse Reporting/
├── DimDate.csv
├── DimCategory.csv
├── DimCountry.csv
├── FactSales.csv
└── README.md
```

## Materi yang Dipelajari
- Import data CSV ke PostgreSQL menggunakan fitur **Import/Export Data** pgAdmin (setara `COPY` command, dijalankan otomatis lewat `\copy` di sisi client — tidak perlu memindahkan file ke folder khusus server seperti kasus `secure_file_priv` di MySQL)
- **GROUPING SETS** — menghasilkan beberapa breakdown agregasi independen (per country, per category, dan grand total) dalam satu query, tanpa perlu `UNION` manual
- **ROLLUP** — agregasi hierarkis bertingkat (detail → subtotal per level → grand total), cocok untuk dimensi yang punya urutan alami seperti tahun
- **CUBE** — agregasi ke segala arah kombinasi (superset dari ROLLUP), menghasilkan subtotal dari setiap kombinasi dimensi yang mungkin
- **Materialized View (MQT)** — hasil query yang disimpan secara fisik untuk mempercepat akses berulang, dengan trade-off perlu `REFRESH` manual saat data sumber berubah
- Verifikasi konsistensi data lintas-query (grand total dari GROUPING SETS, ROLLUP, dan Materialized View saling cocok sebagai cross-check kebenaran hasil)

## Command Penting

**Load data (via pgAdmin Import/Export GUI, setara):**
```sql
\copy public.dimdate(dateid, date, year, quarter, quartername, month, monthname, day, weekday, weekdayname)
FROM 'DimDate.csv' WITH (FORMAT csv, DELIMITER ',', HEADER);
```

**Grouping Sets:**
```sql
SELECT c.country, cat.category, SUM(f.amount) AS totalsales
FROM factsales f
JOIN dimcountry c ON f.countryid = c.countryid
JOIN dimcategory cat ON f.categoryid = cat.categoryid
GROUP BY GROUPING SETS (
    (c.country),
    (cat.category),
    ()
)
ORDER BY c.country, cat.category;
```

**Rollup:**
```sql
SELECT d.year, c.country, SUM(f.amount) AS totalsales
FROM factsales f
JOIN dimdate d ON f.dateid = d.dateid
JOIN dimcountry c ON f.countryid = c.countryid
GROUP BY ROLLUP (d.year, c.country)
ORDER BY d.year, c.country;
```

**Cube:**
```sql
SELECT d.year, c.country, AVG(f.amount) AS averagesales
FROM factsales f
JOIN dimdate d ON f.dateid = d.dateid
JOIN dimcountry c ON f.countryid = c.countryid
GROUP BY CUBE (d.year, c.country)
ORDER BY d.year, c.country;
```

**Materialized View:**
```sql
CREATE MATERIALIZED VIEW total_sales_per_country AS
SELECT c.country, SUM(f.amount) AS total_sales
FROM factsales f
JOIN dimcountry c ON f.countryid = c.countryid
GROUP BY c.country;
```

## Relevansi terhadap Data Engineering
Modul ini melatih kemampuan menghasilkan laporan bisnis multi-level dari data warehouse — kebutuhan umum di dunia kerja seperti "total penjualan per negara, per kategori, dan keseluruhan" dalam satu laporan. Teknik GROUPING SETS/ROLLUP/CUBE menghindari kebutuhan menjalankan banyak query terpisah, sementara Materialized View menjadi teknik optimasi standar untuk laporan yang sering diakses namun tidak butuh data real-time — keduanya langsung relevan untuk Modul 4 (Dashboard BI) yang akan mengonsumsi hasil laporan ini.

## Catatan Pribadi
- Skema kolom di file CSV (`DimDate`, `DimCategory`, `DimCountry`, `FactSales`) ternyata berbeda dari desain ERD Modul 3.1 (nama tabel `softcart*` vs skema sederhana di sini) — konsisten dengan skenario lab yang menyebutkan "senior data engineer telah mengimprove desain", sehingga penting selalu memverifikasi struktur data asli (`type` header CSV) sebelum membuat `CREATE TABLE`, bukan berasumsi dari desain sebelumnya.
- Tanda kutip ganda yang terlihat di sekitar nilai string (misal `"Argentina"`) saat menampilkan hasil query di pgAdmin Data Output grid adalah **gaya tampilan visual**, bukan bagian dari data asli — dikonfirmasi dengan `LENGTH()` yang menunjukkan panjang string sudah benar tanpa karakter kutip tambahan.
- Grand total dari GROUPING SETS (Task 5) dan ROLLUP (Task 6) menghasilkan angka yang identik (`1,201,006,258.00`) — digunakan sebagai cross-check konsistensi data antar query.
