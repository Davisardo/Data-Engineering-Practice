# 3.3 - Creating a Python Package

**Lab: Creating a Python Package**
Course 3 - Python Project for Data Engineering (IBM Data Engineering Professional Certificate)

## Tujuan Lab Ini

- Membuat modul `basic` dengan beberapa fungsi.
- Membuat modul `stats` dengan beberapa fungsi.
- Membuat package Python bernama `mymath`.
- Memverifikasi package berfungsi dengan benar.

## Struktur Folder

3.3 - Creating a Python Package/
└── mymath/
    ├── __init__.py     # Menandai folder sebagai package, memuat semua modul
    ├── basic.py         # square(), double(), add()
    ├── stats.py         # mean(), median()
    └── geometry.py      # area_of_rectangle(), area_of_circle() (Practice Exercise)

## Konsep Package yang Dipakai

- **Modul** — file `.py` berisi fungsi-fungsi terkait (misal `basic.py` untuk operasi dasar, `stats.py` untuk statistik).
- **Package** — folder berisi banyak modul, ditandai dengan file `__init__.py` di dalamnya.
- **`__init__.py`** — mengimpor semua modul di dalam package saat package itu di-import, sehingga bisa diakses langsung lewat `namapackage.namamodul.namafungsi()`.

## Cara Menjalankan

python
>>> import mymath
>>> mymath.basic.add(3, 4)
7
>>> mymath.stats.mean([3, 4, 5])
4.0
>>> mymath.geometry.area_of_circle(5)
78.53975

## Catatan Pribadi

Bagian Practice Exercise (modul `geometry`) melatih cara menambah modul baru ke package yang sudah ada — cukup buat file modul baru, lalu update `__init__.py` supaya modul tersebut ikut ter-load saat package di-import.