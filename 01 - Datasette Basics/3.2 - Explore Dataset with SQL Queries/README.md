# 3.2 - Explore Dataset with SQL Queries

**Lab: Explore your dataset using SQL queries using Datasette**
Course 01 - Datasette Basics (IBM Data Engineering Professional Certificate)

## Tujuan Lab Ini

- Menjalankan query SQL dasar pada data yang sudah dimuat ke database, lewat Datasette.

## Struktur Folder

3.2 - Explore Dataset with SQL Queries/
└── car_sales.db     # Disalin dari 3.1, database berisi data mobil bekas

## Query yang Dijalankan

**1. Cek harga maksimum**

select max(price) as max_price from exercise03_car_sales_data

Hasil: `26500`

**2. Lihat model mobil yang unik (distinct)**

select distinct(model) from exercise03_car_sales_data;

Hasil: 5 model — Discovery, Freelander, Range Rover, Range Rover Sport, Range Rover Evoque

## Cara Menjalankan

datasette car_sales.db

Buka browser ke `http://127.0.0.1:8001`, masuk ke bagian "View and edit SQL", jalankan query di atas.

## Catatan Pribadi

Lab ini melanjutkan dataset dari 3.1, fokus pada dua pola query yang sering dipakai saat eksplorasi data awal: fungsi agregat (`MAX`, bisa juga `MIN`/`AVG`/`COUNT`) untuk melihat ringkasan angka, dan `DISTINCT` untuk melihat variasi nilai unik di suatu kolom kategorikal — keduanya jadi langkah awal umum sebelum analisis lebih dalam.