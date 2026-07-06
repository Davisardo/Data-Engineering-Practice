# Cheat Sheet: Lists and Tuples

Referensi cepat method-method List & Tuple di Python. Pelengkap dari lab [2.1 - Lists](../2.1%20-%20Lists/README.md) dan [2.2 - Tuples](../2.2%20-%20Tuples/README.md).

## List

### Membuat List
List adalah tipe data terurut dan **mutable** (bisa diubah), ditulis dengan kurung siku `[]`.
```python
fruits = ["apple", "banana", "orange", "mango"]
```

### Indexing
```python
my_list = [10, 20, 30, 40, 50]
print(my_list[0])   # 10
print(my_list[-1])  # 50
```

### Slicing
```python
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # [2, 3, 4]
print(my_list[:3])   # [1, 2, 3]
print(my_list[2:])   # [3, 4, 5]
```

### Mengubah Elemen
```python
my_list = [10, 20, 30, 40, 50]
my_list[1] = 25
print(my_list)  # [10, 25, 30, 40, 50]
```

### `append()` — tambah 1 elemen di akhir
```python
fruits.append("mango")
```

### `extend()` — tambah banyak elemen (flat, dari iterable lain)
```python
fruits.extend(["mango", "grape"])
```

### `insert()` — sisipkan elemen di posisi tertentu
```python
my_list.insert(2, 6)  # sisipkan 6 di index 2
```

### `pop()` — hapus & kembalikan elemen (default: elemen terakhir)
```python
removed = my_list.pop(2)   # hapus & ambil elemen index 2
removed = my_list.pop()    # hapus & ambil elemen terakhir
```

### `remove()` — hapus elemen berdasarkan nilai (kemunculan pertama)
```python
my_list.remove(30)
```

### `del` — hapus elemen berdasarkan index
```python
del my_list[2]
```

### `sort()` — urutkan in-place (mengubah list asli)
```python
my_list.sort()               # ascending
my_list.sort(reverse=True)   # descending
```

### `reverse()` — balik urutan elemen
```python
my_list.reverse()
```

### `copy()` — shallow copy (independen dari list asli)
```python
new_list = my_list.copy()
```

### `count()` — hitung kemunculan elemen tertentu
```python
my_list.count(2)
```

---

## Tuple

Tuple mirip list, tapi **immutable** (tidak bisa diubah setelah dibuat). Ditulis dengan kurung `()`.

### `count()` — hitung kemunculan nilai tertentu
```python
fruits = ("apple", "banana", "apple", "orange")
fruits.count("apple")   # 2
```

### `index()` — cari posisi kemunculan pertama suatu nilai
```python
fruits.index("apple")   # 0 (raise ValueError kalau tidak ketemu)
```

### `sum()` — total semua elemen numerik
```python
numbers = (10, 20, 5, 30)
sum(numbers)   # 65
```

### `min()` / `max()` — nilai terkecil/terbesar
```python
min(numbers)   # 5
max(numbers)   # 30
```

### `len()` — jumlah elemen
```python
len(fruits)   # 3
```

---

## Kapan Pakai yang Mana? (Ringkas)

| Kebutuhan | List | Tuple |
|---|---|---|
| Data akan diubah/ditambah/dihapus | ✅ | ❌ |
| Data harus tetap (fixed) sepanjang program | ❌ | ✅ |
| Jadi key dictionary / elemen set | ❌ (unhashable) | ✅ |
| Method modifikasi (`append`, `sort`, dst) | ✅ | ❌ (tidak ada) |
| Method baca-saja (`count`, `index`, `len`) | ✅ | ✅ |