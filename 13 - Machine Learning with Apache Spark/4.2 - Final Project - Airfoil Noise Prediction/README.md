# Final Project: Build a Machine Learning Pipeline for Airfoil Noise Prediction

**Course:** 13 - Machine Learning with Apache Spark
**Module:** 4 - Final Project

## Tujuan Lab Ini

Membangun pipeline Machine Learning end-to-end menggunakan Apache Spark (PySpark) untuk memprediksi tingkat kebisingan (Sound Level) dari data aerodinamika airfoil NASA. Pipeline mencakup 4 tahap utama:
1. **ETL** — load, bersihkan (drop duplikat & null), rename kolom, simpan ke format Parquet
2. **ML Pipeline Creation** — bangun pipeline 3 stage (VectorAssembler → StandardScaler → LinearRegression)
3. **Model Evaluation** — hitung metrik MSE, MAE, R², dan intercept model
4. **Model Persistence** — simpan model terlatih ke disk, load ulang, dan buat prediksi menggunakan model yang di-load

## Struktur Folder

```
4.2 - Final Project - Airfoil Noise Prediction/
├── final_project_airfoil_noise.ipynb
├── NASA_airfoil_noise_raw.csv
├── NASA_airfoil_noise_cleaned.parquet/
├── Final_Project/                      (model tersimpan)
└── README.md
```

## Materi yang Dipelajari

- Membuat `SparkSession` dalam mode lokal (`local[*]`) sebagai pengganti Spark cluster cloud
- ETL menggunakan Spark DataFrame: `dropDuplicates()`, `dropna()`, `withColumnRenamed()`
- Menyimpan & membaca data dalam format **Parquet** (columnar storage, lebih efisien dari CSV untuk pipeline data besar)
- Membangun `Pipeline` SparkML dengan 3 stage: `VectorAssembler` (gabung fitur), `StandardScaler` (normalisasi skala), `LinearRegression` (model prediksi)
- Split data training/testing dengan `randomSplit()` dan `seed` tetap untuk hasil yang reproducible
- Evaluasi model regresi menggunakan `RegressionEvaluator` (MSE, MAE, R²)
- Menyimpan (`write().save()`) dan memuat ulang (`PipelineModel.load()`) model terlatih — pola umum untuk deployment model ke production
- Troubleshooting environment Spark di Windows lokal (kebutuhan `winutils.exe` untuk operasi filesystem Hadoop)

## Cara Menjalankan

1. Pastikan Java (8/11/17/21) dan `pip install pyspark findspark --break-system-packages` sudah terinstall
2. **Khusus Windows:** download `winutils.exe` dan `hadoop.dll` (versi sesuai Hadoop yang dibundel PySpark, cek dengan mencari file `hadoop-client-api-*.jar` di folder `pyspark/jars`), taruh di `C:\hadoop\bin`, lalu set environment variable `HADOOP_HOME=C:\hadoop` dan tambahkan `C:\hadoop\bin` ke PATH. Restart VS Code setelahnya.
3. Buka `final_project_airfoil_noise.ipynb`, pastikan kernel mengarah ke Python environment yang sudah terinstall pyspark & findspark
4. Jalankan semua cell secara berurutan (`Run All`)

## Cheat Sheet: Apache Spark ML Pipeline untuk Data Engineering

**Kapan pakai Spark vs Pandas:**

| Situasi | Pilihan |
|---|---|
| Data < beberapa GB, muat di RAM | Pandas / DuckDB — lebih simpel, overhead rendah |
| Data puluhan GB - TB, atau perlu distributed processing | Spark — bisa scale ke cluster |
| Perlu integrasi ke data lake / streaming | Spark (Spark SQL, Structured Streaming) |

**Pola pipeline SparkML yang reusable:**
```python
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.regression import LinearRegression

assembler = VectorAssembler(inputCols=[...], outputCol="features")
scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures")
model = LinearRegression(featuresCol="scaledFeatures", labelCol="target")

pipeline = Pipeline(stages=[assembler, scaler, model])
pipelineModel = pipeline.fit(trainingData)
```
Pola 3 stage ini (assemble → scale → model) adalah struktur standar yang bisa dipakai ulang untuk hampir semua kasus regresi/klasifikasi di SparkML — tinggal ganti stage terakhir sesuai algoritma (`LogisticRegression`, `RandomForestClassifier`, dll).

**Kenapa harus scaling sebelum model linear:**
Fitur dengan skala jauh berbeda (misal `Frequency` dalam ribuan vs `AngleOfAttack` dalam puluhan) bisa membuat model bias ke fitur berskala besar. `StandardScaler` menormalisasi semua fitur ke skala yang sebanding sebelum training.

**Parquet vs CSV — kenapa penting untuk data engineer:**
| Aspek | CSV | Parquet |
|---|---|---|
| Format | Row-based, teks | Columnar, biner |
| Ukuran file | Lebih besar | Lebih kecil (kompresi built-in) |
| Kecepatan baca kolom tertentu | Lambat (baca semua baris) | Cepat (baca kolom saja) |
| Skema | Tidak tersimpan | Tersimpan dalam file |

Praktik umum: simpan hasil ETL sebagai Parquet, bukan CSV, terutama untuk data yang akan dipakai berulang kali di tahap-tahap pipeline berikutnya.

**Perangkap umum:**
- **Lupa set `seed`** saat `randomSplit()` → hasil model tidak reproducible antar-run, menyulitkan debugging dan perbandingan eksperimen
- **Salah nyambung `featuresCol`** di stage terakhir (misal pakai `features` mentah, bukan `scaledFeatures`) → model tetap jalan tanpa error, tapi hasil tidak ternormalisasi dengan benar — bug diam-diam yang sulit terdeteksi
- **Windows tanpa `winutils.exe`** → error `Py4JJavaError` saat menulis file (parquet, model) meskipun proses baca & transformasi normal — solusi: setup Hadoop `winutils` seperti dijelaskan di atas
- **Precision mismatch** saat membandingkan hasil model — versi PySpark berbeda (misal 3.1.2 vs 4.2.0) bisa menghasilkan angka desimal yang sedikit berbeda karena perbedaan implementasi internal

## Catatan Pribadi

Insight paling berkesan: pipeline SparkML itu bukan sekadar "rangkaian kode", tapi objek yang bisa disimpan, dipindah, dan dipakai ulang secara utuh (assembler + scaler + model dalam satu unit) — ini yang bikin konsep ML pipeline jauh lebih production-ready dibanding cuma nulis fungsi preprocessing manual satu-satu.