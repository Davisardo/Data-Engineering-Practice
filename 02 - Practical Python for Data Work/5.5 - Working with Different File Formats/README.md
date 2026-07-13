## Hasil Analisis: Dataset Diabetes

Dataset dari National Institute of Diabetes and Digestive and Kidney Diseases, 768 baris × 9 kolom (8 fitur + 1 label `Outcome`).

- **Missing values:** tidak ada (dataset sudah bersih).
- **Tipe data:** semua kolom sudah sesuai (int64/float64), tidak perlu konversi.
- **Distribusi Outcome:** 65.10% Not Diabetic, 34.90% Diabetic.

## Cheat Sheet: Read/Save Berbagai Format File

| Format | Baca | Simpan |
|---|---|---|
| CSV | `pd.read_csv()` | `df.to_csv()` |
| JSON | `pd.read_json()` / `json.load()` | `df.to_json()` / `json.dump()` |
| Excel | `pd.read_excel()` | `df.to_excel()` |
| XML | `pd.read_xml()` | `xml.etree.ElementTree` (manual) |
| HDF | `pd.read_hdf()` | `df.to_hdf()` |

**Kenapa krusial di data engineering:** di dunia nyata, data jarang datang dalam 1 format seragam — pipeline sering perlu membaca dari berbagai sumber (API JSON, laporan Excel dari tim finance, XML dari sistem legacy, CSV dari export database) lalu menyatukannya jadi 1 struktur konsisten.

**Pola serialize/deserialize JSON — dasar komunikasi API:**
```python
# Serialize: Python object -> JSON (untuk kirim/simpan)
json_string = json.dumps(python_dict, indent=4)

# Deserialize: JSON -> Python object (untuk baca/proses)
python_dict = json.loads(json_string)
```
Ini persis proses yang terjadi otomatis saat `requests.get(url).json()` di lab-lab API sebelumnya — di balik layar, response text di-deserialize jadi dictionary Python.

**Pola manual parsing vs shortcut Pandas — konsisten di seluruh course:**

| Format | Manual | Shortcut Pandas |
|---|---|---|
| HTML table | BeautifulSoup + loop `find_all('tr')` | `pd.read_html()` |
| XML | `xml.etree.ElementTree` + loop node | `pd.read_xml()` |

Pola ini berulang di course: pelajari cara manual dulu (paham struktur data di baliknya), baru kenalan dengan shortcut Pandas yang jauh lebih ringkas untuk pekerjaan sehari-hari.

## Catatan Pribadi

Lab ini terasa seperti **rangkuman besar** dari seluruh perjalanan course — mulai dari konsep dasar Python (list, dict), lanjut ke file I/O, Pandas, NumPy, API, web scraping, dan sekarang semuanya digabung dalam satu alur: baca data dari format apapun → validasi & bersihkan → analisis → visualisasikan. Ini persis siklus kerja seorang data engineer/analyst sehari-hari.