# 3.1 - Load CSV into Datasette

**Lab: Load data into the Datasette from a CSV file**
Course 01 - Datasette Basics (IBM Data Engineering Professional Certificate)

## Tujuan Lab Ini

- Membuat dan memuat data ke dalam tabel dari file CSV menggunakan Datasette.

## Tentang Datasette

Datasette adalah tool open-source untuk menjelajahi dan meng-query data (CSV/SQLite) lewat antarmuka web, tanpa perlu menulis kode. Cocok untuk eksplorasi cepat data atau berbagi dataset ke orang lain tanpa mereka perlu setup database sendiri.

## Struktur Folder

3.1 - Load CSV into Datasette/
├── exercise03_car_sales_data.csv   # Data mentah (29 baris data mobil bekas)
└── car_sales.db                     # Hasil konversi ke SQLite, dibaca oleh Datasette

## Alur yang Dilakukan

1. Install `datasette` dan `csvs-to-sqlite`.
2. Download dataset CSV (data mobil bekas: price, mileage, engType, year, model).
3. Konversi CSV ke database SQLite menggunakan `csvs-to-sqlite`.
4. Jalankan server Datasette lokal, buka lewat browser.
5. Jelajahi tabel data lewat web interface.
6. Jalankan query SQL custom: `SELECT COUNT(*) FROM exercise03_car_sales_data;` → hasil 29.

## Cara Menjalankan

pip install datasette csvs-to-sqlite
csvs-to-sqlite exercise03_car_sales_data.csv car_sales.db
datasette car_sales.db

Buka browser ke `http://127.0.0.1:8001`, klik tabel untuk melihat data, atau klik "View and edit SQL" untuk menjalankan query custom.

## Catatan Pribadi

Instruksi asli lab ini dirancang untuk platform Datasette versi lama milik IBM yang bisa langsung membaca CSV lewat menu "Add Datasets" di web. Versi Datasette terbaru tidak lagi mendukung baca CSV langsung — perlu dikonversi dulu ke SQLite menggunakan tool `csvs-to-sqlite` sebelum bisa dibuka. Ini kesempatan bagus untuk memahami bahwa Datasette pada dasarnya adalah viewer untuk database SQLite, bukan pembaca CSV native.