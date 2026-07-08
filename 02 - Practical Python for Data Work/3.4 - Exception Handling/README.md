# 3.4 - Exception Handling

**Lab: Exception Handling**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 3 - Python Programming Fundamentals

## Tujuan Lab Ini

- Memahami exception.
- Menangani exception dengan try-except.

## Struktur Folder

3.4 - Exception Handling/
└── exceptions_demo.py

## Materi yang Dipelajari

1. **Apa itu exception** — error yang terjadi saat kode dijalankan, kalau tidak ditangani akan menghentikan program (`ZeroDivisionError`, `NameError`, `IndexError`, dst).
2. **try-except generik** — `except:` tanpa spesifikasi jenis error, menangkap semua jenis exception.
3. **try-except spesifik** — `except ZeroDivisionError:`, `except ValueError:`, dst, memberi pesan berbeda tergantung jenis error, bisa ditumpuk beberapa `except` sekaligus.
4. **else** — blok yang hanya jalan kalau **tidak ada** exception di blok `try`.
5. **finally** — blok yang **selalu** jalan, baik ada exception maupun tidak, biasa dipakai untuk cleanup (tutup koneksi, tutup file).

## Cara Menjalankan

python exceptions_demo.py

## Cheat Sheet: Exception Handling untuk Data Engineering

**Kenapa krusial:** pipeline data sering jalan tanpa pengawasan langsung (scheduled job tiap malam, misalnya). Tanpa exception handling yang baik, 1 baris data korup bisa bikin **seluruh pipeline crash**. Dengan `try/except` yang tepat, program bisa skip data bermasalah, catat errornya, dan tetap lanjut memproses data yang valid.

**Best practice — tangkap exception spesifik dulu:**
```python
try:
    value = int(row['price'])
except ValueError:
    log_progress(f"Baris invalid, price bukan angka: {row}")
    continue   # skip baris ini, lanjut ke baris berikutnya
except KeyError:
    log_progress(f"Kolom 'price' tidak ditemukan di baris: {row}")
    continue
```
Kenapa penting: `except:` polos menangkap **semua** error, termasuk bug yang seharusnya kamu tahu (misal typo nama variabel) — ini bisa menyembunyikan bug asli. Selalu tangkap error spesifik dulu, baru pakai `except:` generik sebagai jaring pengaman terakhir.

**Pola `finally` untuk cleanup resource — relevan langsung ke lab-lab ETL sebelumnya:**
```python
sql_connection = sqlite3.connect(db_name)
try:
    load_to_db(df, sql_connection, table_name)
    run_query(query_statement, sql_connection)
except Exception as e:
    log_progress(f"ETL gagal: {e}")
finally:
    sql_connection.close()   # SELALU tertutup, error atau tidak
```
Di lab-lab ETL sebelumnya (2.1, 2.2), `conn.close()` ditaruh di akhir kode tanpa `try/except` — kalau ada error di tengah proses, baris `conn.close()` tidak akan pernah tereksekusi, dan koneksi database bisa "bocor" (tetap terbuka). Menaruhnya di `finally` memastikan koneksi selalu ditutup rapi.

**Exception umum yang sering ditemui saat data engineering:**

| Exception | Kapan Muncul |
|---|---|
| `ValueError` | Konversi tipe data gagal (misal string bukan angka ke `int()`) |
| `KeyError` | Akses key dictionary/kolom yang tidak ada |
| `FileNotFoundError` | Baca file yang tidak ada di path yang ditentukan |
| `ConnectionError` | Gagal koneksi ke API/database (server down, timeout) |
| `IndexError` | Akses index list yang di luar batas |

## Catatan Pribadi

Exercise 3 (`complex_calculation`) menunjukkan pola `except Exception as e:` yang generik tapi tetap informatif — menangkap semua jenis error sambil menyimpan detail errornya di variabel `e`, kompromi bagus antara "program tidak crash" dan "tetap ada info untuk debugging" (bisa di-log pakai `log_progress(str(e))` di project nyata).


## Reading: Errors vs Exceptions & Exception Lainnya

Materi reading tambahan dari course, melengkapi pemahaman konseptual dan memperkenalkan beberapa exception baru yang belum dipraktikkan di atas.

### Errors vs Exceptions
Dua istilah ini sering disamakan padahal beda:

| Aspek | Error | Exception |
|---|---|---|
| Asal | Lingkungan, hardware, atau sistem operasi | Hasil dari eksekusi kode bermasalah |
| Sifat | Parah, biasanya bikin program crash total | Kurang parah, bisa ditangani agar program tetap jalan |
| Penanganan | Biasanya **tidak** bisa ditangkap/ditangani program | Bisa ditangkap pakai `try-except`, program tetap lanjut |
| Contoh | `SyntaxError`, `NameError` | `ZeroDivisionError`, `FileNotFoundError` |
| Kategori | Tidak dikategorikan | Dikelompokkan jadi class (`ArithmeticError`, `IOError`, `ValueError`, dst) |

### Exception Tambahan yang Sering Ditemui

**`FileNotFoundError`** — akses file yang tidak ada.
```python
with open("nonexistent_file.txt", "r") as file:
    content = file.read()   # Raises FileNotFoundError
```

**`KeyError`** — akses key dictionary yang tidak ada. Bisa dihindari pakai `.get()`.
```python
my_dict = {"name": "Alice", "age": 30}
value = my_dict.get("city")     # aman, hasil None kalau tidak ada
missing = my_dict["city"]       # Raises KeyError
```

**`TypeError`** — operasi antar tipe data yang tidak kompatibel.
```python
result = "hello" + 5   # Raises TypeError, string + int tidak valid
```

**`AttributeError`** — akses method/atribut yang tidak dimiliki suatu objek.
```python
text = "example"
missing = text.some_method()   # Raises AttributeError
```

**`ImportError`** — mengimpor modul yang tidak tersedia/tidak terinstall.
```python
import non_existent_module   # Raises ImportError
```

**Relevansi ke data engineering:** `KeyError` dan `TypeError` adalah dua exception **paling sering muncul** saat parsing data JSON/API yang strukturnya tidak konsisten (kolom kadang ada kadang tidak) — memahami keduanya penting sebelum masuk ke topik "Working with Data" dan "APIs" di module berikutnya.

