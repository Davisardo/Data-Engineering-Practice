# Views in PostgreSQL

**Course:** 04 - Relational Databases Fundamentals (Introduction to Relational Databases (RDBMS) — IBM/Coursera)
**Module:** 3 — Lab 3.6

## Tujuan Lab Ini

- Merestore skema dan data database dari file dump
- Membuat dan menjalankan view
- Membuat dan menjalankan materialized view

## Struktur Folder

```
3.6 - Views in PostgreSQL/
├── eBooks_pgsql_dump.tar      # dump file database eBooks (format custom/tar)
└── README.md
```

*(Catatan: database `eBooks`, view, dan materialized view tersimpan di dalam PostgreSQL Server lokal, bukan file di folder ini)*

## Materi yang Dipelajari

- Restore database dari file dump format **custom/tar** (bukan `.sql` teks biasa) menggunakan fitur **Restore** di pgAdmin, yang di baliknya memanggil `pg_restore` — beda mekanisme dengan `\include` atau "Open SQL Script" yang dipakai untuk file `.sql`
- Opsi **"Disable Triggers"** saat restore — mencegah trigger otomatis (misal update timestamp) terpicu berulang kali saat data di-insert massal
- **View**: query tersimpan yang dijalankan ulang setiap kali diakses, tidak menyimpan data fisik — selalu real-time mengikuti perubahan tabel sumber
- **Materialized View**: menyimpan hasil query sebagai data fisik (seperti tabel), sehingga jauh lebih cepat diakses untuk query kompleks/berat, tapi datanya **tidak otomatis update** — harus di-*refresh* manual (`REFRESH MATERIALIZED VIEW ... WITH DATA`) setiap kali ingin data terbaru
- Materialized View yang baru dibuat **wajib** di-refresh minimal sekali sebelum bisa diakses — kalau langsung diakses tanpa refresh, akan muncul error "has not been populated"

## Cara Menjalankan

1. Download dump file:
```cmd
   curl -o eBooks_pgsql_dump.tar https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/eBooks/eBooks_pgsql_dump.tar
```
2. Buat database `eBooks` di pgAdmin, lalu klik kanan → **Restore...**
   - Format: `Custom or tar`
   - Filename: pilih file `.tar` (pastikan filter file browser di-set ke "All Files", bukan "*.backup")
   - Tab Options: aktifkan **Disable → Triggers**
   - Klik **Restore**
3. Buat View:
```sql
   -- Nama: publisher_and_rating_view
   SELECT books.title, books.rating, publishers.name
   FROM books INNER JOIN publishers ON books.publisher_id = publishers.publisher_id
```
4. Buat Materialized View (query sama), lalu **wajib** refresh:
   - Klik kanan materialized view → **Refresh View** → **With data**

## Cheat Sheet: Views & Materialized Views untuk Data Engineering

| Aspek | View | Materialized View |
|---|---|---|
| Data fisik | Tidak (query dijalankan ulang tiap akses) | Ya (data di-cache) |
| Kecepatan akses | Tergantung kompleksitas query dasar | Cepat (data sudah tersimpan) |
| Update otomatis | Selalu real-time | Perlu `REFRESH` manual |
| Kapan dipakai | Query yang sering dipakai ulang, data sumber sering berubah | Query berat/agregasi kompleks, data sumber jarang berubah, dibutuhkan performa cepat |

**Koneksi ke project sebelumnya:**

Konsep View di sini mirip dengan bikin fungsi reusable di Python — daripada menulis ulang JOIN yang sama berkali-kali di berbagai query, View menyimpannya sebagai satu objek yang bisa dipanggil seperti tabel biasa. Materialized View lebih dekat ke konsep **caching** dalam data engineering: trade-off antara kecepatan akses (data sudah "siap saji") versus kesegaran data (harus di-refresh manual). Ini relevan banget untuk pipeline ETL/data warehouse — laporan dashboard yang berat query-nya sering dibuat sebagai materialized view yang di-refresh terjadwal (misal tiap malam), bukan dihitung ulang tiap kali user membuka dashboard.

**Perangkap umum:**
- File browser pgAdmin bisa punya filter default yang menyembunyikan tipe file tertentu (misal cuma menampilkan `*.backup`) — kalau file yang dicari tidak muncul di list, cek dulu dropdown filter format-nya, jangan asumsikan file-nya hilang
- Restore gagal dengan pesan `"toc.dat" does not exist` biasanya berarti path yang dipilih itu **folder**, bukan **file** `.tar`-nya — pastikan klik langsung pada nama file, bukan cuma masuk ke foldernya
- Materialized View baru **selalu kosong** sampai di-refresh minimal sekali — jangan buru-buru cek datanya sebelum refresh, atau akan muncul error "has not been populated"

## Catatan Pribadi

Insight paling berkesan: proses restore file `.tar` sempat gagal 2x karena masalah teknis kecil (filter file browser, salah pilih folder vs file) — ini pengingat bagus bahwa error message yang jelas (`pg_restore: error: ... does not appear to be a valid archive`) itu sangat membantu debugging, asal dibaca teliti. Perbedaan mendasar antara View dan Materialized View juga jadi lebih jelas lewat praktik langsung: keduanya menghasilkan data yang identik saat pertama kali diakses, tapi konsekuensi trade-off-nya (freshness vs performance) baru terasa maknanya setelah tau bahwa Materialized View butuh refresh manual sementara View biasa tidak.