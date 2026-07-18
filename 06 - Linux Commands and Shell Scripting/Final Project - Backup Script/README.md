# Final Project: Automated Backup Script

## Tujuan
Final project graded course "Linux Commands and Shell Scripting" (IBM).
Membuat script Bash `backup.sh` yang secara otomatis meng-arsipkan file
yang berubah dalam 24 jam terakhir di suatu direktori, lalu menjadwalkannya
untuk berjalan otomatis setiap hari menggunakan `cron`.

## Skenario
Sebagai Linux developer di perusahaan fiktif ABC International Inc.,
membuat sistem backup otomatis untuk file-file penting yang sering berubah.

## Environment
- WSL2 (Ubuntu) via VS Code
- Course: IBM Data Engineering Professional Certificate —
  Linux Commands and Shell Scripting (Final Project)

## Cara Menjalankan
```bash
./backup.sh <folder_sumber> <folder_tujuan>
# Contoh:
./backup.sh important-documents .
```
Script akan membuat file `backup-<timestamp>.tar.gz` berisi semua file
di `<folder_sumber>` yang dimodifikasi dalam 24 jam terakhir.

## Konsep Shell Scripting yang Dipelajari

| Konsep | Implementasi di Script |
|---|---|
| Shebang | `#!/bin/bash` — menandai file sebagai script Bash |
| Command line arguments | `$1`, `$2`, `$#` — argumen saat script dipanggil |
| Command substitution | `` `date +%s` `` — simpan hasil command ke variabel |
| Variable interpolation | `"$targetDirectory"` — sisipkan isi variabel ke teks/path |
| Aritmatika Bash | `$(($currentTS - 24*60*60))` — hitung timestamp 24 jam lalu |
| Array | `declare -a toBackup`, `toBackup+=($file)` — kumpulkan daftar file |
| For loop | `for file in *` — iterasi semua file di direktori |
| If statement | `if [[ ... -gt ... ]]` — cek kondisi (file lebih baru dari kemarin) |
| Guard clause | `cd "$dir" \|\| exit` — hentikan script jika `cd` gagal (safety) |
| `tar` | `tar -czvf` — compress & archive banyak file jadi satu |
| `chmod` | `chmod u+x` — beri izin eksekusi ke script |
| `cron` | Jadwalkan script jalan otomatis (`crontab -e`) |

## Deployment
```bash
sudo cp backup.sh /usr/local/bin/
chmod u+x /usr/local/bin/backup.sh
```

## Penjadwalan (Cron)
0 0 * * * /usr/local/bin/backup.sh "<path_folder>" /tmp

Format cron: `menit jam tanggal bulan hari command`. `0 0 * * *` = tiap hari jam 00:00.

## Relevansi ke Data Engineering
- Ini adalah pola dasar **automated backup/archival pipeline** — sangat umum
  di data engineering untuk backup database dump, log file, atau hasil ETL
  secara terjadwal tanpa campur tangan manual.
- Konsep guard clause (`|| exit`) penting untuk mencegah script merusak
  data di lokasi yang salah jika terjadi error di tengah eksekusi.
- `cron` adalah scheduler paling dasar sebelum beralih ke tools orchestration
  yang lebih canggih (Airflow, dll) di dunia data engineering profesional.

## Catatan Pribadi & Debugging
- **Bug variable tanpa kutip**: `mv $backupFileName $destDirAbsPath` gagal
  karena nama folder mengandung spasi, dan variabel tanpa kutip dipecah
  jadi beberapa argumen oleh Bash. Solusi: selalu bungkus variabel path
  dengan `" "`.
- **Wildcard `*` tidak match dotfile**: testing pertama di `/home/davisardo25`
  gagal karena folder itu isinya cuma dotfile (`.bashrc`, dll) yang tidak
  cocok wildcard default `*`. Solusi: test di folder berisi file biasa.
- **Cron di WSL tidak auto-start**: perlu `sudo service cron start` manual,
  beda dari Linux server biasa yang cron-nya auto-start.
- **Edit crontab via nano bisa error-prone**: `Ctrl+K` di nano sempat tidak
  menghapus baris yang dimaksud. Solusi lebih aman: manipulasi crontab
  lewat command line langsung, contoh:
  `crontab -l | grep -v 'pola' | crontab -` untuk hapus baris tertentu, atau
  `(crontab -l; echo 'baris baru') | crontab -` untuk menambah baris.

  