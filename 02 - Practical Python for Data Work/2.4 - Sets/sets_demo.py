# ===== 1. Membuat Set =====
# set otomatis membuang duplikat & tidak punya urutan tetap
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)

# ===== 2. Konversi list ke set =====
album_list = [
    "Michael Jackson",
    "Thriller",
    1982,
    "00:42:19",
    "Pop, Rock, R&B",
    46.0,
    65,
    "30-Nov-82",
    None,
    10.0,
]
album_set = set(album_list)
print(album_set)

music_genres = set(
    [
        "pop",
        "pop",
        "rock",
        "folk rock",
        "hard rock",
        "soul",
        "progressive rock",
        "soft rock",
        "R&B",
        "disco",
    ]
)
print(music_genres)


# ===== 3. Membuat & Modifikasi Set =====
A = set(["Thriller", "Back in Black", "AC/DC"])
print(A)

A.add("NSYNC")            # tambah elemen
print(A)

A.add("NSYNC")            # tambah elemen sama lagi -> tidak berpengaruh
print(A)

A.remove("NSYNC")         # hapus elemen
print(A)

print("AC/DC" in A)       # cek keberadaan elemen

# ===== 4. Set Logic Operations =====
album_set1 = set(["Thriller", "AC/DC", "Back in Black"])
album_set2 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])

print(album_set1)
print(album_set2)

# Intersection: elemen yang ada di KEDUA set (mirip INNER JOIN)
print(album_set1 & album_set2)
print(album_set1.intersection(album_set2))

# Difference: elemen yang HANYA ada di 1 set (mirip LEFT JOIN ... WHERE kanan NULL)
print(album_set1.difference(album_set2))   # hanya di set1
print(album_set2.difference(album_set1))   # hanya di set2

# Union: gabungan semua elemen dari kedua set (tanpa duplikat)
print(album_set1.union(album_set2))

# Subset & Superset
print(set(album_set1).issuperset(album_set2))   # apakah set1 mencakup semua set2?
print(set(album_set2).issubset(album_set1))     # apakah set2 bagian dari set1?

print({"Back in Black", "AC/DC"}.issubset(album_set1))     # True
print(album_set1.issuperset({"Back in Black", "AC/DC"}))   # True

# ===== 5. Quiz: Sets =====
print(set(['rap', 'house', 'electronic music', 'rap']))   # duplikat 'rap' hilang

A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print("the sum of A is:", sum(A))   # 6 (list, semua elemen dihitung)
print("the sum of B is:", sum(B))   # 3 (set, duplikat sudah hilang)

album_set1 = set(["Thriller", "AC/DC", "Back in Black"])
album_set2 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])

album_set3 = album_set1.union(album_set2)
print(album_set3)

print(album_set1.issubset(album_set3))   # True, semua isi set1 pasti ada di union-nya