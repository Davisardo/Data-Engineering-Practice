# 2.1 - Querying Data in NoSQL Databases

## Tujuan
Mengimpor, meng-query, dan meng-export data katalog produk e-commerce (SoftCart) menggunakan MongoDB sebagai database NoSQL, sebagai bagian dari Modul 2 - Data Engineering Capstone Project (IBM Data Engineering Professional Certificate).

Modul ini melengkapi Modul 1 (OLTP/MySQL) dengan menunjukkan bagaimana data semi-terstruktur (katalog produk dengan atribut bervariasi per kategori) ditangani menggunakan database dokumen, sebagai bagian dari arsitektur data hybrid SoftCart.

## Environment
- **OS:** Windows 11
- **Database:** MongoDB Community Server 8.3.7, berjalan sebagai Windows Service (`MongoDB`)
- **Tools:**
  - `mongosh` 2.9.2 (shell interaktif untuk query)
  - MongoDB Database Tools 100.17.0 (`mongoimport`, `mongoexport`)
- **Terminal:** CMD

### Catatan Instalasi
MongoDB Community Server, `mongosh`, dan Database Tools diinstal secara terpisah (tiga package berbeda). `mongosh` dan Database Tools tidak otomatis masuk ke System PATH, sehingga perlu ditambahkan manual melalui Environment Variables, diikuti restart penuh laptop agar perubahan PATH ter-apply ke semua proses baru.

## Struktur Project
```
2.1 - Querying Data in NoSQL Databases/
├── catalog.json          # Data mentah hasil download (format JSON Lines)
├── electronics.csv        # Hasil export field _id, type, model
└── README.md
```

## Materi yang Dipelajari
- Konsep database NoSQL berbasis dokumen (document store) dan fleksibilitas skema — dokumen `laptop` dan `smart phone` di collection yang sama boleh memiliki field berbeda (laptop punya `ram` dan `hard disk`, smartphone tidak), berbeda total dari skema kaku di MySQL OLTP (Modul 1)
- Import bulk data JSON Lines menggunakan `mongoimport`
- Query dasar (`countDocuments`) dengan filter pada field bernama ganda (`"screen size"`)
- MongoDB Aggregation Pipeline (`$match`, `$group`, `$avg`) untuk menghitung agregat seperti rata-rata
- Pembuatan index pada field non-`_id` (`createIndex`)
- Export data terpilih (subset field) ke format CSV menggunakan `mongoexport`

## Command Penting

**Import data:**
```bash
mongoimport --db catalog --collection electronics --file catalog.json
```

**Query interaktif (mongosh):**
```javascript
show dbs
use catalog
show collections

db.electronics.createIndex({ type: 1 })

db.electronics.countDocuments({ type: "laptop" })
// Hasil: 389

db.electronics.countDocuments({ type: "smart phone", "screen size": 6 })
// Hasil: 8

db.electronics.aggregate([
  { $match: { type: "smart phone" } },
  { $group: { _id: null, avgScreenSize: { $avg: "$screen size" } } }
])
// Hasil: { avgScreenSize: 6 }
```

**Export data:**
```bash
mongoexport --db catalog --collection electronics --type csv --fields _id,type,model --out electronics.csv
```

## Relevansi terhadap Data Engineering
Modul ini melatih kemampuan bekerja dengan sumber data heterogen — kombinasi SQL (OLTP transaksional) dan NoSQL (katalog fleksibel) yang sama-sama umum ditemui di perusahaan e-commerce sungguhan. Skill query dan aggregation MongoDB di sini menjadi dasar bagi proses ETL di Modul 5, di mana data dari MongoDB (bersama MySQL) akan diekstrak dan dimuat ke dalam data warehouse terpusat (Modul 3).

## Catatan Pribadi
- MongoDB default tidak mengaktifkan access control (tanpa username/password) — cukup aman untuk lab lokal, tetapi tidak boleh digunakan seperti ini di production.
- Field bernama `"screen size"` (mengandung spasi) mengharuskan penulisan query dengan tanda kutip eksplisit — detail kecil yang mudah menyebabkan hasil query kosong jika terlewat.
- Instalasi MongoDB sempat gagal di percobaan pertama karena installer tidak dijalankan dengan privilege Administrator — pelajaran yang sama seperti kendala service MySQL di Modul 1.