## Cheat Sheet: NumPy untuk Data Engineering

**Kenapa krusial:** NumPy adalah **fondasi** Pandas — setiap kolom di DataFrame sebenarnya adalah NumPy array di balik layar. Memahami NumPy membantu memahami kenapa operasi Pandas begitu cepat (vectorized) dibanding loop manual Python biasa.

**Vectorized operation vs loop manual — bedanya krusial untuk performa:**
```python
# Cara lambat (loop manual)
result = []
for i in range(len(arr1)):
    result.append(arr1[i] + arr2[i])

# Cara cepat (vectorized, NumPy)
result = np.add(arr1, arr2)   # atau cukup arr1 + arr2
```
Untuk data besar (jutaan baris), perbedaan performa ini signifikan — NumPy memproses di level C internal, jauh lebih cepat dari loop Python murni.

**Dot product di dunia nyata:**
- **Machine Learning** — perkalian matrix di neural network pada dasarnya rangkaian dot product.
- **Cosine Similarity** — mengukur kemiripan antar dokumen/vektor teks (dipakai di recommendation system, search engine).
- **Weighted sum** — menghitung skor gabungan dari beberapa metrik dengan bobot berbeda.

**`linspace` vs `range` — kapan pakai yang mana:**

| | `range()` | `np.linspace()` |
|---|---|---|
| Hasil | Integer saja | Bisa desimal (float) |
| Kontrol | Step size (jarak antar elemen) | Jumlah elemen total |
| Kegunaan | Iterasi loop | Membuat grid nilai untuk plotting/sampling |

## Catatan Pribadi

Bagian visualisasi `Plotvec2` memberi pemahaman visual yang kuat: dot product 0 selalu terjadi saat dua vektor membentuk sudut 90° (tegak lurus) — terbukti langsung dari 2 pasang vektor uji coba di quiz yang hasilnya 0, dibanding pasangan ketiga yang tidak tegak lurus dan hasilnya bukan 0. Ini jembatan bagus antara konsep matematika abstrak dan representasi visual konkret.

## Reading: Matematika di Balik Operasi NumPy

Materi reading tambahan dari course, menjelaskan dasar matematika (aljabar linear) di balik operasi-operasi NumPy yang sudah dipraktikkan di atas.

### Vektor (Array 1D)
Array 1D disebut **vektor** dalam matematika, bisa berorientasi sebagai row vector (baris) atau column vector (kolom).

**Operasi elemen-per-elemen** — addition, subtraction, multiplication antar 2 vektor **hanya valid kalau shape-nya sama**. Hasilnya selalu punya ukuran yang sama dengan vektor aslinya.

**Operasi dengan skalar (konstanta)** — bisa ditambah/dikurang/dikali konstanta tunggal, diterapkan ke SEMUA elemen sekaligus (ini yang disebut *broadcasting*, sudah dipraktikkan di Cell 31: `u + 1`).

### Matriks (Array 2D) — Preview Topik Berikutnya
Array 2D disebut **matriks**, biasanya berbentuk tabel persegi/persegi panjang dengan data di beberapa baris.

**Aturan dot product antar matriks:**
- Dot product matriks berukuran **m × n** hanya valid dengan matriks berukuran **n × p** — jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua.
- Hasilnya berbentuk **m × p**.
- Contoh: matriks 4×2 dikalikan matriks 2×4 → hasil matriks 4×4. Sebaliknya, matriks 2×4 dikalikan 4×2 → hasil matriks 2×2 (urutan perkalian matriks **memengaruhi hasil**, tidak seperti perkalian angka biasa).

**Catatan penting soal dot product vektor:**
- Dot product **row vector** dengan **column vector** (jumlah elemen sama) → menghasilkan **1 nilai skalar tunggal** (ini yang sudah dipraktikkan di lab: `np.dot(X, Y)` menghasilkan 1 angka).
- Dot product **column vector** dengan **row vector** → menghasilkan **matriks 2D**, bukan skalar.

**Relevansi ke data engineering & ML:** operasi matriks ini adalah fondasi di balik hampir semua algoritma machine learning (regresi linear, neural network) dan transformasi data skala besar — Pandas DataFrame sendiri pada dasarnya adalah matriks 2D dengan label baris/kolom.