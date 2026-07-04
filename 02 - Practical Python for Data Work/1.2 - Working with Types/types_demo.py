# Tipe data dasar
print(type(12))  # int
print(type(2.14))  # float
print(type("Hello, Python 101!"))  # str
print(type(12.0))  # float

# Integer bisa negatif atau positif
print(type(-1))
print(type(4))
print(type(0))

# Float
print(type(1.0))  # 1 int, 1.0 float
print(type(0.5))
print(type(0.56))

# Info sistem soal float
import sys

print(sys.float_info)

# Konversi tipe data (typecasting)
print(float(2))  # int ke float
print(type(float(2)))
print(int(1.1))  # float ke int, kehilangan desimal (hasil: 1)

print(int("1"))  # string ke int
# int('1 or 2 people')       # akan error, string tidak murni angka

print(float("1.2"))  # string ke float

print(str(1))  # int ke string
print(str(1.2))  # float ke string

# Boolean
print(True)
print(False)
print(type(True))
print(type(False))

print(int(True))  # True -> 1
print(bool(1))  # 1 -> True
print(bool(0))  # 0 -> False
print(float(True))  # True -> 1.0


# --- Exercise: Types ---

# Tipe hasil dari 6 / 2
print(type(6 / 2))  # float

# Tipe hasil dari 6 // 2 (pembagian bulat)
print(type(6 // 2))  # int

# Tipe hasil dari string
print(type("Hello, World!"))  # str

# Tipe hasil dari perbandingan
print(type("hello" == "world"))  # bool

# Konversi employee id "1001" ke integer
print(int("1001"))

# Konversi nilai finansial "1234.56" ke float
print(float("1234.56"))

# Konversi nomor telepon jadi string (sudah string dari awal)
print(str("123-456-7890"))
