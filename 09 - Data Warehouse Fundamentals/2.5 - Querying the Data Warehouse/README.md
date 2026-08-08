# 2.5 - Querying the Data Warehouse

## Tujuan Lab
Mempraktikkan query analitik lanjutan pada data warehouse `Production` menggunakan `GROUPING SETS`, `ROLLUP`, `CUBE`, dan materialized view untuk mendukung pelaporan multi-dimensi (per tahun, kuartal, kategori, negara).

## Environment
- PostgreSQL 15 (Docker container `course9-postgres`, port 5433)
- pgAdmin 4 (Query Tool)
- Database: `Production`

## Materi yang Dipelajari
- Perbedaan hasil `GROUPING SETS` vs `ROLLUP` vs `CUBE` pada data yang sama
- `GROUPING SETS` menghasilkan ringkasan sesuai kombinasi yang diminta persis
- `ROLLUP` menghasilkan hierarki linear (detail → subtotal bertingkat → grand total)
- `CUBE` menghasilkan semua kombinasi yang mungkin (2^n kombinasi untuk n kolom) — jauh lebih banyak baris dibanding ROLLUP pada kolom yang sama
- Materialized view dengan multiple grouping columns untuk pelaporan granular
- Container Docker tetap aman setelah dipindahkan ke drive lain via Docker Desktop Settings (Move disk image location) — data tidak hilang, cukup `docker start` ulang

## Command & Code Penting

| Tahap | Query |
|---|---|
| GROUPING SETS | `group by grouping sets(year, category)` → 13 baris (2 ringkasan terpisah) |
| ROLLUP | `group by rollup(year, category)` → 33 baris (hierarki + grand total) |
| CUBE (2 kolom) | `group by cube(year, category)` → 35 baris (semua kombinasi) |
| CUBE (3 kolom) | `group by cube(year, country, category)` → ribuan baris (2³ = 8 level kombinasi) |
| Materialized view 2 dimensi | `CREATE MATERIALIZED VIEW countrystats (country, year, totalbilledamount) AS (... group by country, year)` → 1419 baris |
| Materialized view 4 dimensi | `CREATE MATERIALIZED VIEW average_billamount (year, quarter, category, country, avgbilledamount) AS (... group by year, quarter, category, country)` → 8844 baris |

**Grand total konsisten di semua query:** $1.320.220.745 (baik dari ROLLUP, CUBE 2 kolom, maupun CUBE 3 kolom) — cross-check yang membuktikan hasil agregasi benar meski cara query berbeda.

## Relevansi terhadap Data Engineering
`GROUPING SETS`, `ROLLUP`, dan `CUBE` adalah fitur SQL inti untuk laporan BI multi-level tanpa perlu menulis banyak query terpisah dan `UNION`. Pemilihan di antara ketiganya adalah trade-off antara kelengkapan insight dan biaya komputasi — penting dipahami saat merancang query untuk dashboard produksi, terutama pada tabel besar dengan kolom berkardinalitas tinggi seperti `country`.

## Catatan Pribadi
- Sempat khawatir kehilangan data setelah memindahkan lokasi disk image Docker Desktop ke drive D — ternyata aman karena menggunakan fitur resmi "Move disk image location", container cuma perlu di-`docker start` ulang setelah proses migrasi.
- Baru paham secara nyata (bukan cuma teori) kenapa `CUBE` dengan kolom berkardinalitas tinggi (seperti `country`, ratusan nilai unik) bisa menghasilkan ribuan baris dan berat secara komputasi.
- Practice exercise soal 1-2 di-skip karena pola query-nya sama persis dengan Exercise 2 & 3 (beda kolom saja); soal 3 (CUBE 3 kolom) dan soal 4 (materialized view 4 dimensi) dikerjakan penuh karena kompleksitasnya beda dari yang sudah dicoba sebelumnya.