# 1.3 - Web Scraping and Extracting Data

**Lab: Web Scraping dan Ekstraksi Data menggunakan API**
Course 3 - Python Project for Data Engineering (IBM Data Engineering Professional Certificate)

## Tujuan Lab Ini

- Menggunakan library `requests` dan `BeautifulSoup` untuk mengambil isi halaman web.
- Menganalisis struktur HTML untuk menemukan data yang dibutuhkan.
- Mengekstrak data dan menyimpannya dalam format CSV dan database.

## Skenario

Mengambil data 50 film dengan rating terbaik dari halaman web (`Average Rank`, `Film`, `Year`), lalu menyimpannya ke file CSV dan database SQLite.

## Struktur Folder

1.3 - Web Scraping and Extracting Data/
├── webscraping_movies.py    # Script utama
├── top_50_films.csv         # Hasil ekstraksi dalam CSV
└── Movies.db                # Hasil ekstraksi dalam database SQLite

## Alur Program

1. **Load halaman web** — ambil HTML halaman pakai `requests`, lalu parsing pakai `BeautifulSoup`.
2. **Cari tabel data** — temukan tabel pertama di halaman, ambil semua barisnya.
3. **Ekstrak data** — looping tiap baris, ambil kolom `Average Rank`, `Film`, `Year`, batasi hanya 50 data teratas.
4. **Simpan hasil** — ke file `top_50_films.csv` dan tabel `Top_50` di database `Movies.db`.

## Cara Menjalankan

pip install pandas bs4 requests
python webscraping_movies.py

Hasil ekstraksi akan tampil di terminal, dan file `top_50_films.csv` + `Movies.db` akan terbentuk di folder ini.

## Catatan Pribadi

Halaman sumber diakses lewat Wayback Machine (arsip web.archive.org) supaya struktur HTML-nya konsisten dan tidak berubah-ubah seperti versi live-nya.