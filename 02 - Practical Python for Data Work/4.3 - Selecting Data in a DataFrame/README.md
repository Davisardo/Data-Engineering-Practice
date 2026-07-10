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


## Reading: Pandas Series, DataFrame Attributes, dan Conditional Filtering

Materi reading tambahan dari course, memperkenalkan konsep Series secara mandiri dan beberapa method DataFrame penting yang belum dipraktikkan di lab hands-on.

### Pandas Series — Array 1 Dimensi dengan Label

```python
import pandas as pd

data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)
# Index otomatis 0,1,2,3,4 -- bisa diganti label custom
```

**Akses elemen Series:**
```python
print(s[2])       # akses berdasarkan label -> 30
print(s.iloc[3])  # akses berdasarkan posisi -> 40
print(s[1:4])     # slicing berdasarkan label
```

**Attribute & method penting Series (belum dipraktikkan di lab):**
| Attribute/Method | Fungsi |
|---|---|
| `.values` | Data Series sebagai array NumPy |
| `.index` | Label/index Series |
| `.shape` | Dimensi Series |
| `.size` | Jumlah elemen |
| `.mean()`, `.sum()`, `.min()`, `.max()` | Statistik ringkasan |
| `.unique()`, `.nunique()` | Nilai unik / jumlah nilai unik |
| `.sort_values()`, `.sort_index()` | Urutkan berdasarkan nilai atau index |
| `.isnull()`, `.notnull()` | Cek data kosong (NaN) |
| `.apply()` | Terapkan fungsi custom ke tiap elemen |

### DataFrame — Konsep Tambahan

**Conditional Filtering — belum dipraktikkan di lab hands-on, tapi krusial:**
```python
# Filter baris berdasarkan kondisi (mirip WHERE di SQL)
high_above_25 = df[df['Age'] > 25]
```
Ini pola yang **sangat sering** dipakai di data cleaning/analysis — filter baris berdasarkan syarat tertentu, dibahas juga di konteks lab Conditions sebelumnya (`&`/`|` untuk kombinasi kondisi).

**unique() — cari nilai unik di satu kolom:**
```python
unique_ages = df['Age'].unique()
```

**Saving DataFrame ke file:**
```python
df.to_csv('output.csv', index=False)
```
`index=False` mencegah kolom index bawaan Pandas ikut tersimpan sebagai kolom terpisah di file CSV — pola yang sudah dipakai berkali-kali di lab-lab ETL sebelumnya.

**Reading CSV — dasar sebelum dipraktikkan di lab-lab ETL selanjutnya:**
```python
df = pd.read_csv('your_file.csv')
```

### Tabel Lengkap Attribute & Method DataFrame

| Attribute/Method | Fungsi |
|---|---|
| `.shape` | Dimensi (jumlah baris, kolom) |
| `.info()` | Ringkasan tipe data & jumlah non-null per kolom |
| `.describe()` | Statistik ringkasan untuk kolom numerik (mean, std, min, max, dst) |
| `.head()`, `.tail()` | Lihat n baris pertama/terakhir |
| `.mean()`, `.sum()`, `.min()`, `.max()` | Statistik per kolom |
| `.sort_values()` | Urutkan berdasarkan 1 atau lebih kolom |
| `.groupby()` | Kelompokkan data untuk agregasi (mirip `GROUP BY` di SQL) |
| `.fillna()`, `.drop()`, `.rename()` | Isi data kosong, hapus kolom, ganti nama kolom |
| `.apply()` | Terapkan fungsi custom ke elemen/baris/kolom |

**Relevansi ke data engineering:** `.info()` dan `.describe()` adalah dua method **pertama** yang biasa dipanggil setelah load data baru — persis seperti tahap "structural check" dan "completeness check" di blueprint file eksplorasi data yang lebih besar (mirip pola `explore.py` di project-project data engineering nyata).

