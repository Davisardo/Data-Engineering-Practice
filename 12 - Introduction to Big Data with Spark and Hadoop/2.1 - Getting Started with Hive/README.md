# 2.1 - Getting Started with Hive

## Tujuan
Belajar dasar Apache Hive: menjalankan HiveServer2 lewat Docker, membuat database & tabel, memuat data dari file CSV, dan menjalankan query HiveQL sederhana.

## Environment
- **OS**: Windows 11 + WSL (Ubuntu)
- **Container**: Docker Desktop, image `apache/hive:4.0.0-alpha-1`
- **Client**: Beeline (CLI bawaan Hive, dijalankan lewat `docker exec`)
- **Data source**: `emp.csv` (data karyawan: emp_id, emp_name, salary), didownload dari IBM Skills Network

## Materi & Command yang Dipakai

| Tahap | Command / Query | Keterangan |
|---|---|---|
| Download data | `wget <url>/emp.csv` | Ambil file CSV mentah |
| Pull image Hive | `docker pull apache/hive:4.0.0-alpha-1` | Ambil image Hive dari Docker Hub |
| Jalankan container | `docker run -d -p 10000:10000 -p 10002:10002 --env SERVICE_NAME=hiveserver2 --name hive4 apache/hive:4.0.0-alpha-1` | Start HiveServer2 di background, expose port client (10000) & Web UI (10002) |
| Masuk Beeline | `docker exec -it hive4 beeline -u jdbc:hive2://localhost:10000` | Buka CLI client Hive di dalam container |
| Buat database | `CREATE DATABASE IF NOT EXISTS emp_db;` | Bikin database baru, idempotent |
| Pilih database | `USE emp_db;` | Pindah context kerja ke database `emp_db` |
| Buat tabel | `CREATE TABLE IF NOT EXISTS employee (emp_id INT, emp_name STRING, salary INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE TBLPROPERTIES ("skip.header.line.count"="1");` | Skema tabel sesuai CSV, skip baris header saat load |
| Copy file ke container | `docker cp "<path emp.csv>" hive4:/opt/hive/emp.csv` | Pindahkan file dari host ke filesystem container |
| Load data | `LOAD DATA LOCAL INPATH '/opt/hive/emp.csv' INTO TABLE employee;` | `LOCAL` = ambil file dari filesystem container (tempat HiveServer2 jalan), bukan dari HDFS |
| Verifikasi | `SELECT * FROM employee LIMIT 10;` | Cek data berhasil masuk dengan benar |

## Relevansi ke Data Engineering
- **Schema-on-read**: Hive tidak memvalidasi skema saat data di-load, beda dari RDBMS yang schema-on-write — konsep dasar yang sama dipakai di data lake modern.
- **Container-based tooling**: menjalankan Hive lewat Docker mencerminkan praktik industri, di mana software kompleks (Hive/Spark/Kafka) umumnya dijalankan via container/orchestrator, bukan install manual.
- **HiveQL mirip SQL**: mempercepat transisi dari skill RDBMS/SQL yang sudah dikuasai ke ekosistem big data.
- **Host vs container filesystem**: kebutuhan `docker cp` sebelum `LOAD DATA LOCAL INPATH` menegaskan pentingnya paham batas filesystem antara host dan container saat bekerja dengan data terdistribusi.

## Catatan Pribadi
- Sempat kena error `docker: command not found` di WSL — ternyata WSL Integration untuk distro Ubuntu belum diaktifkan di Docker Desktop (Settings → Resources → WSL Integration). Setelah diaktifkan, `docker` langsung bisa dipanggil dari WSL.
- Sempat juga kena `permission denied ... docker.sock` — awalnya dikira masalah izin user ke docker group, ternyata cuma karena Docker Desktop belum dibuka. Buka aplikasinya dulu, baru jalan normal.
- `docker cp` sempat gagal karena path yang dipakai adalah path style WSL (`/mnt/d/...`) padahal command-nya dijalankan dari CMD Windows — harus pakai path style Windows (`D:\...`) supaya CMD bisa baca.
- Pelajaran utama: container itu punya filesystem sendiri, terpisah dari host. Makanya perlu `docker cp` dulu sebelum `LOAD DATA LOCAL INPATH` bisa baca file itu dari dalam container.
- Lab ini jadi first-hand experience gimana rasanya Hive jalan di atas container — dari sisi DE, ini nunjukkin kalau troubleshooting environment (WSL, Docker, path OS) itu sama pentingnya dengan paham HiveQL-nya sendiri.