# ===== 1. List Dasar & Indexing =====
L = ["The Bodyguard", 7.0, 1992]
print(L)

# Indexing positif & negatif menunjuk elemen yang sama
print("Positive:", L[0], "| Negative:", L[-3])
print("Positive:", L[1], "| Negative:", L[-2])
print("Positive:", L[2], "| Negative:", L[-1])

# List bisa berisi banyak tipe sekaligus, termasuk list & tuple lain (nested)
print(["The Bodyguard", 7.0, 1992, [1, 2], ("A", 1)])


# ===== 2. Slicing =====
L = ["The Bodyguard", 7.0, 1992, "BG", 1]
print(L[3:5])  # ambil index 3-4

# ===== 3. extend() vs append() =====
L = ["The Bodyguard", 7.0]
L.extend(["pop", 10])  # tambah tiap elemen secara terpisah (flat)
print("extend:", L)

L2 = ["The Bodyguard", 7.0]
L2.append(["pop", 10])  # tambah 1 elemen berupa list (nested)
print("append:", L2)

# Efeknya beda kalau ditambah berkali-kali
L = ["The Bodyguard", 7.0]
L.extend(["pop", 10])
print(L)
L.append(["a", "b"])  # ini nambah 1 elemen nested list
print(L)

# ===== 4. List bersifat mutable (bisa diubah) =====
A = ["disco", 10, 1.2]
print("Before change:", A)
A[0] = "hard rock"
print("After change:", A)

# ===== 5. Hapus elemen dengan del =====
print("Before change:", A)
del A[0]
print("After change:", A)

# ===== 6. Split string jadi list =====
print("hard rock".split())  # default pisah per spasi
print("A,B,C,D".split(","))  # pisah pakai delimiter koma


# ===== 7. Copy by Reference (bahaya!) =====
A = ["hard rock", 10, 1.2]
B = A  # B menunjuk ke objek yang SAMA dengan A, bukan copy baru
print("A:", A)
print("B:", B)

print("B[0] sebelum:", B[0])
A[0] = "banana"  # ubah A...
print("B[0] setelah:", B[0])  # ...ternyata B ikut berubah!

# ===== 8. Clone by Value (aman) =====
B = A[:]  # slicing penuh = bikin copy independen
print("B[0] sebelum:", B[0])
A[0] = "hard rock"  # ubah A lagi...
print("B[0] setelah:", B[0])  # ...B tidak ikut berubah

# ===== 9. Quiz: List =====
a_list = [1, "hello", [1, 2, 3], True]
print(a_list)
print(a_list[1])  # index 1
print(a_list[1:4])  # index 1 sampai 3

A = [1, "a"]
B = [2, 1, "d"]
print(A + B)  # concatenate 2 list

# ===== 10. Scenario: Shopping List =====
shopping_list = []  # Task 1: list kosong
shopping_list = ["Watch", "Laptop", "Shoes", "Pen", "Clothes"]  # Task 2
shopping_list.append("Football")  # Task 3
print(shopping_list[0])  # Task 4: item pertama
print(shopping_list[-1])  # Task 5: item terakhir
print(shopping_list)  # Task 6: seluruh list
print(shopping_list[1:3])  # Task 7: Laptop & Shoes
shopping_list[3] = "Notebook"  # Task 8: ganti Pen -> Notebook
del shopping_list[4]  # Task 9: hapus Clothes
print(shopping_list)  # Task 10: hasil akhir
