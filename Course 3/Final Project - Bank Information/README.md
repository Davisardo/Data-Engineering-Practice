# 2.2 - World's Largest Banks

**Practice Project: Acquiring and Processing Information on the World's Largest Banks**
Course 3 - Python Project for Data Engineering (IBM Data Engineering Professional Certificate)

## Skenario

Sebagai data engineer, membuat sistem otomatis untuk mengumpulkan daftar 10 bank terbesar di dunia berdasarkan kapitalisasi pasar (dalam miliar USD), lalu mengonversinya ke GBP, EUR, dan INR sesuai kurs yang tersedia. Data disimpan ke CSV dan database, siap dijalankan ulang tiap kuartal.

## Struktur Folder

2.2 - World's Largest Banks/
├── banks_project.py         # Script utama
├── exchange_rate.csv        # Data kurs mata uang
├── Largest_banks_data.csv   # Hasil akhir dalam CSV
├── Banks.db                 # Hasil akhir dalam database SQLite
└── code_log.txt             # Log proses eksekusi

## Alur Program

1. **Extract** — scraping tabel "By market capitalization" dari Wikipedia (via arsip web.archive.org), ambil nama bank dan Market Cap dalam USD.
2. **Transform** — baca kurs dari `exchange_rate.csv`, tambahkan 3 kolom baru: Market Cap dalam GBP, EUR, dan INR (dibulatkan 2 desimal).
3. **Load** — simpan ke `Largest_banks_data.csv` dan tabel `Largest_banks` di database `Banks.db`.
4. **Query** — jalankan 3 query: lihat semua data, rata-rata Market Cap dalam GBP, dan 5 nama bank teratas.
5. **Logging** — setiap tahap dicatat waktunya ke `code_log.txt`.

## Cara Menjalankan

pip install pandas numpy bs4 lxml
python banks_project.py

Hasil ketiga query akan tampil berurutan di terminal.

## Catatan Pribadi

Bagian tersulit di lab ini ada di fungsi `extract()` — kolom nama bank di tabel HTML-nya punya 2 link sekaligus (flag negara & nama bank), jadi harus diambil link yang kedua (index 1) supaya dapat nama banknya, bukan nama negaranya.