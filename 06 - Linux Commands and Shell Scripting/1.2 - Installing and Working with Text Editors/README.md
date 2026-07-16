# Installing and Working with Text Editors

## Tujuan
Praktik menggunakan editor teks berbasis command-line di Linux (`nano` dan `vim`)
— skill wajib untuk kerja di server yang tidak punya GUI.

## Environment
- WSL2 (Ubuntu) via VS Code
- Course: IBM Data Engineering Professional Certificate —
  Linux Commands and Shell Scripting (Module 1)

## Materi yang Dipelajari

### 1. GNU nano (editor sederhana)
| Command/Shortcut | Fungsi |
|---|---|
| `nano nama_file.txt` | Buka/buat file di nano |
| `Ctrl + O` | Save (Write Out), lalu Enter untuk konfirmasi nama file |
| `Ctrl + X` | Keluar (kalau ada perubahan belum simpan, akan ditanya Yes/No) |
| `Y` / `N` (huruf biasa, BUKAN Ctrl) | Jawaban untuk prompt "Save modified buffer?" |

### 2. vim (editor mode-based, lebih powerful)
Vim punya **2 mode utama**:
- **Command Mode** (default) — untuk navigasi & perintah, bukan untuk mengetik teks
- **Insert Mode** — untuk mengetik/edit teks (masuk dengan tombol `i`)

| Command | Fungsi |
|---|---|
| `vim nama_file.txt` | Buka/buat file di vim |
| `i` | Masuk Insert Mode (mulai bisa ngetik) |
| `Esc` | Keluar dari Insert Mode, balik ke Command Mode |
| `:w` | Simpan (write) |
| `:q` | Keluar (quit) |
| `:wq` | Simpan + keluar sekaligus |
| `:q!` | Keluar paksa, buang semua perubahan yang belum disimpan |

### 3. Verifikasi isi file
```bash
cat nama_file.txt   # tampilkan isi file langsung di terminal
```

## Cheat Sheet: nano vs vim

| | nano | vim |
|---|---|---|
| Cocok untuk | Pemula, edit cepat | Power user, lebih kuat |
| Mulai ngetik | Langsung ketik | Tekan `i` dulu |
| Save + keluar | `Ctrl+O` → Enter → `Ctrl+X` | `Esc` → `:wq` |
| Batal/keluar paksa | `Ctrl+X` → `N` | `Esc` → `:q!` |
| Petunjuk shortcut | Selalu tampil di bawah layar | Tidak ada petunjuk visual |

## Relevansi ke Data Engineering
- Server production **jarang punya GUI** — edit config file, script, atau cron job
  di server via SSH wajib pakai command-line editor.
- `vim` sangat umum jadi default editor di banyak distro server (misal saat
  `crontab -e` atau `git commit` tanpa flag `-m`), jadi minimal harus tahu
  cara keluar dengan aman (`:wq` atau `:q!`).

## Catatan Pribadi
- Sempat kejebak di prompt "Save modified buffer?" nano — ternyata jawabannya
  pakai huruf biasa (Y/N), bukan Ctrl+Y.
- Tombol `:` di vim perlu Shift (Shift + ;) — bukan soal vim, tapi keyboard biasa.
- Trap terbesar vim: refleks langsung ngetik tanpa tekan `i` dulu, teks malah
  dianggap perintah. Solusi: selalu ingat `i` untuk nulis, `Esc` untuk keluar dari nulis.