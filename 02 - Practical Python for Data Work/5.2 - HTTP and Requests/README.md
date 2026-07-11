## Cheat Sheet: HTTP Status Codes

| Range | Arti | Contoh |
|---|---|---|
| 1xx | Informational | Request diterima, proses berlanjut |
| 2xx | Success | 200 OK — request berhasil |
| 3xx | Redirection | 301 Moved Permanently |
| 4xx | Client Error | 404 Not Found, 401 Unauthorized |
| 5xx | Server Error | 500 Internal Server Error |

## Cheat Sheet: Requests untuk Data Engineering

**Kenapa krusial:** ini fondasi teknis di balik **semua** lab pengambilan data dari web sejauh course ini — web scraping (lab ETL GDP, Banks), REST API (lab 5.1 NBA), semuanya pakai library `requests` yang sama.

**Pola dasar GET request:**
```python
r = requests.get(url)
if r.status_code == 200:
    data = r.json()   # kalau response JSON
else:
    print(f"Request gagal: {r.status_code}")
```

**GET dengan parameter — jauh lebih efisien dari download semua lalu filter manual:**
```python
payload = {"category": "electronics", "limit": 50}
r = requests.get(api_url, params=payload)
# otomatis jadi: api_url?category=electronics&limit=50
```

**Kapan pakai GET vs POST di real API:**

| | GET | POST |
|---|---|---|
| Data terkirim di | URL (query string) | Request body |
| Terlihat di URL/history | Ya | Tidak |
| Ukuran data | Terbatas | Bisa lebih besar |
| Kegunaan umum | Mengambil/query data | Mengirim data baru (form, login, upload) |

**Download file binary (gambar, PDF, dst):**
```python
r = requests.get(file_url)
with open('output.png', 'wb') as f:   # 'wb' wajib untuk file non-teks
    f.write(r.content)   # .content untuk binary, bukan .text
```

## Catatan Pribadi

Perbedaan `.text` vs `.content` sering jadi sumber bug: `.text` untuk konten teks (HTML, JSON as string), `.content` untuk data binary mentah (gambar, PDF, file terkompresi) — kalau salah pilih saat menyimpan gambar pakai `.text`, hasilnya akan corrupt/rusak.