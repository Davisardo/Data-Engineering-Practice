# 4.3 - Selecting Data in a DataFrame

**Practice Lab: Selecting Data in a Dataframe**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 4 - Working with Data in Python

## Tujuan Lab Ini

- Memahami struktur DataFrame dan Series di Pandas.
- Memilih kolom, baris, dan cell tertentu menggunakan `loc()` dan `iloc()`.
- Melakukan slicing pada DataFrame.

## Struktur Folder

4.3 - Selecting Data in a DataFrame/
└── dataframe_selection.ipynb

## Catatan Format

Lab ini adalah **notebook pertama** yang dikerjakan pakai Jupyter di VS Code (bukan `.py` script biasa) — cocok karena fokusnya eksplorasi interaktif tabel data, bukan pipeline otomatis.

## Materi yang Dipelajari

1. **DataFrame** — struktur data 2 dimensi (tabel), dibuat dari dictionary lewat `pd.DataFrame(dict)`.
2. **Column Selection** — `df['col']` (1 kurung) hasilnya **Series**, `df[['col']]` (2 kurung) hasilnya **DataFrame**.
3. **`iloc[row, col]`** — akses berdasarkan **posisi angka** (integer location).
4. **`loc[row, col]`** — akses berdasarkan **nama/label**.
5. **`set_index()`** — mengubah kolom tertentu jadi index, supaya `loc()` bisa pakai nama yang lebih bermakna.
6. **Slicing** — `iloc[0:2]` **tidak termasuk** batas akhir (seperti list Python biasa), sementara `loc[0:2]` **termasuk** batas akhir (inklusif kedua ujung).

## Cara Menjalankan

Buka file `.ipynb` di VS Code (dengan Jupyter extension terinstall), jalankan tiap cell dengan `Shift+Enter`.

## Cheat Sheet: Pandas Selection untuk Data Engineering

**Kenapa krusial:** hampir seluruh pipeline ETL yang sudah dikerjakan sejauh course ini (2.1, 2.2, Final Project) internnya pakai Pandas. Skill memilih data dengan tepat adalah dasar sebelum bisa melakukan transformasi/filtering data lebih lanjut.

**Perbedaan `iloc` vs `loc` — perangkap umum:**

| | `iloc` | `loc` |
|---|---|---|
| Akses berdasarkan | Posisi angka (0, 1, 2, ...) | Nama/label |
| Slicing batas akhir | **Tidak termasuk** (`0:2` = index 0,1) | **Termasuk** (`0:2` = index 0,1,2) |
| Kapan dipakai | Index masih default angka, atau butuh posisi pasti | Index sudah diganti jadi label bermakna (nama, tanggal, ID) |

**Kaitan dengan `set_index()` di real project:** mengubah index jadi kolom yang unik (misal `customer_id`, `date`) adalah pola umum sebelum melakukan lookup cepat — mirip primary key di database, membuat pencarian baris tertentu jadi lebih efisien dan bermakna dibanding pakai index angka default.

**Perbedaan tipe hasil seleksi kolom — penting untuk operasi lanjutan:**
```python
df['Salary']      # Series -> bisa langsung .sum(), .mean(), dst
df[['Salary']]    # DataFrame -> perlu .sum() per kolom, hasilnya beda struktur
```
Salah pilih bracket tunggal/ganda bisa bikin method berikutnya error atau hasilnya beda struktur dari yang diharapkan.

## Catatan Pribadi

Lab ini jadi titik balik penting: mulai sekarang lab-lab yang lebih fokus eksplorasi data (Pandas, visualisasi) akan dikerjakan pakai Jupyter Notebook di VS Code, sementara lab yang fokus ke pipeline/automation script tetap pakai `.py` biasa — mengikuti pola kerja nyata di industri data engineering.