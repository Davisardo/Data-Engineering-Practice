# 1.4 - String Operations

**Lab: String Operations**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 1 - Python Basics

## Tujuan Lab Ini

- Bekerja dengan string.
- Melakukan operasi pada string.
- Manipulasi string lewat indexing dan escape sequence.

## Struktur Folder

1.4 - String Operations/
└── strings_demo.py

## Materi yang Dipelajari

1. **Dasar string** — kutip ganda/tunggal, spasi, karakter spesial.
2. **Indexing** — akses karakter lewat posisi (mulai dari 0), termasuk negative indexing dari belakang.
3. **Slicing & Stride** — ambil sebagian string (`name[0:4]`), lompat tiap N elemen (`name[::2]`).
4. **Concatenate & Replikasi** — gabung string dengan `+`, ulangi dengan `*`.
5. **Escape Sequences** — `\n` (baris baru), `\t` (tab), `\\` (backslash), raw string (`r"..."`).
6. **Method string** — `upper()`, `replace()`, `find()` (return -1 kalau tidak ketemu), `split()`.
7. **RegEx (`re` module)** — `search()`, `findall()`, `split()`, `sub()`, special sequence `\d` dan `\W`.

## Cara Menjalankan

python strings_demo.py

## Catatan Pribadi

Poin penting yang mudah salah paham: `"1" + "2"` hasilnya `"12"` (concatenation string), bukan `3` (penjumlahan angka) — karena kedua operand bertipe string, bukan int. Ini beda dengan lab Types sebelumnya yang membahas konversi tipe data.