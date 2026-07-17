# Informational Commands

## Tujuan
Praktik command-command dasar untuk mengecek informasi sistem: user, OS,
disk usage, proses yang berjalan, serta cara mencari bantuan/dokumentasi
command bawaan Linux.

## Environment
- WSL2 (Ubuntu) via VS Code
- Course: IBM Data Engineering Professional Certificate —
  Linux Commands and Shell Scripting (Module 2)

## Materi yang Dipelajari

### 1. Info User
| Command | Fungsi |
|---|---|
| `whoami` | Nama user yang sedang login |
| `id` | UID, GID, dan semua group user |
| `id -u` | Hanya UID (angka) |
| `id -u -n` | Nama user berdasarkan UID |

### 2. Info Sistem Operasi
| Command | Fungsi |
|---|---|
| `uname` | Nama kernel (Linux) |
| `uname -s -r` | Nama + versi kernel |
| `uname -v` | Info build kernel lebih detail |

### 3. Disk Usage
| Command | Fungsi |
|---|---|
| `df -h ~` | Disk usage untuk home directory (human-readable) |
| `df -h` | Disk usage semua filesystem yang ter-mount |

### 4. Proses yang Berjalan
| Command | Fungsi |
|---|---|
| `ps -e` | List semua proses (snapshot sekali) |
| `top` | Monitor proses real-time (interaktif, keluar dengan `q`) |

### 5. Cetak Teks & Variabel
| Command | Fungsi |
|---|---|
| `echo "teks"` | Cetak teks ke layar |
| `echo $PATH` | Cetak isi variabel environment `PATH` |

### 6. Tanggal & Waktu
| Command | Fungsi |
|---|---|
| `date` | Tanggal & waktu format default |
| `date +"%A %j %Y"` | Format custom (nama hari, hari ke-N, tahun) |

### 7. Dokumentasi Bawaan
| Command | Fungsi |
|---|---|
| `man nama_command` | Buka manual lengkap suatu command (navigasi panah, keluar `q`) |

## Relevansi ke Data Engineering
- `df -h` dan `top`/`ps` adalah command pertama untuk debugging server saat
  pipeline data lambat/gagal (cek disk penuh, proses hang, CPU/memory tinggi).
- `date` sering dipakai untuk generate nama file log/backup otomatis
  (misal `backup_$(date +%Y%m%d).csv`).
- `$PATH` menjelaskan bagaimana shell menemukan lokasi executable command
  (relevan untuk debugging "command not found").

## Catatan Pribadi
- `echo $PATH` di WSL menunjukkan WSL Interop — PATH gabungan antara
  Linux (`/bin`, `/usr/bin`) dan Windows (`/mnt/c/...`), sehingga program
  Windows bisa dipanggil langsung dari WSL.
- `top` itu tampilan live/interaktif, keluar pakai huruf `q`, bukan Ctrl+C.