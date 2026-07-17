# Lab: PostgreSQL Instance Configuration and System Catalog

## Tujuan
Memahami cara mengkonfigurasi instance PostgreSQL (parameter server, restart vs
live-reload), serta belajar menavigasi system catalog PostgreSQL (`pg_tables`,
`pg_class`, `pg_settings`) untuk mengambil metadata objek database dan mengatur
keamanan tingkat baris (Row-Level Security).

## Environment
- PostgreSQL 18.4 — terinstall native di **Windows**, dijalankan sebagai
  Windows Service (`postgresql-x64-18`)
- Dijalankan via **CMD** untuk psql, dan **Services GUI** (`services.msc`) untuk
  restart service (karena `net stop/start` butuh akses Administrator penuh)
- Dataset: `flights_RUSSIA_small.sql` (subset/versi lama dari Postgres Pro demo
  database — skema penerbangan: booking, tiket, penerbangan, kursi, boarding pass)

## Materi yang Dipelajari

| Command / Konsep | Kegunaan |
|---|---|
| `\i filename.sql` | Menjalankan/restore file dump SQL ke server |
| `\c database_name` | Berpindah koneksi ke database lain |
| `\dt` | Melihat daftar tabel (meta-command psql, interaktif saja) |
| `SHOW parameter_name;` | Melihat nilai parameter konfigurasi saat ini |
| `ALTER SYSTEM SET parameter = 'value';` | Mengubah parameter server, ditulis ke `postgresql.auto.conf` (bukan `postgresql.conf` utama) |
| `SELECT * FROM pg_tables WHERE schemaname = '...';` | Query metadata tabel via system catalog (bisa dipanggil dari script/aplikasi, beda dari `\dt`) |
| `ALTER TABLE ... ENABLE ROW LEVEL SECURITY;` | Mengaktifkan keamanan tingkat baris pada tabel |
| `SELECT relname, relrowsecurity FROM pg_class WHERE ...;` | Verifikasi status RLS suatu tabel |
| `SELECT name, setting, context, source FROM pg_settings WHERE ...;` | Melihat detail parameter, termasuk kolom `context` yang menentukan apakah butuh restart |
| `ALTER TABLE ... RENAME TO ...;` | Cara resmi mengubah nama tabel (system catalog update otomatis) |

## Relevansi ke Data Engineering
- **Context parameter (`postmaster` vs `sighup` vs `user`)** penting saat kamu
  tuning database production — salah paham soal ini bisa bikin kamu pikir
  perubahan config sudah aktif padahal belum (butuh restart), risiko downtime
  tidak terduga.
- **System catalog sebagai read-only reference** — pola ini konsisten di semua
  RDBMS modern, dan jadi dasar bagaimana tools data catalog (misalnya dbt docs,
  Atlan, atau Airflow schema sensors) melakukan introspeksi struktur database
  secara otomatis tanpa perlu akses manual ke setiap tabel.
- **Row-Level Security** relevan untuk skenario multi-tenant data warehouse —
  misalnya satu tabel data dipakai banyak klien, tapi tiap klien cuma boleh
  lihat barisnya sendiri, tanpa perlu bikin tabel/view terpisah per klien.
- Prinsip **"jangan edit metadata secara manual, selalu lewat DDL resmi"**
  berlaku universal — mencegah database berada dalam state yang tidak
  konsisten antara metadata dan struktur fisik sebenarnya.

## Catatan Pribadi
- Restart service PostgreSQL di Windows lewat `net stop/start` butuh CMD
  Administrator; kalau ribet, restart lewat `services.msc` (GUI) jauh lebih
  praktis dan tidak perlu ubah cara buka terminal.
- Perbedaan penting: `\dt` itu command interaktif psql (tidak bisa dipanggil
  dari kode program), sedangkan `pg_tables` adalah view SQL biasa yang bisa
  di-query dari mana saja termasuk aplikasi/script Python.
- File `flights_RUSSIA_small.sql` yang dipakai course ini adalah versi lama
  dari Postgres Pro demo database — skemanya (`aircrafts_data`, `ticket_flights`)
  sedikit beda dari dokumentasi resmi terbaru (`airplanes_data`, `segments`),
  tapi konsepnya tetap sama.