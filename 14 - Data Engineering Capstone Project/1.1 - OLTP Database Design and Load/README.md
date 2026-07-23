# 1.1 - OLTP Database Design and Load

## Tujuan
Merancang dan mengimplementasikan database OLTP (Online Transaction Processing) menggunakan MySQL untuk menyimpan data transaksi penjualan e-commerce (SoftCart), sebagai bagian dari Modul 1 - Data Engineering Capstone Project (IBM Data Engineering Professional Certificate).

Deliverable modul ini menjadi dasar bagi pipeline ETL dan data warehouse yang akan dibangun di modul-modul berikutnya.

## Environment
- **OS:** Windows 11
- **Database:** MySQL 8.0.43 (Community Server), berjalan sebagai Windows Service (`MySQL80`)
- **Terminal:** CMD (untuk operasi MySQL & Windows), WSL Ubuntu (untuk bash scripting & mysqldump)
- **Tools:** MySQL Command Line Client, mysqldump (WSL, versi 8.4.10)

### Catatan Setup Cross-Environment (WSL ↔ Windows MySQL)
Karena bash script (`datadump.sh`) dijalankan dari WSL sementara MySQL server berjalan di Windows, diperlukan konfigurasi tambahan:
1. `bind-address=0.0.0.0` ditambahkan ke `my.ini` agar MySQL menerima koneksi dari luar `127.0.0.1`
2. Firewall rule baru ditambahkan untuk mengizinkan koneksi masuk ke port 3306 dari semua profile network
3. User `'root'@'172.19.%'` dibuat khusus untuk mengizinkan login dari IP range WSL (bukan `'root'@'%'`, demi membatasi akses hanya dari jaringan lokal WSL)

## Struktur Project
```
1.1 - OLTP Database Design and Load/
├── oltpdata.csv          # Data mentah hasil download (2605 baris transaksi)
├── datadump.sh            # Script bash untuk export data ke file SQL
├── sales_data.sql          # Hasil export (struktur + data) dari mysqldump
└── README.md
```

## Materi yang Dipelajari
- Konsep dan karakteristik database OLTP (normalisasi tinggi, latency rendah, write-heavy)
- Desain skema tabel transaksi (`sales_data`) dengan tipe data yang tepat, termasuk penggunaan `DECIMAL` untuk nilai uang (bukan `FLOAT`, demi menghindari rounding error)
- Bulk import data menggunakan `LOAD DATA INFILE` dan pemetaan kolom eksplisit
- Pembuatan index (`CREATE INDEX`) dan trade-off-nya (mempercepat SELECT, memperlambat INSERT/UPDATE)
- Administrasi database via `mysqldump` untuk backup/export data
- Troubleshooting koneksi jaringan lintas-environment (WSL2 ↔ Windows): `bind-address`, Windows Firewall, dan MySQL user privileges berbasis host

## Command Penting

**Membuat database & tabel:**
```sql
CREATE DATABASE sales;
USE sales;

CREATE TABLE sales_data (
    row_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Import data CSV:**
```sql
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/oltpdata.csv'
INTO TABLE sales_data
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(product_id, customer_id, price, quantity, timestamp);
```

**Index & verifikasi:**
```sql
CREATE INDEX ts ON sales_data (timestamp);
SHOW INDEX FROM sales_data;
```

**Export data (dari WSL):**
```bash
mysqldump -h <IP_WSL_HOST> -u root -p sales sales_data > sales_data.sql
```
> Password dimasukkan lewat prompt interaktif (`-p` tanpa nilai langsung setelahnya), bukan hardcoded di command.

## Code Penting
```bash
#!/bin/bash
# datadump.sh - export semua data dari tabel sales_data ke file SQL
# Kredensial TIDAK di-hardcode; gunakan environment variable atau ~/.my.cnf
mysqldump -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASS" sales sales_data > sales_data.sql
```
> Nilai `DB_HOST`, `DB_USER`, `DB_PASS` disetel sebagai environment variable lokal sebelum menjalankan script, atau disimpan di file `~/.my.cnf` yang di-`.gitignore`-kan — bukan ditulis langsung di dalam script.

## Relevansi terhadap Data Engineering
Modul ini melatih fondasi paling dasar dari data engineering: bagaimana data transaksional operasional (OLTP) dirancang, diisi, dan dijaga performanya sebelum nantinya diekstrak ke dalam data warehouse (dibahas di Modul 3 & 5). Skema `sales_data` yang dibuat di sini akan menjadi sumber data bagi proses ETL inkremental di Modul 5, terutama untuk fungsi seperti `get_last_rowid()` dan `get_latest_records()` yang bergantung pada struktur dan index tabel ini.

## Catatan Pribadi
- Kredensial database yang dipakai selama lab ini hanya untuk keperluan lokal dan **tidak dicantumkan di repo** demi keamanan.
- Sebelum push ke GitHub, dipastikan `datadump.sh` tidak memuat password secara hardcoded di dalam kode.
- Kendala terbesar di modul ini bukan soal SQL, melainkan konfigurasi jaringan WSL2 ↔ Windows (bind-address, firewall, host-based privilege) — pengalaman debugging ini sangat relevan untuk skenario kerja nyata dengan environment hybrid/container.