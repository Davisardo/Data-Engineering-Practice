# Navigating and Managing Files and Directories

## Tujuan
Praktik command-command untuk navigasi lanjutan (wildcard, opsi `ls`),
serta membuat, mencari, menghapus, memindahkan, dan menyalin file/direktori.

## Environment
- WSL2 (Ubuntu) via VS Code
- Course: IBM Data Engineering Professional Certificate —
  Linux Commands and Shell Scripting (Module 2)

## Materi yang Dipelajari

### 1. Wildcard & Opsi ls
| Command | Fungsi |
|---|---|
| `ls /bin/b*` | List file yang DIAWALI huruf tertentu (wildcard `*`) |
| `ls /bin/*r` | List file yang DIAKHIRI huruf tertentu |
| `ls -l` | Format panjang: permission, owner, ukuran, tanggal modifikasi |
| `ls -a` | Tampilkan file/folder tersembunyi (diawali titik) |
| `ls -la` | Gabungan `-l` dan `-a` |

### 2. Membuat File & Direktori
| Command | Fungsi |
|---|---|
| `mkdir nama_folder` | Buat direktori baru |
| `cd` (tanpa argumen) | Shortcut ke home directory (setara `cd ~`) |
| `touch nama_file` | Buat file kosong, atau update timestamp jika file sudah ada |
| `date -r nama_file` | Cek kapan file terakhir dimodifikasi |

### 3. Mengelola File & Direktori
| Command | Fungsi |
|---|---|
| `find /path -name '*.ext'` | Cari file berdasarkan pola nama (rekursif ke subfolder) |
| `rm -i nama_file` | Hapus file DENGAN konfirmasi (`y`/`n`) — lebih aman |
| `rm -r nama_folder` | Hapus folder beserta isinya (rekursif) — HATI-HATI, tidak ada trash |
| `rmdir nama_folder` | Hapus folder HANYA jika kosong (lebih aman dari `rm -r`) |
| `mv sumber tujuan` | Pindahkan file, ATAU rename jika tujuan di folder yang sama |
| `cp sumber tujuan` | Salin file (file asal tetap ada, beda dengan `mv`) |

## Cheat Sheet: cp vs mv
| | `cp` (copy) | `mv` (move) |
|---|---|---|
| File asal | Tetap ada | Hilang (dipindah) |
| Hasil | File baru (duplikat) | File sama, lokasi/nama berubah |
| Analoginya | Fotokopi dokumen | Pindahkan dokumen asli |

## Relevansi ke Data Engineering
- `find` sangat berguna untuk mencari file log/data spesifik di server dengan
  ribuan file (misal: `find /var/log -name '*.log'`).
- `cp` dan `mv` adalah dasar manajemen file pipeline data (misal pindahkan
  hasil ETL ke folder "processed", backup file sebelum overwrite).
- Wildcard (`*`) sering dipakai untuk operasi massal, misal
  `rm *.tmp` atau `cp data_2026*.csv backup/`.
- "Permission denied" saat `find` di folder sistem itu normal — bagian dari
  mekanisme keamanan Linux (akan dibahas lebih detail di topik permission).

## Catatan Pribadi
- File `/etc/passwd` berisi daftar semua user sistem, formatnya
  `username:x:UID:GID:...:home_dir:shell`. User service (non-login) biasanya
  punya shell `/usr/sbin/nologin`.
- Perlu hati-hati mengecek posisi folder (`pwd`) sebelum menjalankan
  `touch`/`mv`/`cp` — sempat salah folder sekali saat praktik.