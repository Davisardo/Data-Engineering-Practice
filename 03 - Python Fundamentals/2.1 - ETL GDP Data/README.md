# 2.1 - ETL GDP Data

**Practice Project: Extract, Transform and Load GDP Data**
Course 3 - Python Project for Data Engineering (IBM Data Engineering Professional Certificate)

## Skenario

Sebagai Data Engineer, membuat script otomatis untuk mengekstrak daftar GDP semua negara (dalam miliar USD) dari data IMF, lalu menyimpannya ke CSV dan database, sekaligus menjalankan query dan mencatat log proses.

## Tujuan

1. Menulis fungsi ekstraksi data dari URL.
2. Mentransformasi GDP dari Juta USD ke Miliar USD.
3. Memuat data ke file CSV dan database.
4. Menjalankan query pada database.
5. Mencatat progres eksekusi dengan timestamp.

## Struktur Folder

2.1 - ETL GDP Data/
├── etl_project_gdp.py       # Script utama
├── Countries_by_GDP.csv     # Hasil akhir dalam CSV
├── World_Economies.db       # Hasil akhir dalam database SQLite
└── etl_project_log.txt      # Log proses eksekusi

## Alur Program

1. **Extract** — scraping tabel GDP dari halaman Wikipedia (via arsip web.archive.org), ambil kolom `Country` dan GDP dari IMF, skip baris kosong/tanpa link/tanpa data.
2. **Transform** — ubah format angka currency jadi float, konversi dari Juta USD ke Miliar USD (dibagi 1000, dibulatkan 2 desimal), ganti nama kolom jadi `GDP_USD_billions`.
3. **Load** — simpan ke `Countries_by_GDP.csv` dan tabel `Countries_by_GDP` di database `World_Economies.db`.
4. **Query** — tampilkan negara dengan GDP ≥ 100 miliar USD.
5. **Logging** — setiap tahap dicatat waktunya ke `etl_project_log.txt`.

## Cara Menjalankan

pip install pandas numpy bs4
python etl_project_gdp.py

Hasil query (negara dengan GDP ≥ 100 miliar USD) akan tampil di terminal.

## Catatan Pribadi

Ini project ETL paling lengkap sejauh course ini — menggabungkan web scraping, transformasi data, load ke CSV & database, query SQL, sekaligus logging, semuanya dipisah rapi per fungsi (extract, transform, load_to_csv, load_to_db, run_query, log_progress).

