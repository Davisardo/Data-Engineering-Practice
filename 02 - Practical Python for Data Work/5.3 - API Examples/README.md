# 5.3 - API Examples

**Hands-on Lab: API Examples — RandomUser and Fruityvice API**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 5 - APIs and Data Collection

## Tujuan Lab Ini

- Load dan pakai RandomUser API, menggunakan library `RandomUser()`.
- Load dan pakai Fruityvice API, menggunakan library `requests`.
- Load dan pakai Open-Joke-API, menggunakan library `requests`.

## Struktur Folder

5.3 - API Examples/
└── api_examples.ipynb

## Materi yang Dipelajari

1. **Dua pendekatan konsumsi API:**
   - **Library khusus** (`randomuser`) — lebih mudah, tapi terbatas ke API tertentu saja.
   - **`requests` generik** — lebih fleksibel, bisa dipakai ke API manapun.
2. **RandomUser API** — generate data user palsu untuk testing, lewat method seperti `get_full_name()`, `get_email()`, `get_picture()`.
3. **Fruityvice API** — data nutrisi buah-buahan, response berupa **nested JSON**.
4. **`pd.json_normalize()`** — meratakan (flatten) nested JSON jadi kolom-kolom terpisah (misal `nutritions.calories`, `nutritions.fat`).
5. **Query DataFrame** — `df.loc[df["col"] == value]` untuk cari baris spesifik, `.iloc[0]['kolom']` untuk ambil 1 nilai.
6. **Official Joke API** — data lelucon random, praktik pertama `.drop(columns=[...])` untuk hapus kolom tidak perlu.

## Cara Menjalankan

Buka `api_examples.ipynb` di VS Code (Jupyter extension), jalankan tiap cell dengan `Shift+Enter`.

Dependency:

pip install randomuser requests pandas

## Cheat Sheet: Nested JSON & json_normalize untuk Data Engineering

**Kenapa krusial:** response API di dunia nyata **hampir selalu nested** (objek di dalam objek) — data mentah dari API jarang langsung berbentuk tabel rapi. `pd.json_normalize()` adalah tool utama untuk mengubah struktur bertingkat itu jadi DataFrame siap analisis.

**Contoh masalah nested JSON:**
```python
# Data mentah dari API (nested)
{"name": "Persimmon", "nutritions": {"calories": 81, "fat": 0.0}}

# pd.DataFrame(results) -> kolom 'nutritions' tetap berupa dict, TIDAK berguna untuk analisis
# pd.json_normalize(results) -> otomatis pecah jadi 'nutritions.calories', 'nutritions.fat'
```

**Pola query data spesifik — dipakai berulang di lab ini:**
```python
row = df.loc[df["name"] == 'Cherry']   # filter baris berdasarkan kondisi
value = row.iloc[0]['family']            # ambil 1 nilai spesifik dari hasil filter
```
Ini pola umum untuk **lookup** — cari 1 baris spesifik dari data besar berdasarkan kriteria tertentu, lalu ambil informasi yang dibutuhkan.

**`.drop(columns=[...])` — praktik pertama di course ini:**
```python
df.drop(columns=["type", "id"], inplace=True)
```
`inplace=True` mengubah DataFrame **langsung** tanpa perlu re-assign ke variabel baru. Kolom `type`/`id` di contoh joke API dihapus karena tidak relevan untuk analisis konten lelucon.

## Catatan Pribadi

Lab ini pengalaman nyata pertama: data dari API publik seperti Fruityvice sering datang dalam struktur nested yang tidak langsung bisa dipakai — `json_normalize()` jadi langkah wajib sebelum data API siap diproses lebih lanjut, sama pentingnya dengan `read_csv()` untuk file tabular biasa.