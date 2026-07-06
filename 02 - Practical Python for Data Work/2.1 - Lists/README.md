# 2.1 - Lists

**Lab: Lists in Python**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 2 - Python Data Structures

## Tujuan Lab Ini

- Melakukan operasi list di Python: indexing, manipulasi list, copy/clone list.

## Struktur Folder

2.1 - Lists/
└── lists_demo.py

## Materi yang Dipelajari

1. **List dasar & indexing** — list bisa berisi banyak tipe data sekaligus (termasuk nested list/tuple), diakses lewat index positif/negatif.
2. **Slicing** — ambil sebagian elemen list, misal `L[3:5]`.
3. **extend() vs append()** — `extend()` menambah elemen secara flat, `append()` menambah 1 elemen (bisa berupa list utuh/nested).
4. **Mutability** — isi list bisa diubah langsung lewat index (`A[0] = 'baru'`), beda dengan string yang immutable.
5. **del** — menghapus elemen berdasarkan index.
6. **split()** — ubah string jadi list berdasarkan delimiter (default: spasi).
7. **Copy by reference vs Clone by value** — `B = A` membuat `B` menunjuk objek memory yang sama dengan `A` (perubahan saling memengaruhi); `B = A[:]` membuat copy independen.

## Cara Menjalankan

python lists_demo.py

## Cheat Sheet: List untuk Data Engineering

**Kenapa penting:** baris data mentah dari CSV/JSON sering berbentuk list of values sebelum diubah jadi struktur lebih rapi (dict, DataFrame). List of dicts (`[{...}, {...}]`) adalah representasi umum data JSON/API sebelum di-load ke Pandas.

**Perangkap yang sering bikin bug:**

| Kasus | Yang Terjadi | Solusi |
|---|---|---|
| `B = A` lalu ubah `B` | `A` ikut berubah (reference sama) | Pakai `B = A[:]` atau `A.copy()` |
| Pakai `append()` untuk gabung 2 list | Hasilnya nested, bukan flat | Pakai `extend()` |
| List di-passing ke fungsi lalu diubah | List asli ikut berubah (mutable) | Clone dulu sebelum diubah di dalam fungsi |
| Loop sambil `del` elemen list | Index bergeser, bisa skip elemen | Loop dari belakang, atau pakai list comprehension |

**Method penting yang belum dibahas di lab ini:**
- `sorted(list)` vs `list.sort()` — yang pertama hasil baru, yang kedua ubah in-place.
- `list.pop(index)` — hapus & sekaligus ambil nilainya.
- List comprehension: `[x for x in data if kondisi]` — cara idiomatik filter/transformasi data.

**Kaitan dengan tool selanjutnya:** `pd.DataFrame(list_of_dicts)` untuk bikin DataFrame dari list; hasil `response.json()` dari API biasanya berupa list; `cursor.fetchall()` dari database mengembalikan list of tuples.

## Catatan Pribadi

Konsep copy vs clone kelihatan sepele, tapi paling sering jadi sumber bug tersembunyi saat kerja dengan data dalam skala besar — terutama saat fungsi memodifikasi list yang di-passing sebagai parameter tanpa disadari efeknya ke variabel asli di luar fungsi.