import numpy as np                      # library untuk operasi array/matriks

a = np.array([2, 3, 4])                 # array pertama
b = np.array([3, 2, 1])                 # array kedua
c = a + b                               # jumlahkan tiap elemen -> [5, 5, 5]
print(c)                                # tampilkan hasil

# Practice: ganti 'a' jadi [5, 3, 1] lalu jalankan ulang -> hasil [8, 5, 2]
# a = np.array([5, 3, 1])