# 1.2 - ETL Extract Transform Load

**Lab: Ekstraksi, Transformasi, dan Memuat Data menggunakan Python**
Course 3 - Python Project for Data Engineering (IBM Data Engineering Professional Certificate)

## Tujuan Lab Ini

- Membaca tipe file CSV, JSON, dan XML.
- Mengekstrak data dari berbagai tipe file tersebut.
- Mentransformasikan data ke format yang seragam.
- Menyimpan hasil akhir dalam format siap dimuat ke database.

## Struktur Folder

1.2 - ETL Extract Transform Load/
├── etl_code.py       # Script utama ETL
├── source1.csv / source2.csv / source3.csv
├── source1.json / source2.json / source3.json
└── source1.xml / source2.xml / source3.xml

Catatan: `transformed_data.csv` dan `log_file.txt` sengaja tidak di-commit (ada di `.gitignore`) karena itu hasil eksekusi program, bisa dibuat ulang kapan saja dengan menjalankan `etl_code.py`.

## Alur Program

1. **Extract** — baca semua file csv, json, xml di folder ini, gabungkan jadi satu tabel data (`name`, `height`, `weight`).
2. **Transform** — ubah satuan tinggi (inci → meter) dan berat (pon → kilogram).
3. **Load** — simpan hasil akhir ke `transformed_data.csv`.
4. Setiap tahap dicatat waktunya ke `log_file.txt`.

## Cara Menjalankan

pip install pandas
python etl_code.py

Hasil transformasi akan tampil di terminal, dan file `transformed_data.csv` + `log_file.txt` akan terbentuk di folder ini.

## Catatan Pribadi

Data sumber (`source1-3.csv/json/xml`) didapat dari link resmi lab IBM Skills Network. Lab ini dikerjakan mandiri di VS Code lokal untuk latihan membangun pipeline ETL sederhana dari nol.