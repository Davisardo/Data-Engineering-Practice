# 2.2 - Setting up a Staging Area

## Tujuan Lab
Menyiapkan staging area untuk data warehouse `billingDW` menggunakan PostgreSQL — membuat schema resmi, memuat data dimension (`DimCustomer`, `DimMonth`) dan fact table (`FactBilling`) dari file `.sql` yang disediakan, lalu memverifikasi jumlah baris yang berhasil dimuat.

## Environment
- PostgreSQL 15 (Docker container `course9-postgres`, port 5433)
- pgAdmin 4 + Docker CLI (`docker exec`, `docker cp`)
- Database: `billingDW`

## Materi yang Dipelajari
- Konsep staging area sebagai tempat penampungan sementara sebelum data masuk ke warehouse final
- Transaction block (`BEGIN` ... `COMMIT`) untuk menjamin proses schema creation bersifat atomic
- Urutan loading data yang benar: dimension table dulu, baru fact table (karena foreign key constraint)
- Menjalankan file `.sql` di dalam container lewat `psql -f`
- `docker cp` untuk memindahkan file dari host ke dalam container

## Command & Code Penting

| Tahap | Command |
|---|---|
| Download & extract file lab | `curl -o billing-datawarehouse.tgz "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Setting%20up%20a%20staging%20area/billing-datawarehouse.tgz"` lalu `tar -xvzf billing-datawarehouse.tgz` |
| Copy file ke container | `docker cp <nama_file>.sql course9-postgres:/<nama_file>.sql` (diulang untuk 5 file) |
| Hapus tabel lama (dari lab 2.1) | `DROP TABLE IF EXISTS FactBilling; DROP TABLE IF EXISTS DimCustomer; DROP TABLE IF EXISTS DimMonth;` |
| Bikin schema resmi | `docker exec -it course9-postgres psql -U postgres -d billingDW -f /star-schema.sql` |
| Load data dimension | `docker exec -it course9-postgres psql -U postgres -d billingDW -f /DimCustomer.sql` dan `/DimMonth.sql` |
| Load data fact | `docker exec -it course9-postgres psql -U postgres -d billingDW -f /FactBilling.sql` |
| Verifikasi | `docker exec -it course9-postgres psql -U postgres -d billingDW -f /verify.sql` |

**Hasil verifikasi:**
| Tabel | Jumlah baris |
|---|---|
| DimMonth | 132 |
| DimCustomer | 1000 |
| FactBilling | 132000 |

## Relevansi terhadap Data Engineering
Staging area adalah pola umum di ETL pipeline untuk memisahkan proses transformasi/loading dari data warehouse final, sehingga risiko data kotor bisa diisolasi dan proses bisa diaudit. Urutan loading dimension-sebelum-fact adalah aturan wajib di setiap star schema karena foreign key constraint — pola ini akan selalu muncul di pipeline data warehouse manapun di dunia kerja.

## Catatan Pribadi
- Tabel `DimCustomer`, `DimMonth`, `FactBilling` yang dibuat manual di lab 2.1 sengaja dihapus (`DROP TABLE`) sebelum menjalankan `star-schema.sql` resmi, supaya tidak bentrok nama tabel — proses ini melatih pemahaman kenapa urutan `DROP` juga penting (fact dulu baru dimension, kebalikan dari urutan `CREATE`/`LOAD`).
- Baru paham lebih dalam soal transaction (`BEGIN`...`COMMIT`) setelah lihat output `star-schema.sql` — dulu di lab 2.1 bikin tabel manual satu-satu tanpa transaction eksplisit.
- Angka `132000` di `FactBilling` masuk akal karena 1000 customer × 132 bulan — jadi ketemu logika kenapa jumlahnya sebesar itu, bukan cuma hafal angka doang.