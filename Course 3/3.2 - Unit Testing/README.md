# 3.2 - Unit Testing

**Lab: Unit Testing**
Course 3 - Python Project for Data Engineering (IBM Data Engineering Professional Certificate)

## Tujuan Lab Ini

- Menulis unit test untuk menguji sebuah fungsi.
- Menjalankan unit test dan memahami hasilnya.

## Struktur Folder

3.2 - Unit Testing/
├── mymodule.py         # Fungsi yang diuji
└── test_mymodule.py    # Kumpulan unit test

## Fungsi yang Diuji

Lab ini bertahap menguji 3 fungsi berbeda di `mymodule.py`:

1. `square(number)` — mengembalikan kuadrat suatu angka.
2. `double(number)` — mengembalikan dua kali lipat suatu angka.
3. `add(a, b)` — mengembalikan hasil penjumlahan dua nilai (bagian latihan mandiri).

## Konsep Unit Testing yang Dipakai

- `unittest.TestCase` — class dasar untuk mengelompokkan test yang berkaitan.
- Method wajib diawali kata `test` supaya otomatis terdeteksi dan dijalankan.
- `assertEqual(a, b)` — memastikan nilai `a` sama dengan `b`.
- `assertNotEqual(a, b)` — memastikan nilai `a` tidak sama dengan `b` (dipakai untuk kasus yang seharusnya gagal).
- `unittest.main()` — menjalankan semua test di file saat script dieksekusi langsung.

## Cara Menjalankan

python test_mymodule.py

Output `OK` di baris terakhir menandakan semua test lolos. Output `FAILED` menandakan ada test yang gagal, beserta detail test mana yang bermasalah.

## Catatan Pribadi

Bagian latihan mandiri (fungsi `add()`) melatih menulis test case untuk berbagai tipe data sekaligus — bilangan bulat, desimal, string (concatenation), dan kasus negatif yang harus dipastikan TIDAK menghasilkan nilai tertentu (pakai `assertNotEqual`).