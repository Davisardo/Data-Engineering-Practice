# 4.6 - 2D Numpy

**Hands-on Lab: 2D Numpy in Python**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 4 - Working with Data in Python

## Tujuan Lab Ini

- Membuat dan mengakses array NumPy 2 dimensi (matriks).
- Melakukan operasi dasar matriks: addition, scalar multiplication, Hadamard product, dot product.
- Melakukan transpose matriks.

## Struktur Folder

4.6 - 2D Numpy/
└── numpy_2d.ipynb

## Materi yang Dipelajari

1. **Membuat matriks** — dari nested list, `np.array([[..], [..], [..]])`.
2. **Attribute** — `.ndim` (jumlah dimensi), `.shape` (baris, kolom), `.size` (total elemen).
3. **Akses elemen** — `A[baris, kolom]` atau `A[baris][kolom]`, hasilnya sama.
4. **Slicing 2D** — `A[0][0:2]` (baris pertama, kolom tertentu), `A[0:2, 2]` (beberapa baris, kolom tertentu).
5. **Matrix Addition** — `X + Y`, elemen-per-elemen posisi yang sama.
6. **Scalar Multiplication** — `2 * Y`, semua elemen dikali konstanta.
7. **Hadamard Product** — `X * Y`, perkalian elemen-per-elemen posisi yang sama (BUKAN perkalian matriks matematis).
8. **Matrix Multiplication (Dot Product)** — `np.dot(A, B)`, mengikuti aturan aljabar linear: matriks m×n hanya bisa dikalikan dengan n×p, hasil m×p.
9. **Transpose** — `.T`, menukar posisi baris jadi kolom dan sebaliknya.

## Cara Menjalankan

Buka `numpy_2d.ipynb` di VS Code (Jupyter extension), jalankan tiap cell dengan `Shift+Enter`.

## Cheat Sheet: Perbedaan Kritis — Hadamard Product vs Dot Product

**Ini perangkap paling sering bikin bug di kode matematis/ML:**

```python
X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 1], [1, 2]])

X * Y        # Hadamard product -> [[2,0],[0,2]]  (elemen posisi sama)
np.dot(X, Y) # Dot product      -> [[2,1],[1,2]]  (aturan perkalian matriks)
```

| | Hadamard (`*`) | Dot Product (`np.dot()`) |
|---|---|---|
| Syarat shape | Kedua matriks harus **sama persis** | Kolom matriks 1 = baris matriks 2 |
| Cara hitung | Elemen posisi sama dikalikan langsung | Baris × kolom, dijumlahkan |
| Kegunaan nyata | Masking, filtering elemen tertentu | Transformasi linear, perkalian matriks matematis |

**Kaitan ke ML/data engineering:** dot product matriks adalah operasi inti di balik **neural network** (setiap layer pada dasarnya perkalian matriks bobot dengan input), transformasi PCA, dan operasi aljabar linear lain yang dipakai di feature engineering skala besar.

**Transpose (`.T`) di dunia nyata:** sering dipakai saat data perlu "diputar" orientasinya — misal mengubah data dari format "1 baris = 1 fitur" jadi "1 baris = 1 observasi" (atau sebaliknya), yang sering dibutuhkan sebelum data dimasukkan ke model ML.

## Catatan Pribadi

Bukti nyata di lab ini (Cell 12 vs 13): `X * Y` menghasilkan `[[2,0],[0,2]]`, sementara `np.dot(X, Y)` menghasilkan `[[2,1],[1,2]]` — dua hasil yang **sama sekali berbeda** dari input yang sama. Kalau salah pilih operator ini di project nyata (misal saat menghitung transformasi data atau bobot model), hasilnya bisa salah total tanpa error yang jelas — karena secara sintaks kedua operasi valid, cuma maknanya beda.