# Final Assignment — ETL Data Pipelines with BashOperator using Apache Airflow

Bagian dari **IBM Data Engineering Professional Certificate**
Course: *ETL and Data Pipelines with Shell, Airflow and Kafka*

## Tujuan

Membangun DAG Apache Airflow yang mengekstrak data lalu lintas tol dari 3 sumber
berformat berbeda (CSV, TSV, fixed-width), mentransformasi salah satu kolomnya,
lalu menggabungkan semuanya menjadi satu file konsolidasi di staging area —
mensimulasikan skenario nyata mengumpulkan data dari beberapa operator tol yang
punya sistem IT berbeda-beda.

## Environment

- **OS**: Windows, dijalankan lewat CMD + Docker Desktop (WSL2 backend)
- **Orkestrasi**: Docker Compose, `apache/airflow:2.9.3`, executor CeleryExecutor
  (Postgres + Redis)
- **Airflow Web UI**: `http://localhost:8081` (port disesuaikan dari default 8080
  karena ada stack Airflow lain di komputer ini yang memakai port tersebut)
- **Struktur folder**:
  ```
  Final Project - ETL Toll Data/
  ├── dags/
  │   ├── ETL_toll_data.py         # DAG utama
  │   └── staging/                  # hasil ekstraksi & file final
  ├── docker-compose.yaml
  └── .env
  ```

## Materi yang dipelajari & command/code yang dipakai

| Konsep | Command / Kode | Keterangan |
|---|---|---|
| Setup Airflow via Docker | `docker compose up -d` | Menjalankan seluruh stack (webserver, scheduler, worker, triggerer, postgres, redis) di background |
| Definisi DAG & default_args | `DAG(dag_id=..., default_args=..., catchup=False)` | `catchup=False` penting untuk mencegah backfill run massal saat `start_date` di masa lalu |
| Ekstraksi CSV | `cut -d"," -f1-4 file.csv > out.csv` | Ambil kolom berdasarkan delimiter koma |
| Ekstraksi TSV | `cut -f5-7 file.tsv \| tr -d "\r" \| tr "\t" ","` | `tr -d "\r"` wajib karena file sumber pakai line-ending Windows (CRLF), kalau tidak dibuang akan nempel jadi karakter sampah di kolom terakhir |
| Ekstraksi fixed-width | `cut -c59-67 file.txt \| tr -s " " ","` | Range karakter harus mencakup spasi pemisah antar-field, kalau di-skip field akan nempel jadi satu |
| Gabung file horizontal | `paste -d"," f1 f2 f3 > out.csv` | Menggabungkan kolom (bukan baris) dari beberapa file sekaligus |
| Transformasi kolom spesifik | `awk -F"," 'BEGIN{OFS=","} {$4=toupper($4); print}'` | Lebih presisi dari `tr` karena hanya mengubah satu kolom, bukan seluruh baris |
| Task dependency | `t1 >> t2 >> t3 ...` | Operator downstream, urutan eksekusi sequential |
| Debug DAG | `airflow dags list-import-errors`, `airflow dags list` | Verifikasi DAG ter-load tanpa error syntax |
| Reset DAG state | `airflow dags delete <dag_id> -y` | Menghapus history run dari database tanpa menghapus file `.py` |

## Relevansi ke Data Engineering

- **Handling multi-format data source** — kasus nyata di industri, tiap vendor/sistem
  sering pakai format ekspor berbeda; harus bisa menyatukan tanpa mengubah sistem sumber.
- **Idempotency & catchup** — memahami `catchup=False` penting untuk pipeline produksi
  supaya tidak tanpa sengaja memproses ulang data historis dalam jumlah besar.
- **Debugging pipeline lewat log** — kemampuan membaca Airflow task log untuk
  mendiagnosis kegagalan (misal isu CRLF, path salah) adalah skill sehari-hari DE.
- **Docker sebagai environment standar** — hampir semua deployment Airflow modern
  berjalan di container/K8s, bukan native install.

## Catatan Pribadi

- Environment asli lab (IBM Cloud IDE) memakai path `/home/project/airflow/dags/...`;
  di setup lokal ini disesuaikan ke `/opt/airflow/dags/...` mengikuti struktur volume
  mount Docker Compose resmi Apache Airflow.
- Sempat menemukan 2 bug tersembunyi yang tidak muncul di instruksi lab asli:
  1. File `tollplaza-data.tsv` memakai line-ending CRLF (khas Windows), butuh `tr -d "\r"`
     tambahan sebelum konversi delimiter.
  2. `cut -c` dengan range terpisah koma (mis. `59-61,63-67`) tidak menyisipkan spasi
     pemisah antar-range; solusinya ambil range utuh (`59-67`) baru squeeze spasi jadi koma.
- Pelajaran ini menegaskan pentingnya selalu verifikasi output mentah tiap tahap
  ETL (`head`, `cat -A`) daripada asumsi command shell selalu berperilaku "intuitif".