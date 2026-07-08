# Cheat Sheet: Dictionaries and Sets

Referensi cepat method-method Dictionary & Set di Python. Pelengkap dari lab [2.3 - Dictionaries](../2.3%20-%20Dictionaries/README.md) dan [2.4 - Sets](../2.4%20-%20Sets/README.md).

## Dictionary

### Membuat Dictionary
```python
dict_name = {}   # dictionary kosong
person = {"name": "John", "age": 30, "city": "New York"}
```

### Akses Value
```python
name = person["name"]
age = person["age"]
```

### Tambah / Modifikasi
Assign ke key baru → entry baru dibuat. Assign ke key yang sudah ada → value ditimpa.
```python
person["Country"] = "USA"   # entry baru
person["city"] = "Chicago"  # timpa value lama
```

### `del` — hapus entry
Raise `KeyError` kalau key tidak ada.
```python
del person["Country"]
```

### Cek Keberadaan Key
```python
if "name" in person:
    print("Name exists in the dictionary.")
```

### `keys()`
```python
person_keys = list(person.keys())
```

### `values()`
```python
person_values = list(person.values())
```

### `items()` — pasangan key-value sebagai list of tuple
Berguna untuk iterasi `for key, value in dict.items():`
```python
info = list(person.items())
```

---

## Set

### Definisi Set
Koleksi unik & tidak terurut (posisi elemen tidak tetap).
```python
empty_set = set()
fruits = {"apple", "banana", "orange"}
colors = {"orange", "red", "green"}
```

### `add()` — tambah elemen
Kalau sudah ada, tidak ditambah lagi (otomatis unik).
```python
fruits.add("mango")
```

### `in` — cek keberadaan elemen
```python
"banana" in fruits
```

### `issubset()` — cek semua elemen ada di set lain
```python
fruits.issubset(colors)
```

### `issuperset()` — cek set ini mencakup semua elemen set lain
```python
colors.issuperset(fruits)
```

### `remove()` — hapus elemen
Raise `KeyError` kalau elemen tidak ada.
```python
fruits.remove("banana")
```

### Set Operations
```python
union_set = set1.union(set2)                         # gabungan semua elemen
intersection_set = set1.intersection(set2)            # elemen yang sama di keduanya
difference_set = set1.difference(set2)                 # hanya ada di set1
sym_diff_set = set1.symmetric_difference(set2)          # ada di salah satu, tapi tidak keduanya
```

**`symmetric_difference()`** ini belum dibahas di lab 2.4 — bedanya dengan `difference()`: hasilnya elemen yang **unik di salah satu set** (gabungan dari "hanya di A" + "hanya di B"), bukan cuma satu arah.
```python
fruits = {"apple", "banana", "orange"}
colors = {"orange", "red", "green"}
fruits.symmetric_difference(colors)
# {"apple", "banana", "red", "green"} -> semua KECUALI "orange" yang sama di keduanya
```
