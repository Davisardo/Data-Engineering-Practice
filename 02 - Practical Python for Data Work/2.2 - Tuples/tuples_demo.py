# ===== 1. Tuple Dasar =====
tuple1 = ("disco", 10, 1.2)
print(tuple1)
print(type(tuple1))  # <class 'tuple'>

# ===== 2. Indexing =====
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

# ===== 3. Negative Indexing =====
print(tuple1[-1])  # elemen terakhir
print(tuple1[-2])
print(tuple1[-3])

# ===== 4. Concatenate Tuple =====
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)

# ===== 5. Slicing =====
print(tuple2[0:3])  # index 0-2
print(tuple2[3:5])  # index 3-4

# ===== 6. Panjang tuple =====
print(len(tuple2))

# ===== 7. Sorting =====
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
RatingsSorted = sorted(Ratings)  # hasilnya LIST, bukan tuple
print(RatingsSorted)
print(type(RatingsSorted))

# ===== 8. Nested Tuple =====
NestedT = (1, 2, ("pop", "rock"), (3, 4), ("disco", (1, 2)))

print("Element 0 of Tuple:", NestedT[0])
print("Element 1 of Tuple:", NestedT[1])
print("Element 2 of Tuple:", NestedT[2])
print("Element 3 of Tuple:", NestedT[3])
print("Element 4 of Tuple:", NestedT[4])

# Akses tuple di dalam tuple (index kedua)
print("Element 2,0 of Tuple:", NestedT[2][0])
print("Element 2,1 of Tuple:", NestedT[2][1])
print("Element 3,0 of Tuple:", NestedT[3][0])
print("Element 3,1 of Tuple:", NestedT[3][1])
print("Element 4,0 of Tuple:", NestedT[4][0])
print("Element 4,1 of Tuple:", NestedT[4][1])

# Akses karakter di dalam string yang ada di nested tuple (index ketiga)
print(NestedT[2][1][0])  # karakter pertama dari "rock"
print(NestedT[2][1][1])  # karakter kedua dari "rock"
print(NestedT[4][1][0])  # elemen pertama dari (1, 2) di dalam index 4
print(NestedT[4][1][1])  # elemen kedua dari (1, 2) di dalam index 4


# ===== 9. Quiz: Tuples =====
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock",
                "R&B", "progressive rock", "disco")

print(len(genres_tuple))        # panjang tuple
print(genres_tuple[3])          # elemen index 3
print(genres_tuple[3:6])        # slicing index 3-5
print(genres_tuple[0:2])        # 2 elemen pertama

print("disco".find('s'))        # cari index 's' dalam string "disco"

C_tuple = (-5, 1, -3)
C_list = sorted(C_tuple)        # hasil sorted = list
print(C_list)