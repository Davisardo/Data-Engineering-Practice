## Hasil Akhir

| Country | GDP (Billion USD) |
|---|---|
| United States | 26854.60 |
| China | 19373.59 |
| Japan | 4409.74 |
| Germany | 4308.85 |
| India | 3736.88 |
| United Kingdom | 3158.94 |
| France | 2923.49 |
| Italy | 2169.74 |
| Canada | 2089.67 |
| Brazil | 2081.24 |

## Perbandingan dengan Project ETL GDP Sebelumnya

Project ini secara skenario **identik** dengan lab ETL GDP yang dikerjakan jauh sebelumnya (Course 03 - Python Fundamentals, lab 2.1), dengan hasil angka yang sama persis — tapi pendekatannya jauh berbeda:

| Aspek | ETL GDP (Course 03) | Practice Project ini |
|---|---|---|
| Ekstraksi tabel | BeautifulSoup manual — `find_all('tbody')`, loop `tr`/`td`, filter baris manual | `pd.read_html(URL)` — 1 baris kode, otomatis jadi DataFrame |
| Filter baris tidak valid | Cek manual `col[0].find('a')` dan tanda `—` | Slicing langsung `.iloc[1:11, :]` karena tabel sudah bersih dari `read_html` |
| Baris kode total | ~20 baris untuk extract | ~8 baris untuk extract |

**Insight penting:** `pd.read_html()` bekerja sangat baik untuk tabel HTML **standar** yang terstruktur rapi, tapi BeautifulSoup manual tetap dibutuhkan untuk kasus yang lebih kompleks — data campuran (bukan cuma tabel), filter kondisi rumit, atau struktur HTML tidak standar. Kemampuan memilih pendekatan yang tepat (bukan selalu pakai yang "tercepat") adalah tanda kematangan skill data engineering.

## Catatan Pribadi

Project ini terasa seperti "ujian akhir" tersirat untuk skill web scraping — bisa menyelesaikan tugas yang sama dengan hasil identik, tapi dengan pemahaman yang jauh lebih dalam tentang *kapan* harus pakai pendekatan manual (kontrol penuh) vs shortcut (`read_html`, efisiensi). Progres dari BeautifulSoup manual ke `pd.read_html()` yang percaya diri adalah bukti nyata pertumbuhan pemahaman selama course ini.
