# Final Assignment: Data Engineering for a Consulting Firm

Proyek ini adalah Final Assignment dari course **Introduction to NoSQL Databases** (IBM Data Engineering Professional Certificate). Skenarionya: berperan sebagai Data Engineer di sebuah firma konsultasi data, yang bertugas memindahkan dan mentransformasi data film antar dua platform database NoSQL — **MongoDB** dan **Cassandra**.

**Hasil akhir: 95/100 (passing grade 70%)**

## Tujuan

- Import data semi-terstruktur (JSON) ke MongoDB
- Melakukan query & agregasi data di MongoDB
- Export data (subset field) dari MongoDB ke CSV
- Mendesain skema tabel dan import data ke Cassandra
- Melakukan query CQL di Cassandra, termasuk membuat secondary index

## Environment

Assignment ini awalnya didesain untuk dikerjakan di **Skills Network Cloud IDE** (Theia + Docker terkelola otomatis), tapi dikerjakan ulang secara **lokal** menggunakan:

- **OS:** Windows 11 + WSL2 (Ubuntu)
- **Docker Desktop** (WSL2 backend) untuk menjalankan MongoDB & Cassandra sebagai container
- **VS Code** (terhubung ke WSL) sebagai editor & terminal utama

### Menjalankan environment dari nol

```bash
# MongoDB
docker run -d --name mongodb-nosql -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=root \
  -e MONGO_INITDB_ROOT_PASSWORD=password123 \
  mongo:latest

# Cassandra (heap dibatasi supaya tidak OOMKilled di WSL2)
docker run -d --name cassandra-nosql -p 9042:9042 \
  -e CASSANDRA_CLUSTER_NAME=nosql-cluster \
  -e MAX_HEAP_SIZE=512M -e HEAP_NEWSIZE=100M \
  cassandra:latest
```

> **Catatan resource:** Cassandra butuh heap JVM yang cukup besar secara default, dan bisa langsung ter-`OOMKilled` (exit code 137) kalau limit memori WSL2 terlalu kecil. Solusinya: set `.wslconfig` di Windows (`%UserProfile%\.wslconfig`) dengan alokasi memori minimal ~6GB, dan batasi heap Cassandra lewat `MAX_HEAP_SIZE`/`HEAP_NEWSIZE`.

## Struktur Project

```
11 - Introduction to NoSQL Databases/
└── 4.1 - Final Assignment - Data Engineering for a Consulting Firm/
    ├── movies.json          # data mentah (didownload dari IBM Skills Network)
    ├── partial_data.csv     # hasil export dari MongoDB, jadi input untuk Cassandra
    └── README.md
```

## Materi yang Dipelajari

- Perbedaan mendasar antara MongoDB (document store) dan Cassandra (wide-column store), termasuk trade-off desainnya
- MongoDB aggregation pipeline (`$group`, `$sort`, `$limit`, `$match`, `$avg`)
- Import/export data MongoDB (`mongoimport`, `mongoexport`) dan format JSON Lines vs JSON Array
- Desain skema tabel Cassandra dan aturan penamaan kolom di CQL (identifier tidak boleh diawali underscore tanpa quoting)
- Import data ke Cassandra lewat `COPY` command
- Secondary index di Cassandra: kapan cocok dipakai (kolom cardinality rendah) dan trade-off performanya
- Menjalankan database sebagai container Docker untuk kebutuhan development lokal, termasuk tuning resource (heap JVM, memori WSL2)

## Command Penting

**MongoDB — import & query:**
```bash
docker exec mongodb-nosql mongoimport --username root --password password123 \
  --authenticationDatabase admin --db entertainment --collection movies --file /movies.json

docker exec mongodb-nosql mongosh --username root --password password123 \
  --authenticationDatabase admin entertainment --eval \
  "db.movies.aggregate([{ \$group: { _id: '\$year', moviecount: { \$sum: 1 } } }, { \$sort: { moviecount: -1 } }, { \$limit: 1 }])"
```

**MongoDB — export ke CSV:**
```bash
docker exec mongodb-nosql mongoexport --username root --password password123 \
  --authenticationDatabase admin --db entertainment --collection movies \
  --type=csv --fields=_id,title,year,rating,Director --out /partial_data.csv
```

**Cassandra — keyspace, tabel, import, index:**
```bash
docker exec -it cassandra-nosql cqlsh -e \
  "CREATE KEYSPACE entertainment WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};"

docker exec -it cassandra-nosql cqlsh -e \
  "CREATE TABLE entertainment.movies (\"_id\" text PRIMARY KEY, title text, year text, rating text, director text);"

docker exec -it cassandra-nosql cqlsh -e \
  "COPY entertainment.movies (\"_id\", title, year, rating, director) FROM '/partial_data.csv' WITH HEADER=TRUE;"

docker exec -it cassandra-nosql cqlsh -e \
  "CREATE INDEX IF NOT EXISTS rating_idx ON entertainment.movies (rating);"
```

## Code Penting

Query MongoDB paling signifikan — cari tahun dengan jumlah film terbanyak (aggregation pipeline):

```javascript
db.movies.aggregate([
  { $group: { _id: "$year", moviecount: { $sum: 1 } } },
  { $sort: { moviecount: -1 } },
  { $limit: 1 }
])
// Result: [ { _id: 2016, moviecount: 73 } ]
```

Query CQL — hitung film ber-rating "G" setelah index dibuat di kolom `rating`:

```sql
SELECT COUNT(*) FROM entertainment.movies WHERE rating = 'G';
-- Result: 32
```

## Relevansi terhadap Data Engineering

Project ini mensimulasikan skenario umum di dunia kerja: **migrasi & transformasi data lintas platform database**. Alurnya (MongoDB → CSV → Cassandra) merepresentasikan pola ETL sederhana — extract dari satu sistem sumber, transform (seleksi kolom relevan), lalu load ke sistem tujuan yang punya struktur & tipe data berbeda. Tantangan teknis seperti *impedance mismatch* (aturan penamaan kolom `_id` di MongoDB vs CQL identifier rules di Cassandra) adalah hal nyata yang sering dihadapi saat integrasi sistem heterogen.

## Catatan Pribadi

- Awalnya assignment ini didesain untuk Skills Network Cloud IDE, tapi dikerjakan ulang secara lokal pakai Docker — proses debugging environment (resource WSL2, OOMKilled Cassandra) jadi pembelajaran tambahan di luar materi course itu sendiri.
- Submission pertama sempat gagal (55%) karena bukti screenshot tidak menampilkan command yang dijalankan, hanya output-nya saja — pelajaran penting soal dokumentasi bukti kerja yang tidak cuma "benar secara hasil" tapi juga "bisa diverifikasi prosesnya".
- Skor akhir: **95/100**.