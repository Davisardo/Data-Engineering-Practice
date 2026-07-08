# 3.5 - Classes and Objects

**Lab: Classes and Objects in Python**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 3 - Python Programming Fundamentals

## Tujuan Lab Ini

- Bekerja dengan class dan object.
- Memahami konsep dasar Object-Oriented Programming (OOP).

## Struktur Folder

3.5 - Classes and Objects/
├── classes_demo.py
├── red_circle.png
├── blue_circle.png
├── skinny_blue_rectangle.png
└── fat_yellow_rectangle.png

## Materi yang Dipelajari

1. **Class** — blueprint/cetakan untuk membuat object, ditulis dengan `class NamaClass(object):`.
2. **Constructor (`__init__`)** — method khusus yang jalan otomatis saat object dibuat, untuk inisialisasi atribut.
3. **`self`** — merepresentasikan object itu sendiri, dipakai untuk akses atribut/method di dalam class.
4. **Instance & Attribute** — object nyata yang dibuat dari class (`RedCircle = Circle(10, 'red')`), tiap instance punya nilai atribut sendiri-sendiri.
5. **Method** — fungsi di dalam class yang bisa mengubah/berinteraksi dengan object (`add_radius()`, `draw_circle()`).
6. **`dir(object)`** — melihat semua method/atribut yang tersedia di suatu object.
7. **Class Attribute vs Instance Attribute** — class attribute (di luar `__init__`, misal `color = "white"`) sama untuk semua object; instance attribute (di dalam `__init__` via `self`) beda tiap object.

## Cara Menjalankan

pip install matplotlib
python classes_demo.py

Catatan: kode di file ini pakai `plt.savefig()` (bukan `plt.show()`) supaya visualisasi tersimpan sebagai file gambar — lebih cocok untuk dijalankan sebagai script `.py`, bukan notebook interaktif.

## Cheat Sheet: Class untuk Data Engineering

**Kenapa penting:** OOP adalah fondasi di balik hampir semua library yang sudah/akan dipakai — `pd.DataFrame` adalah class, `requests.Session()` mengembalikan object, koneksi database (`sqlite3.connect()`) juga object dengan method-methodnya sendiri. Paham class = paham cara kerja tools itu di balik layar.

**Kapan bikin class sendiri di data engineering:**
- Merepresentasikan **entitas dunia nyata yang berulang** dengan struktur konsisten — misal `class Customer`, `class Order`, `class DatabaseConnection` — daripada terus-menerus pakai dict/list lepas.
- Membungkus **logic + data terkait** jadi satu unit, misal class `ETLPipeline` yang punya method `extract()`, `transform()`, `load()` sekaligus menyimpan state (URL sumber, nama tabel, dst) sebagai atribut.

**Contoh sederhana relevan ke ETL:**
```python
class DataSource:
    def __init__(self, name, url, format='csv'):
        self.name = name
        self.url = url
        self.format = format
        self.records_loaded = 0

    def load(self, df):
        self.records_loaded = len(df)
        print(f"{self.name}: loaded {self.records_loaded} records")

source1 = DataSource("Bank Data", "https://...", "csv")
source2 = DataSource("GDP Data", "https://...", "json")
```
Dibanding pakai variabel/dict terpisah untuk tiap sumber data, class ini mengelompokkan data & perilaku terkait jadi satu, dan mudah di-scale kalau sumber data bertambah banyak.

## Catatan Pribadi

Bagian scenario Vehicle jadi contoh bagus perbedaan **class attribute** vs **instance attribute** — `color = "white"` didefinisikan sekali di level class dan otomatis berlaku untuk semua object (`vehicle1` dan `vehicle2` sama-sama warna putih), sementara `max_speed` dan `mileage` unik per object karena didefinisikan lewat `self` di dalam `__init__`.