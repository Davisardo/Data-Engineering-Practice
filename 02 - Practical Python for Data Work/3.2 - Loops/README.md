# 3.2 - Loops

**Lab: Loops in Python**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 3 - Python Programming Fundamentals

## Tujuan Lab Ini

- Bekerja dengan loop (for dan while).

## Struktur Folder

3.2 - Loops/
└── loops_demo.py

## Materi yang Dipelajari

1. **range()** — objek ordered sequence (bukan list) untuk kontrol jumlah iterasi.
2. **for loop** — dua gaya: akses via index (`for i in range(len(list))`) atau akses langsung elemen (`for item in list`), yang kedua lebih Pythonic.
3. **enumerate()** — dapat index dan value sekaligus dalam satu loop.
4. **while loop** — mengulang selama kondisi masih True, cocok kalau jumlah iterasi tidak diketahui pasti dari awal.
5. **break** — hentikan loop total, langsung keluar.
6. **continue** — skip iterasi saat ini, lanjut ke iterasi berikutnya.

## Cara Menjalankan

python loops_demo.py

## Cheat Sheet: Loop untuk Data Engineering

**Kenapa penting:** loop adalah tool paling sering dipakai di pipeline data — dari iterasi file di folder (`for file in glob.glob("*.csv")`, seperti di lab ETL sebelumnya), sampai looping baris data untuk validasi/transformasi satu per satu.

**Kapan pakai for vs while:**

| Situasi | Loop yang Cocok |
|---|---|
| Jumlah iterasi sudah pasti (list, range, file di folder) | `for` |
| Iterasi sampai kondisi tertentu terpenuhi, jumlahnya belum pasti | `while` |
| Retry koneksi API sampai berhasil / limit tercapai | `while` |
| Baca data streaming sampai tanda "selesai" | `while` |

**Pola umum data validation dengan break/continue:**
```python
for row in dataset:
    if row['value'] is None:
        continue   # skip baris tidak valid, lanjut ke baris berikutnya
    if row['critical_error']:
        break        # data korup total, hentikan proses
    process(row)
```

**Perangkap umum:**
- Mengubah list yang sedang di-loop (`del`, `remove`) bisa bikin index bergeser dan skip elemen — biasanya lebih aman buat list baru daripada modifikasi in-place saat looping.
- `while` loop yang kondisinya tidak pernah jadi False = **infinite loop**, pastikan selalu ada langkah yang mengubah kondisi di dalam loop (misal `i = i + 1`).

## Catatan Pribadi

Bagian quiz terakhir (skip kelipatan 3, stop kalau > 12) adalah contoh bagus kombinasi `continue` dan `break` dalam satu loop — pola ini persis yang dipakai saat filter data sekaligus membatasi jumlah baris yang diproses (mirip logic `count < 50` di lab web scraping sebelumnya).