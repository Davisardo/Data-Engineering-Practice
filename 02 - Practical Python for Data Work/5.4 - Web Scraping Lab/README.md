# 5.4 - Web Scraping Lab

**Hands-on Lab: Web Scraping Lab**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 5 - APIs and Data Collection

## Tujuan Lab Ini

- Familiar dengan dasar-dasar library `BeautifulSoup`.
- Bisa scraping halaman web untuk data dan filter datanya.

## Struktur Folder

5.4 - Web Scraping Lab/
└── web_scraping_lab.ipynb

## Materi yang Dipelajari

1. **BeautifulSoup Object** — `BeautifulSoup(html, 'html5lib')`, `prettify()` untuk lihat struktur.
2. **Tags** — akses elemen lewat nama tag (`soup.title`, `soup.h3`), otomatis ambil elemen pertama kalau ada duplikat nama tag.
3. **Tree Navigation** — `parent`, child (`tag.b`), `next_sibling`.
4. **HTML Attributes** — akses seperti dictionary (`tag['id']`), `.attrs`, `.get('id')`.
5. **Navigable String** — teks di dalam tag, bisa dikonversi ke string Python biasa.
6. **find_all()** — filter berdasarkan nama tag, list nama tag, attribute, string isi.
7. **find()** — cari elemen **pertama** saja, termasuk filter pakai `class_` (underscore karena `class` keyword Python).
8. **Scraping halaman nyata** — download & parse HTML asli (IBM.com), scrape semua link dan gambar.
9. **Scraping tabel HTML** — iterasi `<tr>`/`<td>` manual, sama seperti fungsi `extract()` di lab-lab ETL sebelumnya.
10. **`pd.read_html()`** — shortcut Pandas untuk scraping tabel dalam 1 baris kode, alternatif jauh lebih ringkas dari BeautifulSoup manual.

## Cara Menjalankan

Buka `web_scraping_lab.ipynb` di VS Code (Jupyter extension), jalankan tiap cell dengan `Shift+Enter`.

Dependency:

pip install bs4 html5lib lxml requests pandas

## Catatan Teknis: Whitespace & next_sibling

Saat HTML ditulis manual dengan banyak baris (pakai backslash continuation), `next_sibling` bisa menangkap **whitespace kosong** di antara tag, bukan langsung tag berikutnya — perlu dipanggil berkali-kali untuk "melompati" whitespace, dan jumlahnya tidak selalu terprediksi.

**Solusi lebih robust:** pakai `find_next(nama_tag)`, yang otomatis mencari tag target berikutnya **tanpa peduli whitespace di antaranya**:
```python
salary_lebron = tag_object.find_next('p')   # lebih aman dari next_sibling berulang
```

## Cheat Sheet: BeautifulSoup vs pd.read_html() — Kapan Pakai yang Mana

| | BeautifulSoup manual | `pd.read_html()` |
|---|---|---|
| Kontrol | Penuh — bisa filter kondisi kompleks, ambil bukan-cuma-tabel (link, gambar, dst) | Terbatas — cuma untuk tabel HTML |
| Kecepatan development | Lambat, banyak baris kode | Sangat cepat, 1 baris |
| Kapan dipakai | Data campuran (teks + tabel + link), butuh filter spesifik, atau tabel dengan struktur tidak standar | Tabel HTML standar, butuh cepat, tidak perlu customisasi |

**Pola scraping tabel manual (BeautifulSoup) — persis yang dipakai di lab ETL sebelumnya (GDP, Banks):**
```python
table = soup.find('table')
for row in table.find_all('tr'):
    cols = row.find_all('td')
    if len(cols) >= 4:   # skip baris header/kosong
        data = cols[2].string
```

---

## Reading: Web Scraping and HTML Basics

Materi reading yang mendahului lab ini, memberi konteks konseptual sebelum praktik.

### Cara Kerja Web Scraping (Alur Umum)

1. **HTTP Request** — scraper kirim GET request ke URL target.
2. **Web Page Retrieval** — server mengembalikan konten HTML mentah.
3. **HTML Parsing** — HTML dipecah jadi komponen (tag, attribute, teks) pakai BeautifulSoup.
4. **Data Extraction** — cari & ambil data spesifik lewat tag/attribute/pattern.
5. **Data Transformation** — bersihkan data (hapus tag HTML, konversi format).
6. **Storage** — simpan hasil ke database, CSV, JSON, dst.
7. **Automation** — otomatisasi lewat script untuk scraping berulang dari banyak halaman.

### Struktur HTML Dasar

- `<html>` — elemen root halaman.
- `<head>` — meta-informasi halaman.
- `<body>` — konten yang ditampilkan (biasanya yang di-scrape).
- `<h3>` — heading tipe 3 (dipakai untuk nama pemain di contoh lab).
- `<p>` — paragraf (dipakai untuk info gaji di contoh lab).

### HTML Document Tree

HTML divisualisasikan sebagai **tree** dengan tag sebagai node — tag bisa berisi string dan tag lain (jadi **child**-nya), sementara tag dalam parent yang sama disebut **sibling**. Contoh: `<head>` dan `<body>` adalah children dari `<html>`, sekaligus sibling satu sama lain.

### Struktur Tabel HTML

- `<table>` — mendefinisikan tabel.
- `<tr>` — table row (baris).
- `<th>` — table header (baris pertama biasanya).
- `<td>` — table data/cell (isi tiap sel).

**Relevansi ke praktik di atas:** semua konsep tree ini (parent/child/sibling) langsung dipraktikkan di bagian "Tree Navigation" lab hands-on, dan struktur tabel HTML ini persis yang dipakai di bagian "Scraping Data dari Tabel HTML" dan fungsi `extract()` di project-project ETL sebelumnya.

## Catatan Pribadi

Lab ini menutup lingkaran pemahaman: sejak awal course, fungsi `extract()` di berbagai project ETL (GDP, World's Largest Banks) selalu memakai pola `tables[n].find_all('tr')` tanpa penjelasan detail *kenapa* pola itu bekerja. Lab ini akhirnya membongkar detail di baliknya — bagaimana BeautifulSoup merepresentasikan HTML sebagai tree, dan kenapa navigasi lewat `find_all()`/`find()` jauh lebih reliable dibanding `next_sibling` manual yang rentan whitespace.