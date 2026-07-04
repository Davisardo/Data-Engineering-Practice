# 3.1 - Static Code Analysis

**Lab: Static Code Analysis (Opsional)**
Course 3 - Python Project for Data Engineering (IBM Data Engineering Professional Certificate)

## Tujuan Lab Ini

- Install package `pylint`.
- Menjalankan static code analysis pada program Python.
- Memahami compliance score dan cara membacanya.
- Memperbaiki kesalahan umum untuk meningkatkan skor.

## Struktur Folder

3.1 - Static Code Analysis/
├── sample1.py     # Versi kode "kotor" (skor 0.00/10)
└── sample2.py     # Versi kode sudah diperbaiki (skor 10.00/10)

## Masalah yang Diperbaiki

| Masalah | Kode Pylint |
|---|---|
| Module docstring hilang | `missing-module-docstring` |
| Function docstring hilang | `missing-function-docstring` |
| Penamaan variabel tidak UPPER_CASE (konstanta) | `invalid-name` |
| Pakai `.format()` alih-alih f-string | `consider-using-f-string` |
| Newline hilang di akhir file | `missing-final-newline` |

## Cara Menjalankan

pip install pylint
pylint sample1.py
pylint sample2.py

Hasil: `sample1.py` mendapat skor 0.00/10 (menunjukkan semua masalah umum), `sample2.py` mendapat skor 10.00/10 (semua masalah sudah diperbaiki).

## Catatan Pribadi

Lab ini opsional, tapi saya kerjakan karena penasaran soal code quality tooling. Versi `pylint` di instruksi asli (2.11.1) sudah terlalu lama dan tidak kompatibel dengan Python 3.13 (dependency `wrapt` memakai fungsi yang sudah dihapus), jadi saya pakai versi terbaru pylint — hasil dan jenis errornya tetap sama secara prinsip.