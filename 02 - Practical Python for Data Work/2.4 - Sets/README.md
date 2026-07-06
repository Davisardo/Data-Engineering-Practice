# 2.4 - Sets

**Lab: Sets in Python**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 2 - Python Data Structures

## Tujuan Lab Ini

- Bekerja dengan set di Python.

## Struktur Folder

2.4 - Sets/
└── sets_demo.py

## Materi yang Dipelajari

1. **Set dasar** — koleksi unik (tanpa duplikat), ditulis dengan kurung kurawal `{}`, otomatis membuang elemen yang sama.
2. **Konversi list ke set** — `set(list_name)`, cara umum untuk deduplikasi data.
3. **add() / remove()** — tambah elemen (duplikat diabaikan), hapus elemen berdasarkan nilai.
4. **Set Logic Operations**:
   - `intersection()` / `&` — elemen yang ada di kedua set.
   - `difference()` — elemen yang hanya ada di satu set.
   - `union()` — gabungan semua elemen tanpa duplikat.
   - `issubset()` / `issuperset()` — cek relasi antar set.

## Cara Menjalankan

python sets_demo.py

## Cheat Sheet: Set untuk Data Engineering

**Kenapa penting:** set adalah tool tercepat untuk **deduplikasi** dan **perbandingan antar dataset** — dua kebutuhan yang sangat sering muncul saat membersihkan atau membandingkan data.

**Analogi dengan SQL JOIN:**

| Operasi Set | Setara SQL |
|---|---|
| `set_A & set_B` (intersection) | `INNER JOIN` — data yang ada di keduanya |
| `set_A - set_B` (difference) | `LEFT JOIN ... WHERE B IS NULL` — hanya di A |
| `set_A \| set_B` (union) | `UNION` — gabungan semua data unik |
| `set_A.issubset(set_B)` | Cek apakah semua isi A ada di B |

**Contoh kasus nyata:**
```python
users_system_a = {"alice", "bob", "carol"}
users_system_b = {"bob", "carol", "dave"}

only_in_a = users_system_a - users_system_b   # {"alice"} -> user yang belum migrasi
only_in_b = users_system_b - users_system_a   # {"dave"}  -> user baru di sistem B
common = users_system_a & users_system_b       # {"bob", "carol"}
```

**Kenapa lebih cepat dari list:** operasi pencarian (`in`) dan deduplikasi di set punya kompleksitas rata-rata O(1), sementara di list bisa O(n) — signifikan bedanya kalau data yang diproses jutaan baris.

**Perangkap:**
- Set **tidak terurut** — jangan andalkan urutan elemen saat print atau iterasi.
- Elemen set harus immutable (sama seperti key dictionary) — list tidak bisa masuk set, tapi tuple bisa.

## Catatan Pribadi

Bukti nyata di lab ini: `sum([1, 2, 2, 1])` = 6, tapi `sum(set([1, 2, 2, 1]))` = 3 — karena set otomatis membuang duplikat sebelum dihitung. Ini jadi pengingat penting: kalau butuh hitung total/statistik dari data unik, konversi ke set dulu sebelum agregasi.