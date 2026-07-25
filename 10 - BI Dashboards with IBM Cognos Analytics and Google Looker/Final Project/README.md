# Final Project: SwiftAuto Traders — Sales & Service Dashboard

Dashboard interaktif untuk menganalisis penjualan mobil dan performa layanan (service/recall) di seluruh dealer **SwiftAuto Traders**, dibangun menggunakan **Google Looker Studio** sebagai bagian dari Final Project course *BI Dashboards with IBM Cognos Analytics and Google Looker* (IBM Data Engineering Professional Certificate).

**Hasil akhir: 15/15 (100%)** pada AI-graded assessment (Mark).

---

## 🎯 Tujuan

Berperan sebagai Data Scientist di SwiftAuto Traders, tugasnya adalah menganalisis data penjualan dan profit per dealer, lalu menyajikannya dalam bentuk dashboard yang mudah dipahami oleh regional manager (audiens non-teknis) untuk mendukung pengambilan keputusan bisnis.

---

## 🛠️ Environment

| Komponen | Detail |
|---|---|
| Tool BI | Google Looker Studio (free tier) |
| Sumber data | Google Sheets (hasil konversi dari CSV) |
| Penyimpanan dataset | Google Drive |
| OS lokal | Windows 11 |
| Terminal | CMD (untuk manajemen file) |

---

## 📁 Struktur Project

```
Final Project/
├── data/                                          # Dataset mentah (6 file CSV)
│   ├── AU_Car_Models.csv
│   ├── AU_Car_Recalls.csv
│   ├── AU_Daily_Sales.csv
│   ├── AU_Dealers.csv
│   ├── AU_Sales_By_Model.csv
│   └── AU_Sentiment.csv
├── screenshots/                                   # Bukti hasil kerja untuk submission
│   ├── Q1_Sales_Dashboard.png
│   ├── Q2_Service_Dashboard.png
│   └── SwiftAuto_Traders_-_Sales_&_Service_Dashboard.pdf
└── README.md
```

---

## 📚 Materi yang Dipelajari

- Menghubungkan Google Sheets sebagai data source di Looker Studio
- Membuat berbagai tipe visualisasi: Scorecard, Bar Chart, Column Chart, Treemap, Combo Chart, Pivot Table dengan Heatmap
- Konfigurasi format angka (currency, compact number/"millions")
- Mengatur sorting kustom menggunakan **Calculated Field** (CASE WHEN) untuk mengatasi data teks yang ter-sort alfabetis, bukan kronologis
- Multi-page report (memisahkan dashboard Sales dan Service ke halaman berbeda)
- Export laporan sebagai PDF

---

## 💻 Command Penting

Memindahkan dataset dari Downloads ke folder project (Windows CMD):
```cmd
copy "D:\Downloads\Looker_Dataset\Looker_Dataset\*.csv" "D:\Data-Engineering-Practice\10 - BI Dashboards with IBM Cognos Analytics and Google Looker\Final Project\data\"
```

Memindahkan hasil export PDF ke folder project (**dengan nama file spesifik**, bukan wildcard, untuk menghindari ikut ter-copy file pribadi lain di folder Downloads):
```cmd
copy "D:\Downloads\SwiftAuto_Traders_-_Sales_&_Service_Dashboard.pdf" "D:\Data-Engineering-Practice\10 - BI Dashboards with IBM Cognos Analytics and Google Looker\Final Project\screenshots\"
```

---

## 🔧 Kode Penting

**Calculated Field — Month Order** (mengatasi masalah sorting bulan yang alfabetis, bukan kronologis, karena field `Month` bertipe teks):

```sql
CASE 
  WHEN Month = "January" THEN 1
  WHEN Month = "February" THEN 2
  WHEN Month = "March" THEN 3
  WHEN Month = "April" THEN 4
  WHEN Month = "May" THEN 5
  WHEN Month = "June" THEN 6
  WHEN Month = "July" THEN 7
  WHEN Month = "August" THEN 8
  WHEN Month = "September" THEN 9
  WHEN Month = "October" THEN 10
  WHEN Month = "November" THEN 11
  WHEN Month = "December" THEN 12
END
```
Field ini digunakan sebagai kunci sort pada chart *Quantity Sold per Month vs Profit*, sementara field `Month` asli tetap dipakai sebagai label yang ditampilkan.

---

## 📊 Ringkasan Dashboard

### Sales Dashboard
| Metrik | Nilai |
|---|---|
| Total Profit | $78.25M |
| Total Quantity Sold | 58.1K |
| Average Quantity Sold | 19.4 |
| Model terlaris | Hudson (~20K unit) |
| Dealer dengan profit tertinggi | ID 1288 (~10M) |
| Dealer dengan profit terendah | ID 1222 (~5M) |

### Service Dashboard
| Metrik | Insight |
|---|---|
| Model dengan recall tertinggi | Beaufort |
| Sentimen pelanggan | Mayoritas Positive |
| Kombinasi model + sistem bermasalah tertinggi | Champlain – Suspension (60,041 unit) |
| Tren bulanan | Quantity sold & profit naik di pertengahan tahun, sedikit turun sekitar Oktober–November |

---

## 🔗 Relevansi terhadap Data Engineering

Meskipun course ini berbasis tool GUI (no-code), proses pengerjaannya mencerminkan alur kerja data engineering/BI yang sesungguhnya:

- **Data profiling sebelum desain**: sempat salah asumsi bahwa `AU_Daily_Sales` punya field Profit & Model — ternyata tidak. Ini menegaskan pentingnya inspeksi skema tiap sumber data sebelum membangun visualisasi, bukan asal drag field.
- **Tabel fakta vs tabel agregat**: `AU_Daily_Sales` (fakta transaksi mentah + cuaca) vs `AU_Sales_By_Model` (agregat siap pakai per model/dealer) — pemilihan sumber data yang tepat sangat menentukan efisiensi kerja.
- **Sort key / helper column**: teknik `Month Order` adalah pola umum di SQL (`ORDER BY CASE WHEN...`) maupun BI tools untuk mengatasi keterbatasan sorting native pada data teks.
- **Data source vs static file**: menggunakan Google Sheets connector (live-connected) alih-alih file upload statis, mencerminkan best practice agar dashboard bisa auto-refresh saat data sumber berubah.

---

## 📝 Catatan Pribadi

- Sempat terkendala di path Windows karena folder Downloads sudah di-redirect ke drive D — pelajaran: jangan asumsikan `%USERPROFILE%\Downloads` selalu benar, terutama di sistem yang sudah dikustomisasi.
- Insiden penting: penggunaan wildcard `copy *.pdf` di folder Downloads sempat ikut meng-copy 80 file pribadi (CV, sertifikat, dll) ke folder project — untung terdeteksi sebelum sempat di-commit ke Git. **Pelajaran: selalu sebutkan nama file spesifik saat bekerja dengan folder yang isinya campur-aduk.**
- Hasil akhir: **15/15 (100%)** pada penilaian AI (Mark) — passing grade course adalah 70%.