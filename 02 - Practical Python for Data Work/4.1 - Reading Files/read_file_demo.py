# ===== 1. Buka file dengan open() =====
example1 = "example1.txt"
file1 = open(example1, "r")

print("Nama file:", file1.name)
print("Mode:", file1.mode)

file_content = file1.read()
print(file_content)
print("Tipe data:", type(file_content))

file1.close()   # WAJIB ditutup manual kalau pakai open() biasa

# ===== 2. Cara yang lebih baik: pakai 'with' =====
with open(example1, "r") as file1:
    file_content = file1.read()
    print(file_content)

# file otomatis tertutup setelah blok 'with' selesai
print("File sudah tertutup?", file1.closed)

# ===== 3. Baca sebagian karakter =====
with open(example1, "r") as file1:
    print(file1.read(4))   # 4 karakter pertama

# ===== 4. Baca berkali-kali, posisi lanjut dari terakhir =====
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

# ===== 5. Pola serupa dengan jumlah karakter beda =====
with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))

# ===== 6. readline() - baca 1 baris =====
with open(example1, "r") as file1:
    print("first line: " + file1.readline())

# ===== 7. readline() dengan batas karakter =====
with open(example1, "r") as file1:
    print(file1.readline(20))   # tidak akan lewat batas baris
    print(file1.read(20))        # lanjut baca 20 karakter berikutnya

# ===== 8. Loop iterasi tiap baris =====
with open(example1, "r") as file1:
    i = 0
    for line in file1:
        print("Iteration", str(i), ": ", line)
        i = i + 1

# ===== 9. readlines() - simpan semua baris jadi list =====
with open(example1, "r") as file1:
    file_as_list = file1.readlines()

print(file_as_list[0])   # baris pertama
print(file_as_list[1])   # baris kedua
print(file_as_list[2])   # baris ketiga