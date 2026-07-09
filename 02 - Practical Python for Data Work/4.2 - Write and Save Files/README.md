# 4.2 - Write and Save Files

**Lab: Write and Save Files in Python**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 4 - Working with Data in Python

## Tujuan Lab Ini

- Menulis ke file.
- Menambahkan (append) ke file.
- Menyalin (copy) file.

## Struktur Folder

4.2 - Write and Save Files/
├── write_file_demo.py
├── Example2.txt
├── Example3.txt
├── members.txt
└── inactive.txt

## Materi yang Dipelajari

1. **Mode 'w'** — menulis file, **menimpa total** semua isi lama.
2. **Mode 'a'** — menambah (append) ke akhir file, tanpa menghapus data lama.
3. **Mode gabungan** — `r+` (baca+tulis, tidak truncate), `w+` (tulis+baca, truncate), `a+` (append+baca, buat file baru kalau belum ada).
4. **`tell()`** — cek posisi cursor saat ini di file (dalam byte).
5. **`seek(offset, from)`** — pindahkan cursor ke posisi tertentu.
6. **`truncate()`** — hapus semua data setelah posisi cursor saat ini, penting untuk update file tanpa menyisakan "sampah" data lama.
7. **Copy file** — baca file sumber baris per baris, tulis ke file tujuan.
8. **Exercise nyata** — membersihkan data member tidak aktif dari file teks, mensimulasikan data cleaning berbasis file murni (tanpa Pandas).

## Cara Menjalankan

python write_file_demo.py

## Cheat Sheet: File Writing untuk Data Engineering

**Kenapa krusial:** semua fungsi `load_to_csv()` di project ETL sebelumnya pada dasarnya melakukan operasi tulis file. Memahami mode `'w'` vs `'a'` sangat penting — salah pilih bisa **menghapus data produksi** secara tidak sengaja.

**Koneksi langsung dengan `log_progress()` di lab-lab ETL sebelumnya:**
```python
# Pola yang sudah dipakai di semua lab ETL (2.1, 2.2, Final Project)
with open(log_file, "a") as f:   # mode 'a' -> log baru DITAMBAH, bukan menghapus riwayat lama
    f.write(timestamp + ' : ' + message + '\n')
```
Ini contoh nyata kenapa append mode penting: kalau pakai `'w'`, tiap kali script dijalankan, seluruh riwayat log sebelumnya akan hilang.

**Kapan pakai mode apa:**

| Mode | Kapan Dipakai |
|---|---|
| `'w'` | Bikin file baru dari nol, atau memang sengaja ingin menimpa total |
| `'a'` | Logging, menambah data historis tanpa menghapus yang lama |
| `'r+'` | Update sebagian isi file yang sudah ada, tanpa menghapus semuanya |
| `'a+'` | Baca sekaligus siap menambah data, buat file baru otomatis kalau belum ada |

**Pola `truncate()` untuk update-in-place** — dipakai persis di exercise akhir lab ini: filter data langsung di file yang sama (bukan file baru), tulis ulang cuma yang relevan, lalu `truncate()` untuk membuang sisa data lama yang lebih panjang.

## Catatan Pribadi

Exercise akhir lab ini (`clean_files()`) adalah contoh nyata **data cleaning tanpa Pandas** — murni pakai file I/O dan list comprehension (`[member for member in members if 'no' in member]`, konsep yang sudah dipelajari sejak lab List). Ini bagus untuk memahami apa yang terjadi "di balik layar" saat nanti pakai `pd.read_csv()` dan `df[df['active'] == 'no']` — konsepnya sama, cuma Pandas jauh lebih ringkas dan optimal.

## Reading: Tabel Lengkap Mode File di Python

Materi reading tambahan dari course, merangkum seluruh mode file yang tersedia di Python — termasuk mode `'x'` (exclusive) dan varian binary yang belum dipraktikkan di atas.

### Tabel Referensi Mode File

| Mode | Deskripsi |
|---|---|
| `'r'` | Read — buka file yang **sudah ada** untuk dibaca. Error kalau file tidak ada. |
| `'w'` | Write — buat file baru untuk ditulis. **Menimpa total** kalau file sudah ada. |
| `'a'` | Append — buka file untuk ditambah datanya. Membuat file baru kalau belum ada. |
| `'x'` | Exclusive creation — buat file baru, tapi **error kalau file sudah ada** (mencegah menimpa tidak sengaja). |
| `'r+'` | Read + Write — baca dan tulis file yang sudah ada, tanpa truncate otomatis. |
| `'w+'` | Write + Read — buat file baru untuk tulis & baca, menimpa kalau sudah ada. |
| `'a+'` | Append + Read — tambah data & bisa baca, membuat file baru kalau belum ada. |
| `'x+'` | Exclusive + Read/Write — buat file baru untuk baca/tulis, error kalau sudah ada. |
| `'rb'` / `'wb'` / `'ab'` | Versi **binary** dari `r`/`w`/`a` — untuk file non-teks (gambar, PDF, database file). |
| `'rt'` / `'wt'` / `'at'` | Versi eksplisit **text mode** — sebenarnya default untuk file teks, jarang perlu ditulis eksplisit. |

### Mode 'x' — Exclusive Creation (Belum Dipraktikkan)
Berguna saat kamu ingin **mencegah menimpa file secara tidak sengaja** — misal saat generate laporan harian, kamu mau error muncul kalau file hari itu sudah pernah dibuat, daripada diam-diam menimpanya.
```python
try:
    with open('laporan_2026-07-09.txt', 'x') as file:
        file.write("Data laporan...")
except FileExistsError:
    print("File laporan hari ini sudah ada, tidak ditimpa.")
```

**Relevansi ke data engineering:** mode `'x'` ini best practice untuk output pipeline yang **tidak boleh double-run** tanpa disadari (misal file snapshot harian) — kombinasikan dengan exception handling (`try/except FileExistsError`) yang sudah dipelajari di lab 3.4.
