# 3.6 - Practice Lab Text Analysis

**Practice Lab: Text Analysis**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 3 - Python Programming Fundamentals

## Skenario

Menganalisis feedback pelanggan dalam bentuk string, mengekstrak informasi berguna lewat 3 task: format teks jadi lowercase (tanpa tanda baca), hitung frekuensi semua kata unik, dan hitung frekuensi kata tertentu.

## Tujuan Lab Ini

- Menggunakan Python untuk melakukan text analysis.
- Mengubah teks jadi lowercase, lalu menghitung frekuensi semua kata unik maupun kata tertentu.

## Struktur Folder

3.6 - Practice Lab Text Analysis/
└── text_analyzer.py

## Materi yang Dipelajari

Practice lab ini menggabungkan 3 konsep dari lab-lab sebelumnya dalam 1 skenario nyata:
- **List** — hasil `split()` teks jadi list kata.
- **String** — `lower()`, `replace()`, `split()` untuk preprocessing teks.
- **Class & Object** — `TextAnalyzer` membungkus data (`fmtText`) dan behavior (`freq_all()`, `freq_of()`) dalam satu unit.

### Alur Class TextAnalyzer

1. **Constructor (`__init__`)** — terima teks mentah, hapus tanda baca (`.`, `!`, `,`, `?`), ubah jadi lowercase, simpan sebagai `self.fmtText`.
2. **`freq_all()`** — pecah `fmtText` jadi list kata, hitung kemunculan tiap kata unik, kembalikan sebagai dictionary.
3. **`freq_of(word)`** — panggil `freq_all()`, cek apakah kata yang dicari ada di dictionary; kembalikan 0 kalau tidak ditemukan (bukan error).

## Cara Menjalankan

python text_analyzer.py

## Cheat Sheet: Text Analysis untuk Data Engineering

**Kenapa relevan:** preprocessing teks (lowercase, hapus tanda baca, tokenisasi/split kata) adalah langkah **wajib** sebelum data teks siap dipakai untuk analisis lanjutan — sentiment analysis, deteksi kata kunci, atau word cloud. Pola di lab ini adalah versi sederhana dari **NLP (Natural Language Processing) preprocessing pipeline**.

**Pola penting: `freq_of()` return 0, bukan error/None**
```python
def freq_of(self, word):
    freq_map = self.freq_all()
    if word in freq_map:
        return freq_map[word]
    else:
        return 0   # bukan error, bukan None -> aman dipakai langsung untuk kalkulasi
```
Ini best practice: fungsi pencarian sebaiknya kembalikan nilai default yang "aman" (0 untuk hitungan, string kosong untuk teks) daripada `None` atau exception, supaya kode yang memanggilnya tidak perlu selalu cek exception di setiap pemanggilan.

**Perbandingan dengan tool NLP nyata:** apa yang dilakukan `freq_all()` secara manual ini persis fungsi `Counter` dari modul `collections` Python, atau `CountVectorizer` di library `scikit-learn` — versi production biasanya lebih optimal dan punya fitur tambahan (stopword removal, stemming), tapi prinsip dasarnya sama seperti yang baru dibangun di lab ini.

## Catatan Pribadi

Baris `for word in set(word_list):` di `freq_all()` adalah optimasi kecil tapi penting — tanpa `set()`, kata yang sama akan dihitung berkali-kali secara redundan (misal "diam" muncul 5x akan memicu `word_list.count("diam")` sebanyak 5x juga). Pakai `set()` memastikan tiap kata unik cuma dihitung sekali, menghubungkan kembali konsep set dari lab 2.4 dengan skenario nyata.