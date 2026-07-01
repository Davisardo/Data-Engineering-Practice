# 1.1 - Getting Started with IDE

**Lab: Pengenalan IDE (Integrated Development Environment)**
Course 3 - Python Project for Data Engineering (IBM Data Engineering Professional Certificate)

Estimasi waktu: 15 menit

## Tujuan Lab Ini

- Mengenal tampilan dan menu-menu di IDE.
- Install package lewat terminal.
- Membuat program Python sederhana.
- Menjalankan program.
- Mengedit kode lalu menjalankannya ulang.

## Struktur Folder

```
1.1 - Getting Started with IDE/
├── README.md
├── welcome.py      # Latihan utama: penjumlahan array -> diubah jadi print pesan
└── software.py     # Latihan tambahan: penjumlahan array pakai Numpy
```

## Apa yang Dikerjakan

1. **Buat file** — buat file `welcome.py`.
2. **Install Numpy** — lewat terminal:
```bash
   python3.11 -m pip install numpy
```
3. **Jalankan program pertama** — kode `welcome.py` awalnya menjumlahkan dua array Numpy:
```bash
   python3.11 welcome.py
```
4. **Edit & jalankan ulang** — isi `welcome.py` diganti jadi kode yang lebih sederhana (print pesan teks biasa), lalu dijalankan lagi.
5. **Latihan tambahan (Practice)** — buat file baru `software.py`, isinya program penjumlahan array Numpy lagi, lalu:
   - Jalankan filenya
   - Ubah salah satu isi array
   - Jalankan ulang, lihat hasilnya berubah

## Catatan Pribadi

Lab ini aslinya dikerjakan di **Skills Network Cloud IDE** (IDE online bawaan IBM). Di sini saya kerjakan ulang secara mandiri pakai **VS Code lokal**, supaya lebih terbiasa dengan environment kerja yang sebenarnya (bukan cuma IDE cloud sekali pakai).