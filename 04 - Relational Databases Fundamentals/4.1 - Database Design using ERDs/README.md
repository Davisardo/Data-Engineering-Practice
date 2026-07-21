# Database Design using ERDs

**Course:** 04 - Relational Databases Fundamentals (Introduction to Relational Databases (RDBMS) — IBM/Coursera)
**Module:** 4 — Lab 4.1

## Tujuan Lab Ini

- Membuat Entity Relationship Diagram (ERD) dari sebuah database
- Generate dan eksekusi SQL script dari ERD untuk membuat skema
- Memuat skema database dengan data

Lab ini terdiri dari 2 bagian: **Example Exercise** (bikin ERD dari nol, 4 tabel) dan **Practice Exercise** (load ERD dari file, tambah relasi, 7 tabel lengkap).

## Struktur Folder

```
4.1 - Database Design using ERDs/
├── HR_pgsql_dump_data_for_example-exercise.tar   # data untuk Example Exercise (4 tabel)
├── HR_pgsql_ERD_for_practice-exercise.pgerd       # file ERD untuk Practice Exercise (load, bukan bikin manual)
├── HR_pgsql_dump_data.tar                          # data lengkap untuk Practice Exercise (7 tabel)
└── README.md
```

*(Catatan: database `HR` dan `HR_Complete` beserta skema/ERD-nya tersimpan di dalam PostgreSQL Server lokal, bukan file di folder ini)*

## Materi yang Dipelajari

- **ERD Designer (Beta)** di pgAdmin: alat visual drag-drop untuk merancang skema database — bikin entity (tabel), definisikan kolom, dan hubungkan lewat relasi (Foreign Key) tanpa menulis SQL manual
- **One-to-Many relationship**: cara mendefinisikan FK secara visual — klik tabel sumber (sisi "many"), klik tombol relasi, tentukan kolom lokal & tabel/kolom yang direferensikan
- **Self-referencing relationship**: tabel yang merujuk ke dirinya sendiri (`employees.manager_id` → `employees.employee_id`), pola umum untuk struktur hierarki
- **Generate SQL dari ERD**: ERD Designer otomatis membuat script `CREATE TABLE` + `ALTER TABLE ADD FOREIGN KEY` dari diagram visual yang dibuat
- **Load ERD dari file `.pgerd`**: format file ERD pgAdmin yang bisa di-share dan dimuat ulang — mempercepat kerja kalau skema dasarnya sudah didesain orang lain
- **Debugging restore data vs skema**: ketika skema tabel tidak lengkap dibanding data yang di-restore, `pg_restore` memberi pesan error yang menyebutkan kolom yang hilang dan struktur `COPY` lengkap yang diharapkan — sangat membantu untuk memperbaiki skema secara iteratif
- **TRUNCATE ... RESTART IDENTITY CASCADE**: membersihkan data parsial hasil restore yang gagal di tengah jalan, sebelum mencoba restore ulang

## Cara Menjalankan

**Example Exercise:**
1. Buat database `HR`, buka **Generate ERD (Beta)**
2. Buat 4 entity manual: `employees`, `jobs`, `departments`, `locations` (skema lengkap termasuk `commission_pct`, `street_address`, `postal_code`, `state_province`, `country_id`, `manager_id` — lihat Cheat Sheet)
3. Buat 4 relasi: `employees→departments`, `employees→jobs`, `departments→locations`, `employees→employees` (manager)
4. Generate SQL, Execute
5. Download & restore data:
```cmd
   curl -o HR_pgsql_dump_data_for_example-exercise.tar https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/HR_Database/HR_Proper/HR_pgsql_dump_data_for_example-exercise.tar
```

**Practice Exercise:**
1. Buat database `HR_Complete`
2. Buka ERD Designer → **Load from file** → pilih `HR_pgsql_ERD_for_practice-exercise.pgerd`
3. Tambah 5 relasi yang kurang: `countries→regions`, `job_history→departments`, `job_history→employees`, `job_history→jobs`, `locations→countries`
4. Generate SQL, Execute
5. Download & restore data lengkap:
```cmd
   curl -o HR_pgsql_dump_data.tar https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/HR_Database/HR_Proper/HR_pgsql_dump_data.tar
```

## Cheat Sheet: ERD Design & Skema HR Database

**Skema lengkap tabel `employees` (termuan iteratif dari proses debugging):**

| Kolom | Tipe | Catatan |
|---|---|---|
| employee_id | integer | PK |
| first_name, last_name, email | varchar | last_name & email NOT NULL |
| phone_number | varchar(20) | |
| hire_date | date | NOT NULL |
| job_id | varchar(10) | NOT NULL, FK → jobs |
| salary | numeric | |
| commission_pct | numeric | **kolom yang sempat terlewat** — wajib ada untuk restore data sukses |
| manager_id | integer | FK → employees (self) |
| department_id | integer | FK → departments |

**Koneksi ke dunia kerja nyata (data engineering):**

Di kerjaan nyata, mendesain skema lewat GUI drag-drop seperti ERD Designer ini **jarang jadi cara utama** — biasanya skema didefinisikan sebagai **kode** lewat migration tools (Alembic, Flyway, dbt) yang di-track di Git, supaya perubahan skema punya histori jelas dan bisa direview tim. ERD visual biasanya dipakai untuk *dokumentasi/diskusi desain*, bukan implementasi langsung. Ada 2 hal dari lab ini yang **sangat relevan** dengan kerja nyata meski caranya disederhanakan:
1. **Skema-data mismatch adalah hal rutin** — file/API/dump data eksternal jarang 100% cocok dengan asumsi skema awal; membaca error message `pg_restore` untuk tahu kolom apa yang kurang adalah skill debugging inti
2. **Restore/migrate data antar environment** (dev → staging → production) adalah tugas rutin data engineer

**Perangkap umum:**
- Skema yang dibuat manual (Example Exercise) gampang tidak lengkap dibanding data asli — selalu siap membaca error `pg_restore` untuk tahu kolom yang hilang, jangan menebak dari awal
- Restore yang gagal di tengah jalan bisa meninggalkan data "setengah jalan" — jalankan `TRUNCATE ... CASCADE` sebelum mencoba restore ulang untuk menghindari error duplicate key
- Klik "1-M" tanpa tabel sumber ter-select dengan benar akan menghasilkan dialog dengan field kosong semua — pastikan klik tabel dulu sebelum klik tombol relasi

## Catatan Pribadi

Insight paling berkesan: proses trial-error nemuin kolom yang hilang satu-satu (`commission_pct`, `street_address`, `postal_code`, `state_province`, `country_id`, `manager_id`) itu justru pengalaman belajar paling berharga di lab ini — bukan proses drag-drop bikin ERD-nya. Membaca pesan error `pg_restore` yang menyebutkan struktur `COPY` lengkap yang diharapkan, lalu memperbaiki skema secara iteratif sampai berhasil, adalah simulasi kecil dari skill debugging yang benar-benar dipakai sehari-hari di data engineering — jauh lebih berkesan daripada kalau semua langsung berjalan mulus dari awal.