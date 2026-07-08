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

## Reading: Struktur Class & Real-World Example (Car)

Materi reading tambahan dari course, merangkum struktur class secara sistematis dan memberi contoh nyata lengkap dengan method business logic (bukan cuma method gambar).

### Anatomi Lengkap Sebuah Class

```python
class ClassName:
    # Class attribute (dibagi oleh SEMUA instance)
    class_attribute = value

    # Constructor - inisialisasi instance attribute
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    # Instance method - beroperasi pada data instance
    def method1(self, parameter1):
        pass
```

### Dua Cara Memanggil Method
```python
# Cara 1: dot notation langsung
result1 = object1.method1(param_value)

# Cara 2: assign method ke variabel dulu, baru panggil
method_reference = object1.method1
result2 = method_reference(param_value)
```

### Akses & Modifikasi Atribut
```python
attribute_value = object1.attribute1     # baca atribut
object1.attribute2 = new_value            # ubah atribut
class_attr_value = ClassName.class_attribute   # akses class attribute langsung dari class (tanpa perlu object)
```

### Real-World Example: Car Class
Contoh dengan business logic nyata (bukan cuma penyimpanan data) — method `accelerate()` punya validasi (tidak boleh melebihi `max_speed`), lebih representatif dibanding contoh Circle/Rectangle yang cuma soal drawing.

```python
class Car:
    max_speed = 120  # class attribute

    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self, acceleration):
        if self.speed + acceleration <= self.max_speed:
            self.speed += acceleration
        else:
            self.speed = self.max_speed   # dibatasi max_speed

    def get_speed(self):
        return self.speed


car1 = Car("Toyota", "Camry", "Blue")
car1.accelerate(30)
print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
```

**Relevansi ke data engineering:** pola validasi di `accelerate()` (`if kondisi: ... else: batasi nilai`) ini sama persis dengan pola **data validation** — misal fungsi yang membatasi nilai kolom tertentu supaya tidak melebihi batas wajar (data quality check), bukan cuma menyimpan nilai apa adanya.