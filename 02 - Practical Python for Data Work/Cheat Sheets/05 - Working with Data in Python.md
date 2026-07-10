# Cheat Sheet: Working with Data in Python

Referensi cepat File I/O, Pandas, dan NumPy. Pelengkap dari lab [4.1](../4.1%20-%20Reading%20Files/README.md), [4.2](../4.2%20-%20Write%20and%20Save%20Files/README.md), [4.3](../4.3%20-%20Selecting%20Data%20in%20a%20DataFrame/README.md), [4.4](../4.4%20-%20Loading%20Data%20with%20Pandas/README.md), [4.5](../4.5%20-%201D%20Numpy/README.md), dan [4.6](../4.6%20-%202D%20Numpy/README.md).

## File I/O

**Mode buka file:** `r` (read), `w` (write), `a` (append), `+` (update), `b` (binary)

```python
with open("data.txt", "r") as file:
    content = file.read()

with open("output.txt", "w") as file:
    file.write("Hello, world!")

with open("log.txt", "a") as file:
    file.write("Log entry: Something happened.")
```

**Method membaca file:**
```python
file.readlines()   # semua baris jadi list
file.readline()    # 1 baris berikutnya
file.read()        # seluruh isi jadi 1 string
```

**Method menulis file:**
```python
file.write(content)          # tulis 1 string
file.writelines(list_of_str)  # tulis banyak string sekaligus
```

**Iterasi tiap baris:**
```python
with open("data.txt", "r") as file:
    for line in file:
        print(line)
```

---

## Pandas

**Import**
```python
import pandas as pd
```

**Baca & Simpan Data**
```python
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")
df.to_csv("output.csv", index=False)
```

**Akses Kolom**
```python
df["age"]                  # 1 kolom -> Series
df[["name", "age"]]        # banyak kolom -> DataFrame
```

**Lihat DataFrame**
```python
df.head(5)      # 5 baris pertama
df.tail(5)      # 5 baris terakhir
df.info()       # tipe data & memory usage
df.describe()   # statistik ringkasan kolom numerik
```

**drop() — Hapus Kolom/Baris (BELUM dipraktikkan di lab)**
```python
df.drop(["age", "salary"], axis=1, inplace=True)   # hapus kolom
df.drop(index=[5, 10], axis=0, inplace=True)         # hapus baris
```

**dropna() — Hapus Baris dengan Nilai Kosong (BELUM dipraktikkan)**
```python
df.dropna(axis=0, inplace=True)
```

**duplicated() — Deteksi Data Duplikat (BELUM dipraktikkan)**
```python
duplicate_rows = df[df.duplicated()]
```

**Filter Baris Berdasarkan Kondisi (BELUM dipraktikkan)**
```python
filtered_df = df[(df["age"] > 30) & (df["salary"] < 50000)]
```

**groupby() — Agregasi per Kelompok (BELUM dipraktikkan)**
```python
grouped = df.groupby(["category", "region"]).agg({"sales": "sum"})
```

**merge() — Gabungkan 2 DataFrame (BELUM dipraktikkan, mirip JOIN SQL)**
```python
merged_df = pd.merge(sales, products, on=["product_id", "category_id"])
```

**replace() — Ganti Nilai Tertentu (BELUM dipraktikkan)**
```python
df["status"].replace("In Progress", "Active", inplace=True)
```

---

## NumPy

**Import**
```python
import numpy as np
```

**Buat Array**
```python
array_1d = np.array([1, 2, 3])
array_2d = np.array([[1, 2], [3, 4]])
```

**Attribute & Statistik**
```python
np.mean(array)
np.sum(array)
np.min(array)
np.max(array)
np.dot(array_1, array_2)
```

---

## Method Baru yang Belum Dipraktikkan — Perlu Dieksplor Lebih Lanjut

Method-method berikut disebut di cheat sheet resmi tapi belum ada lab hands-on-nya di course sejauh ini: `drop()`, `dropna()`, `duplicated()`, filter kondisi, `groupby()`, `merge()`, `replace()`. Ini semua **sangat penting** untuk data cleaning nyata — kemungkinan besar akan dipraktikkan di lab-lab ETL/data cleaning berikutnya, atau course lanjutan (data analysis).