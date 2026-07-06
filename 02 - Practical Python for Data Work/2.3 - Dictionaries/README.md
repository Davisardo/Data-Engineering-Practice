# 2.3 - Dictionaries

**Lab: Dictionaries in Python**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 2 - Python Data Structures

## Tujuan Lab Ini

- Membuat dictionary dan mengakses elemennya.

## Struktur Folder

2.3 - Dictionaries/
└── dictionaries_demo.py

## Materi yang Dipelajari

1. **Dictionary dasar** — pasangan key-value, ditulis dengan kurung kurawal `{}`, key dipisah value dengan `:`.
2. **Key yang valid** — bisa string, angka, atau tuple (harus immutable), tapi **tidak bisa** list.
3. **Akses value** — lewat key (`dict["key"]`), bukan index angka seperti list.
4. **keys() dan values()** — mengembalikan objek dinamis (`dict_keys`, `dict_values`), bukan list statis.
5. **Tambah/hapus entry** — `dict["key_baru"] = value` untuk tambah, `del dict["key"]` untuk hapus.
6. **Cek keberadaan key** — operator `in`, misal `"key" in my_dict`.

## Cara Menjalankan

python dictionaries_demo.py

## Cheat Sheet: Dictionary untuk Data Engineering

**Kenapa krusial:** dictionary adalah struktur data paling sering muncul di data engineering, karena hampir semua data JSON (API response, config file, NoSQL document) direpresentasikan sebagai dict di Python.

**Method penting yang sering dipakai (belum dibahas eksplisit di lab ini):**

| Method | Fungsi |
|---|---|
| `dict.get(key, default)` | Ambil value, aman dari `KeyError` — kasih nilai default kalau key tidak ada |
| `dict.items()` | Iterasi pasangan `(key, value)` sekaligus, biasa dipakai di `for k, v in dict.items():` |
| `dict.update(other_dict)` | Gabungkan/timpa dictionary dengan dictionary lain |
| `dict.pop(key)` | Hapus key sekaligus ambil valuenya (mirip `list.pop()`) |
| `{**dict1, **dict2}` | Merge 2 dictionary jadi satu (unpacking) |

**Kaitan langsung dengan tools nyata:**
- `response.json()` dari request API hampir selalu berupa dict atau list of dict.
- `pd.DataFrame(list_of_dicts)` — cara umum ubah list of dict jadi DataFrame Pandas.
- Environment variable & file konfigurasi (`.env`, `config.json`) sering dibaca sebagai dictionary.
- Dictionary adalah dasar konsep **hash map**, struktur data dengan lookup super cepat (O(1)) — penting untuk optimasi saat data besar.

**Perangkap umum:**
- Akses key yang tidak ada dengan `dict["key"]` akan **error** (`KeyError`). Pakai `dict.get("key")` kalau tidak yakin key-nya ada, supaya program tidak crash.
- Key harus immutable — list tidak bisa jadi key, tapi tuple bisa (seperti dibahas di lab Tuples sebelumnya).

## Catatan Pribadi

Perbedaan penting dari list: dictionary **tidak diindeks secara numerik**, jadi urutan penyimpanan tidak relevan untuk pengambilan data — yang penting nama key-nya, bukan posisinya. Ini bikin dictionary jauh lebih natural untuk merepresentasikan data terstruktur (misal 1 baris data dengan banyak kolom bernama).