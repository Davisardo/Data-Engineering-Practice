# 3.3 - Functions

**Lab: Functions in Python**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 3 - Python Programming Fundamentals

## Tujuan Lab Ini

- Memahami konsep dasar fungsi, variabel, dan cara menggunakan fungsi di Python.

## Struktur Folder

3.3 - Functions/
└── functions_demo.py

## Materi yang Dipelajari

1. **Fungsi dasar** — `def nama_fungsi(parameter):`, kode setelah `return` tidak pernah dieksekusi.
2. **Local vs Global variable** — variabel di dalam fungsi hanya bisa diakses di dalam fungsi itu, kecuali dideklarasi `global`.
3. **Return None** — fungsi tanpa `return` eksplisit otomatis mengembalikan `None`.
4. **Fungsi bawaan (built-in)** — `sum()`, `len()`, `max()`, `min()`, umumnya butuh iterable (list/tuple), bukan angka lepas.
5. **If/else dan loop di dalam fungsi** — fungsi bisa mengandung logic kompleks, bukan cuma satu baris.
6. **Default argument** — `def func(param=nilai_default):`, bisa dipanggil tanpa isi parameter itu.
7. **Scope** — variabel lokal dengan nama sama seperti variabel global **tidak** saling menimpa (lokal selalu diprioritaskan di dalam fungsinya sendiri).
8. **`*args`** — jumlah argumen tidak pasti, dibungkus sebagai tuple.
9. **`**kwargs`** — jumlah keyword argument tidak pasti, dibungkus sebagai dictionary.
10. **Mutable reference** — list yang di-passing ke fungsi lalu dimodifikasi di dalamnya, perubahan ikut terjadi ke list asli di luar fungsi (passing by reference).

## Cara Menjalankan

python functions_demo.py

## Cheat Sheet: Function untuk Data Engineering

**Kenapa krusial:** semua pipeline ETL yang sudah dikerjakan sejauh ini (`extract()`, `transform()`, `load_to_csv()`, dst) adalah fungsi. Prinsip **DRY (Don't Repeat Yourself)** — kalau kode yang sama ditulis berkali-kali, itu sinyal kuat untuk dijadikan fungsi.

**Manfaat fungsi (dari reading tambahan):**
- **Modularity** — pecah tugas kompleks jadi komponen kecil yang mudah dikelola.
- **Reusability** — pakai berkali-kali tanpa tulis ulang kode.
- **Readability** — nama fungsi yang jelas bikin kode lebih mudah dipahami.
- **Debugging** — mengisolasi fungsi memudahkan pelacakan bug.
- **Maintenance** — perubahan di satu fungsi otomatis berlaku di semua tempat fungsi itu dipanggil.

**Perangkap paling sering:**

| Kasus | Bahaya | Solusi |
|---|---|---|
| Lupa `return` | Fungsi diam-diam kembalikan `None`, error `NoneType` di kode berikutnya | Selalu cek fungsi punya `return` kalau memang butuh hasilnya |
| Pakai `global` sembarangan | Fungsi punya "efek samping" tersembunyi, susah dilacak bug-nya | Sebisa mungkin fungsi hanya bergantung pada parameter, hasil lewat `return` |
| List di-passing ke fungsi lalu diubah | List asli di luar fungsi ikut berubah tanpa disadari | Clone dulu (`list[:]`) di dalam fungsi kalau tidak mau efek samping |

**Pola default argument yang sering dipakai di ETL:**
```python
def extract(url, timeout=30, retries=3):
    ...
```
Bisa dipanggil `extract(my_url)` (pakai default) atau `extract(my_url, timeout=60)` (override sesuai kebutuhan) — pola ini banyak dipakai library populer seperti `requests` dan Pandas.

**`*args`/`**kwargs` di dunia nyata:** banyak dipakai di fungsi logging generik atau fungsi konfigurasi yang menerima jumlah parameter tidak pasti — pola yang sama dipakai di banyak library besar (Pandas, requests, dst).

## Catatan Pribadi

Bagian paling penting untuk diingat: passing list/dict ke fungsi itu **passing by reference** (mutable), beda dari passing angka/string yang aman (immutable). Ini konsep yang sama persis dengan "copy vs clone" yang sudah dibahas di lab List sebelumnya — kalau lupa, bisa jadi sumber bug tersembunyi di pipeline data yang kompleks.

## Reading: Exploring Python Functions

Materi reading tambahan dari course, melengkapi praktik di atas dengan penjelasan konseptual dan contoh baru.

### Anatomi Fungsi: Input → Proses → Output
Fungsi bekerja seperti fungsi matematika: menerima input (parameter), menjalankan proses, mengembalikan output.
```python
def calculate_total(a, b):  # Input: a dan b
    total = a + b            # Proses: penjumlahan
    return total              # Output: hasil penjumlahan

result = calculate_total(5, 7)
print(result)  # 12
```

### Statement `pass`
Placeholder saat fungsi/blok kode didefinisikan tapi belum diisi logic-nya — tetap valid secara syntax meski belum melakukan apa-apa.
```python
def function_name():
    pass
```
Berguna saat merancang struktur kode dulu (misal kerangka semua fungsi ETL), baru diisi implementasinya belakangan — persis pola yang dipakai saat bikin skeleton kode di lab-lab ETL sebelumnya.

### Docstring
Dokumentasi fungsi ditulis di baris pertama dalam triple quotes, membantu developer lain (atau diri sendiri di masa depan) paham fungsi tanpa baca detail kodenya.
```python
def multiply(a, b):
    """
    This function multiplies two numbers.
    Input: a (number), b (number)
    Output: Product of a and b
    """
    print(a * b)
```

### Modifikasi Data Structure Lewat Fungsi
Contoh lengkap fungsi `add_element()` dan `remove_element()` untuk mengelola list — mendemonstrasikan mutable reference dalam konteks nyata (menambah/menghapus data, bukan sekadar contoh teoretis).
```python
my_list = []

def add_element(data_structure, element):
    data_structure.append(element)

def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")

add_element(my_list, 42)
add_element(my_list, 17)
add_element(my_list, 99)
print("Current list:", my_list)   # [42, 17, 99]

remove_element(my_list, 17)
remove_element(my_list, 55)        # tidak ada di list -> print pesan
print("Updated list:", my_list)   # [42, 99]
```

**Relevansi ke data engineering:** pola `add_element()`/`remove_element()` ini bentuk sederhana dari fungsi CRUD (Create, Read, Update, Delete) yang jadi dasar operasi database — di skala lebih besar, ini menjadi fungsi `insert_row()`, `delete_row()`, dst pada pipeline data.