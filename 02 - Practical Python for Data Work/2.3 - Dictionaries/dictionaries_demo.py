# ===== 1. Membuat Dictionary =====
# key bisa string, tuple (harus immutable), value bisa apa saja termasuk list/tuple
Dict = {
    "key1": 1,
    "key2": "2",
    "key3": [3, 3, 3],
    "key4": (4, 4, 4),
    "key5": 5,
    (0, 1): 6,
}
print(Dict)

print(Dict["key1"])  # akses value lewat key string
print(Dict[(0, 1)])  # akses value lewat key tuple

# ===== 2. Dictionary yang lebih realistis =====
release_year_dict = {
    "Thriller": "1982",
    "Back in Black": "1980",
    "The Dark Side of the Moon": "1973",
    "The Bodyguard": "1992",
    "Bat Out of Hell": "1977",
    "Their Greatest Hits (1971-1975)": "1976",
    "Saturday Night Fever": "1977",
    "Rumours": "1977",
}
print(release_year_dict)

# ===== 3. Ambil value lewat key =====
print(release_year_dict["Thriller"])
print(release_year_dict["The Bodyguard"])

# ===== 4. keys() dan values() =====
print(release_year_dict.keys())
print(release_year_dict.values())

# ===== 5. Tambah entry baru =====
release_year_dict["Graduation"] = "2007"
print(release_year_dict)

# ===== 6. Hapus entry =====
del release_year_dict["Thriller"]
del release_year_dict["Graduation"]
print(release_year_dict)

# ===== 7. Cek keberadaan key =====
print("The Bodyguard" in release_year_dict)  # True
print("Thriller" in release_year_dict)  # False, sudah dihapus


# ===== 8. Quiz: Dictionaries =====
soundtrack_dic = {"The Bodyguard": "1992", "Saturday Night Fever": "1977"}
print(soundtrack_dic.keys())
print(soundtrack_dic.values())

album_sales_dict = {"The Bodyguard": 50, "Back in Black": 50, "Thriller": 65}
print(album_sales_dict["Thriller"])
print(album_sales_dict.keys())
print(album_sales_dict.values())

# ===== 9. Scenario: Inventory Toko =====
inventory = {}  # Task 1: dictionary kosong

# Task 2: detail produk 1
ProductNo1 = "Mobile Phone"
ProductNo1_quantity = 5
ProductNo1_price = 20000
ProductNo1_releaseYear = 2020

# Task 3: masukkan produk 1 ke inventory
inventory["ProductNo1"] = ProductNo1
inventory["ProductNo1_quantity"] = ProductNo1_quantity
inventory["ProductNo1_price"] = ProductNo1_price
inventory["ProductNo1_releaseYear"] = ProductNo1_releaseYear

# Task 4: detail produk 2
ProductNo2 = "Laptop"
ProductNo2_quantity = 10
ProductNo2_price = 50000
ProductNo2_releaseYear = 2023

# Task 5: masukkan produk 2 ke inventory
inventory["ProductNo2"] = ProductNo2
inventory["ProductNo2_quantity"] = ProductNo2_quantity
inventory["ProductNo2_price"] = ProductNo2_price
inventory["ProductNo2_releaseYear"] = ProductNo2_releaseYear

# Task 6: tampilkan seluruh inventory
print(inventory)

# Task 7: cek keberadaan release year
print("ProductNo1_releaseYear" in inventory)
print("ProductNo2_releaseYear" in inventory)

# Task 8: hapus release year (tidak dibutuhkan)
del inventory["ProductNo1_releaseYear"]
del inventory["ProductNo2_releaseYear"]
print(inventory)
