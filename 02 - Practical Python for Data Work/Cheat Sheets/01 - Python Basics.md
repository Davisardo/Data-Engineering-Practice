# Cheat Sheet: Python Basics

Referensi cepat dasar-dasar Python. Pelengkap dari lab [1.1](../1.1%20-%20Writing%20Your%20First%20Program/README.md), [1.2](../1.2%20-%20Working%20with%20Types/README.md), [1.3](../1.3%20-%20Expressions%20and%20Variables/README.md), dan [1.4](../1.4%20-%20String%20Operations/README.md).

## Comments
Baris teks yang diabaikan interpreter Python saat menjalankan kode.
```python
# Ini adalah komentar
```

## Data Types
- Integer, Float, Boolean, String
```python
x = 7            # Integer
y = 12.4         # Float
is_valid = True  # Boolean
F_Name = "John"  # String
```

## Variable Assignment
Memberi nilai ke variabel.
```python
name = "John"
x = 5
```

## Python Operators
| Operator | Fungsi |
|---|---|
| `+` | Penjumlahan |
| `-` | Pengurangan |
| `*` | Perkalian |
| `/` | Pembagian (hasil float) |
| `//` | Floor division (hasil integer, dibulatkan ke bawah) |
| `%` | Modulo (sisa hasil bagi) |

```python
x, y = 9, 4
result_add = x + y    # 13
result_sub = x - y    # 5
result_mul = x * y    # 36
result_div = x / y    # 2.25
result_fdiv = x // y  # 2
result_mod = x % y    # 1
```

## Concatenation
Menggabungkan string dengan `+`.
```python
result = "Hello" + " John"
```

## print()
Menampilkan pesan atau nilai variabel.
```python
print("Hello, world")
print(a + b)
```

## Indexing
Akses karakter di posisi tertentu.
```python
my_string = "Hello"
char = my_string[0]   # 'H'
```

## Slicing
Ambil sebagian string.
```python
my_string = "Hello"
substring = my_string[0:5]
```

## len()
Panjang string.
```python
length = len("Hello")   # 5
```

## upper() / lower()
Ubah ke huruf besar/kecil.
```python
"Hello".upper()   # "HELLO"
"Hello".lower()   # "hello"
```

## replace()
Ganti substring.
```python
"Hello".replace("Hello", "Hi")   # "Hi"
```

## split()
Pecah string jadi list berdasarkan delimiter.
```python
"a,b,c".split(",")   # ['a', 'b', 'c']
```

## strip()
Hapus whitespace di awal/akhir string.
```python
"  Hello  ".strip()   # "Hello"
```