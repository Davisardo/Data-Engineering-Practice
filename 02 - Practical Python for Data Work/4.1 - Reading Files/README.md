# 4.1 - Reading Files

**Lab: Reading Files Python**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 4 - Working with Data in Python

## Tujuan Lab Ini

- Membaca file teks.

## Struktur Folder

4.1 - Reading Files/
├── read_file_demo.py
└── example1.txt

## Materi yang Dipelajari

1. **open() / close()** — cara dasar membuka & menutup file, wajib `close()` manual kalau tidak pakai `with`.
2. **Pola `with open(...) as file:`** — best practice, otomatis menutup file meski terjadi error di tengah proses.
3. **read()** — baca seluruh isi file jadi satu string.
4. **read(n)** — baca sejumlah `n` karakter, posisi baca **melanjutkan** dari pemanggilan sebelumnya (tidak mulai dari awal lagi).
5. **readline()** — baca 1 baris saja, bisa dibatasi jumlah karakter (tapi tidak akan melewati batas baris).
6. **Loop `for line in file:`** — iterasi tiap baris file satu per satu.
7. **readlines()** — baca semua baris sekaligus, hasil berupa list (tiap elemen = 1 baris).

## Cara Menjalankan

python read_file_demo.py

## Cheat Sheet: File I/O untuk Data Engineering

**Kenapa krusial:** membaca file adalah **langkah pertama** hampir semua pipeline ETL — sebelum `extract()` data dari CSV/JSON, harus paham dasar buka-baca-tutup file.

**Wajib pakai `with`, bukan `open()`/`close()` manual:**
```python
# Rawan bug: kalau ada error sebelum close(), file tetap "bocor" terkuci
file1 = open("data.txt", "r")
data = file1.read()
file1.close()

# Best practice: otomatis tertutup meski terjadi exception di dalam blok
with open("data.txt", "r") as file1:
    data = file1.read()
```

**Kapan pakai `read()` vs loop per baris — krusial untuk file besar:**

| Method | Kapan Dipakai |
|---|---|
| `read()` | File kecil, muat semuanya ke memory sekaligus aman |
| `for line in file:` | File **besar** (jutaan baris) — proses 1 baris per waktu, hemat memory |
| `readlines()` | Butuh akses random ke baris tertentu via index, tapi file tetap tidak terlalu besar |

Untuk file berukuran GB, `read()` bisa bikin program **crash karena kehabisan memory**. Loop `for line in file:` jauh lebih aman karena Python hanya memuat 1 baris ke memory pada satu waktu.

**Kaitan dengan tools nyata:** ini fondasi sebelum `pd.read_csv()` di Pandas — internal Pandas melakukan hal serupa (baca file per chunk), tapi dengan optimasi jauh lebih baik. Paham cara kerja manual ini membantu debug kalau suatu saat `pd.read_csv()` gagal atau perlu parameter `chunksize` untuk file sangat besar.

## Catatan Pribadi

Poin penting yang terbukti di lab ini: pemanggilan `read(n)` berkali-kali dalam 1 blok `with` **melanjutkan posisi** dari pembacaan sebelumnya, bukan mengulang dari awal — file object menyimpan "cursor" posisi baca internal, mirip bookmark yang bergerak maju setiap kali data dibaca.