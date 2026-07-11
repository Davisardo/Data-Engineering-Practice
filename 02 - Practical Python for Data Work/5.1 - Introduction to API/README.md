# 5.1 - Introduction to API

**Hands-on Lab: Introduction to API**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 5 - APIs and Data Collection

## Tujuan Lab Ini

- Memahami konsep dasar API.
- Memahami Pandas sebagai contoh API.
- Menggunakan REST API nyata (NBA API) untuk mengambil dan menganalisis data.

## Struktur Folder

5.1 - Introduction to API/
└── intro_api.ipynb

## Materi yang Dipelajari

1. **Konsep API secara umum** — dua software berkomunikasi tanpa perlu tahu detail implementasi internal, cukup tahu input & output.
2. **Pandas sebagai API** — `df.mean()`, `df.head()` adalah "komunikasi" dengan API Pandas; banyak bagian implementasinya bahkan bukan Python murni (C, Cython).
3. **REST API** — komunikasi lewat HTTP request/response, biasanya berformat JSON.
4. **NBA API** — contoh REST API nyata, mengambil data tim & pertandingan NBA.
5. **Conditional filtering pertama kali dipraktikkan nyata** — `df[df['nickname'] == 'Warriors']`.
6. **Analisis performa home vs away** — filter, hitung rata-rata (`mean()`), dan visualisasi tren (`plot()`).

## Cara Menjalankan

Buka `intro_api.ipynb` di VS Code (Jupyter extension), jalankan tiap cell dengan `Shift+Enter`.

Dependency:

pip install pandas matplotlib nba_api

## Catatan Teknis Menarik

**Data real-time, bukan data statis lab:** instruksi lab asli mencatat bahwa `stats.nba.com` memblokir request dari Cloud IP (dipakai Skills Network Labs), sehingga disediakan file `.pkl` statis sebagai alternatif. Karena dikerjakan dari **komputer lokal** (bukan cloud), request API berhasil langsung tanpa hambatan — hasilnya data pertandingan Warriors yang **benar-benar terbaru** (musim 2025-2026), bukan data lama dari file statis lab.

**Penyesuaian kode:** karena data yang didapat berbeda periode waktu dari lab asli, dilakukan pengecekan otomatis (`set intersection` antara tim lawan home & away) untuk memastikan tim lawan yang dipilih (Toronto Raptors) memang punya data pertandingan home maupun away yang cukup untuk dianalisis.

## Hasil Analisis

| Metrik | Home (vs TOR) | Away (vs TOR) |
|---|---|---|
| Jumlah pertandingan | 32 | 32 |
| Rata-rata PLUS_MINUS | +2.41 | -2.31 |
| Rata-rata PTS | 110.19 | 105.31 |

**Kesimpulan:** Golden State Warriors secara historis bermain lebih baik saat menjadi tuan rumah melawan Toronto Raptors, baik dari segi selisih skor (PLUS_MINUS) maupun total poin yang dicetak.

## Cheat Sheet: API untuk Data Engineering

**Kenapa krusial:** REST API adalah **sumber data paling umum** di data engineering modern — jauh lebih fleksibel daripada file statis (CSV/Excel) karena datanya selalu ter-update dan bisa di-query sesuai kebutuhan spesifik.

**Pola umum request API dengan `requests`:**
```python
import requests

response = requests.get(url)
if response.status_code == 200:   # 200 = sukses
    data = response.json()          # ubah response JSON jadi dict/list Python
else:
    print(f"Request gagal: {response.status_code}")
```

**Kaitan dengan lab-lab ETL sebelumnya:** fungsi `extract()` di project ETL (2.1, 2.2, Final Project) yang pakai `requests.get(url).text` untuk web scraping sebenarnya konsep yang sama — bedanya, API mengembalikan data terstruktur (JSON) langsung, sementara web scraping harus mem-parsing HTML mentah.

**Rate limiting & pemblokiran API — pelajaran nyata dari lab ini:** banyak API publik membatasi/memblokir request dari IP tertentu (misal cloud provider) untuk mencegah penyalahgunaan. Data engineer perlu siap dengan strategi alternatif (caching data, file backup, retry dengan delay) saat API tidak bisa diakses langsung.

## Catatan Pribadi

Lab ini jadi bukti nyata perbedaan antara *belajar dari data statis* vs *bekerja dengan data live* — instruksi lab yang ditulis untuk 1 titik waktu tertentu (data lama) perlu disesuaikan logikanya (bukan cuma dijalankan mentah-mentah) ketika sumber datanya sudah berubah seiring waktu. Ini skill penting untuk data engineer nyata: kode yang robust harus bisa beradaptasi dengan perubahan data, bukan cuma bekerja untuk 1 snapshot data tertentu.