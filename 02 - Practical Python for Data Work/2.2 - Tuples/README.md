# 2.2 - Tuples

**Lab: Tuples in Python**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 2 - Python Data Structures

## Tujuan Lab Ini

- Melakukan operasi dasar tuple di Python: indexing, slicing, sorting.

## Struktur Folder

2.2 - Tuples/
└── tuples_demo.py

## Materi yang Dipelajari

1. **Tuple dasar** — dibuat dengan tanda kurung `()`, bisa campur banyak tipe data.
2. **Indexing & Negative Indexing** — akses elemen lewat posisi, sama seperti list.
3. **Concatenate** — gabung 2 tuple dengan `+`, hasilnya tuple baru.
4. **Slicing** — ambil sebagian elemen, misal `tuple2[0:3]`.
5. **Sorting** — `sorted()` pada tuple menghasilkan **list** baru, bukan tuple (karena tuple immutable).
6. **Nested Tuple** — tuple di dalam tuple, diakses berlapis (`NestedT[4][1][0]`).

## Cara Menjalankan

python tuples_demo.py

## Cheat Sheet: Tuple untuk Data Engineering

**Beda utama dengan list:** tuple bersifat **immutable** — sekali dibuat, isinya tidak bisa diubah. Ini justru jadi kelebihan saat kamu butuh data yang harus tetap konsisten sepanjang pipeline (misal koordinat, nama kolom fixed, atau baris hasil query).

**Kaitan langsung dengan tools nyata:**
- `cursor.fetchall()` di database Python (sqlite3, psycopg2, dst) selalu mengembalikan **list of tuples** — setiap baris hasil query adalah tuple, bukan list, karena isinya memang tidak seharusnya diubah.
- Tuple sering dipakai sebagai **key di dictionary** (list tidak bisa, karena harus hashable/immutable) — misal `{(2024, 1): "Januari 2024"}` untuk composite key.
- Nested tuple/dict adalah pola yang sama dengan **navigasi JSON API response** bertingkat, misal `data["users"][0]["address"]["city"]` — skill akses `NestedT[4][1][0]` di lab ini langsung terpakai di sana.

**Kapan pakai tuple vs list:**

| Situasi | Pilihan |
|---|---|
| Data tidak boleh berubah (koordinat, konstanta, baris DB) | Tuple |
| Data akan sering ditambah/dihapus/diubah | List |
| Butuh jadi key dictionary atau elemen set | Tuple (list tidak bisa) |
| Return value fungsi dengan beberapa nilai (`return x, y`) | Tuple (implisit) |

## Catatan Pribadi

Detail kecil yang penting: fungsi `sorted()` pada tuple mengembalikan tipe `list`, bukan tuple baru — ini konsisten dengan sifat immutable tuple, karena "mengurutkan" berarti membuat struktur data baru yang boleh diubah lagi nantinya.