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