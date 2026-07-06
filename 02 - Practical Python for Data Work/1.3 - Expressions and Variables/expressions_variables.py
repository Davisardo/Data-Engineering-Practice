# Expressions - operasi aritmatika dasar
print(43 + 60 + 16 + 41)   # penjumlahan
print(50 - 60)              # pengurangan
print(5 * 5)                 # perkalian
print(25 / 5)                # pembagian (hasil float)
print(25 / 6)
print(25 // 5)               # pembagian bulat (integer division)
print(25 // 6)

# Berapa jam dalam 160 menit
print(160 // 60)

# Urutan operasi matematika
print(30 + 2 * 60)           # perkalian dulu, baru tambah
print((30 + 2) * 60)         # tanda kurung diproses lebih dulu

# Variabel
x = 43 + 60 + 16 + 41
print(x)

y = x / 60
print(y)

x = x / 60                   # menimpa nilai x sebelumnya
print(x)

# Penamaan variabel yang bermakna
total_min = 43 + 42 + 57     # total durasi album dalam menit
print(total_min)

total_hours = total_min / 60  # total durasi dalam jam
print(total_hours)

total_hours = (43 + 42 + 57) / 60  # dihitung sekaligus dalam 1 ekspresi
print(total_hours)

# --- Exercise: Expressions ---
print(30 + 20 - 40)          # hasil: 10
print((55 - 5) / 10)         # hasil: 5.0
print((6 * 10) / 12)         # hasil: 5.0

# --- Exercise: Variables ---
x = 3 + 2 * 2
print(x)                     # hasil: 7

y = (3 + 2) * 2
print(y)                     # hasil: 10

z = x + y
print(z)                     # hasil: 17
