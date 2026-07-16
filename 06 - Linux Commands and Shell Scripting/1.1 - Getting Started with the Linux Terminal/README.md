# Getting Started with the Linux Terminal

## Tujuan
Lab pengenalan dasar terminal Linux — belajar berinteraksi dengan shell,
browsing direktori, navigasi filesystem, dan shortcut produktivitas
(tab completion & command history).

## Environment
- WSL2 (Ubuntu) via VS Code, dijalankan di Windows
- Course: IBM Data Engineering Professional Certificate — 
  Linux Commands and Shell Scripting (Module 1)

## Materi yang Dipelajari

### 1. Browsing direktori dengan `ls`
| Command | Fungsi |
|---|---|
| `ls` | Lihat isi direktori saat ini |
| `ls /` | Lihat isi root directory |
| `ls /bin` | Lihat isi folder /bin (bukti `ls` sendiri adalah file di /bin) |

### 2. Navigasi direktori dengan `cd`
| Command | Fungsi |
|---|---|
| `cd ~` | Pindah ke home directory |
| `cd ..` | Naik ke parent directory (relative) |
| `cd /` | Pindah ke root directory (absolute) |
| `cd bin` / `cd ./bin` | Pindah ke child directory (relative, dua cara setara) |
| `cd /path/lengkap` | Pindah pakai absolute path |

### 3. Shortcut produktivitas
- **Tab completion**: tekan `Tab` untuk auto-lengkapi nama file/folder.
  Kalau ada spasi di nama folder, Bash otomatis pakai backslash (`\ `) untuk escape.
- **Command history**: tekan `↑` untuk memanggil kembali command sebelumnya
  tanpa ngetik ulang.

## Cheat Sheet Singkat

| Symbol | Artinya |
|---|---|
| `/` | Root directory |
| `~` | Home directory |
| `.` | Direktori saat ini |
| `..` | Direktori induk (parent) |

## Relevansi ke Data Engineering
- Paham **absolute vs relative path** krusial untuk hindari error di script/pipeline
  yang dijalankan dari cron job atau server (working directory bisa beda dari asumsi).
- `/mnt/d/...` di WSL membuktikan bagaimana Linux memandang filesystem sebagai
  satu pohon tunggal (`/`), beda dari Windows yang pakai drive letter (`C:\`, `D:\`).
- Tab completion & command history akan sangat menghemat waktu saat debugging
  pipeline di server produksi (banyak ketik ulang command serupa).

## Catatan Pribadi
_(isi bagian ini dengan insight/kesulitan pribadi kamu selama lab, opsional)_