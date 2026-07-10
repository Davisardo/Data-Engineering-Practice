## Catatan Teknis: Kendala & Solusi

**Masalah 1 — URL Excel 404 Not Found:** URL asli file Excel di instruksi lab adalah path internal khusus JupyterLite (environment browser Skills Network), tidak bisa diakses langsung dari luar. **Solusi:** generate file Excel sendiri dari data CSV yang berhasil dimuat, pakai `df.to_excel()`.

**Masalah 2 — `!pip install` gagal masuk ke kernel yang benar:** Perintah `!pip install` di beberapa kasus menginstall ke Python environment yang berbeda dari kernel notebook yang aktif. **Solusi:** pakai `%pip install` (magic command Jupyter) yang menjamin instalasi tepat ke kernel yang sedang dipakai, lalu restart kernel setelah instalasi.

**Masalah 3 — `externally-managed-environment`:** Python di sistem ini dikelola oleh `uv`, yang membatasi instalasi package langsung demi keamanan sistem. **Solusi:** tambahkan flag `--break-system-packages` untuk override pembatasan ini (aman untuk package tambahan seperti `openpyxl`, bukan modifikasi sistem inti).

## Cheat Sheet: Membaca Berbagai Format File

**Kenapa penting:** di dunia nyata, data engineer sering menerima data dalam format berbeda-beda tergantung sumbernya (tim finance biasanya kirim Excel, tim engineering biasanya CSV/JSON, sistem legacy kadang masih pakai format lain).

```python
df = pd.read_csv('file.csv')       # CSV
df = pd.read_excel('file.xlsx')     # Excel
df = pd.read_json('file.json')      # JSON
df = pd.read_sql(query, connection)   # Database (butuh koneksi SQL)
```

Semua fungsi `read_*` ini menghasilkan struktur yang sama (DataFrame), jadi setelah data termuat, seluruh teknik seleksi/manipulasi (`loc`, `iloc`, slicing) berlaku sama, terlepas dari format sumbernya.

## Catatan Pribadi

Kendala teknis di lab ini (URL 404, environment `uv` yang restriktif) justru jadi latihan nyata debugging di dunia kerja — instruksi lab sering ditulis untuk environment tertentu (dalam kasus ini JupyterLite), dan menyesuaikannya ke environment lokal sendiri adalah skill yang penting dikuasai data engineer.