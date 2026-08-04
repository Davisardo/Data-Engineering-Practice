# 2.4 - Populating a Data Warehouse using PostgreSQL

## Tujuan Lab
Membuat dan mengisi database `Production` menggunakan file schema yang di-generate oleh ERD tool pgAdmin, dilakukan sepenuhnya lewat pgAdmin GUI (Query Tool → Open File), sebagai variasi dari cara `docker exec` yang dipakai di lab sebelumnya. Dilanjutkan dengan praktik membuat, me-refresh, dan meng-query materialized view.

## Environment
- PostgreSQL 15 (Docker container `course9-postgres`, port 5433)
- pgAdmin 4 (Query Tool dengan fitur "Open File")
- Database: `Production`

## Materi yang Dipelajari
- Strategi pengisian data warehouse: initial load, incremental load, full refresh
- Fact table bersifat dinamis (sering update), dimension table relatif statis
- Nama tabel PascalCase (mis. `"FactBilling"`) butuh tanda kutip di query, karena Postgres default-nya mengubah huruf jadi kecil semua tanpa kutip
- `NOT VALID` pada `ALTER TABLE ... ADD FOREIGN KEY` — constraint berlaku untuk data baru tanpa validasi ulang data lama
- Membuat, me-refresh, dan meng-query `MATERIALIZED VIEW` secara langsung (bukan cuma teori)

## Command & Code Penting

| Tahap | Command/Query |
|---|---|
| Bikin schema | Query Tool → Open File → `star-schema.sql` (versi ERD tool, dari folder 2.1) → Run |
| Load data | Query Tool → Open File → `DimCustomer.sql`, `DimMonth.sql`, `FactBilling.sql` → Run (urutan dimension dulu, fact terakhir) |
| Verifikasi | `select count(*) from public."DimMonth";` |
| Bikin materialized view | `CREATE MATERIALIZED VIEW avg_customer_bill (customerid, averagebillamount) AS (select customerid, avg(billedamount) from public."FactBilling" group by customerid);` |
| Refresh materialized view | `REFRESH MATERIALIZED VIEW avg_customer_bill;` |
| Query materialized view | `select * from avg_customer_bill where averagebillamount > 11000;` |

**Hasil load data:** `DimCustomer` (1000), `DimMonth` (132), `FactBilling` (132000) — konsisten dengan `billingDW` dan `practice`.

**Hasil query materialized view:** 23 customer dengan rata-rata billing di atas $11.000, tertinggi customer #884 dengan rata-rata $11.989,84.

## Relevansi terhadap Data Engineering
Cara mengisi data warehouse lewat GUI (Open File di Query Tool) adalah alternatif dari command line yang berguna saat bekerja dengan tim non-teknis atau environment tanpa akses terminal. Materialized view yang dipraktikkan langsung di sini menunjukkan manfaat nyata: query kompleks (agregasi rata-rata dari 132.000 baris) cukup dihitung sekali, lalu di-query berkali-kali dengan cepat tanpa membebani database berulang kali.

## Catatan Pribadi
- File `star-schema.sql` di lab ini ternyata versi berbeda dari yang dipakai di lab 2.1/2.2 — di-generate oleh ERD tool pgAdmin, memakai nama tabel PascalCase dengan tanda kutip (`"FactBilling"`) dan constraint `NOT VALID`. Baru paham bahwa nama tabel tanpa kutip otomatis di-lowercase oleh Postgres.
- Sempat mengalami "Connection Warning" (koneksi database terputus) saat menjalankan `CREATE MATERIALIZED VIEW` — solusinya klik "Continue" di pgAdmin untuk membuka sesi baru, tanpa kehilangan query yang sudah ditulis.
- Practice exercise soal 1 di-skip karena sama persis dengan verifikasi count yang sudah dilakukan sebelumnya; soal 2-4 (materialized view) dikerjakan penuh karena materi baru yang sebelumnya cuma dipelajari secara teori.