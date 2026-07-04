# 1.2 - Working with Types

**Lab: Working with Types in Python**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 1 - Python Basics

## Tujuan Lab Ini

- Memahami tipe data dasar di Python: int, float, str, bool.
- Melakukan konversi (typecasting) antar tipe data.

## Struktur Folder

1.2 - Working with Types/
└── types_demo.py

## Materi yang Dipelajari

- **Tipe data dasar**: `int`, `float`, `str`, `bool`, dicek pakai `type()`.
- **Typecasting**: konversi antar tipe, misal `float(2)`, `int(1.1)` (kehilangan desimal), `int('1')`, `str(1.2)`.
- **Boolean sebagai angka**: `True`/`False` bisa dikonversi ke `1`/`0` dan sebaliknya.
- **Operator pembagian**: `/` selalu menghasilkan `float`, `//` (integer division) menghasilkan `int`.
- **Hasil perbandingan** (`==`) selalu bertipe `bool`.

## Cara Menjalankan

python types_demo.py

## Catatan Pribadi

Poin penting: konversi float ke int **membuang** bagian desimal, bukan membulatkan (`int(1.1)` = `1`, bukan error atau pembulatan). Juga string harus benar-benar berisi angka murni untuk bisa dikonversi ke `int`/`float`, kalau tidak akan `ValueError`.