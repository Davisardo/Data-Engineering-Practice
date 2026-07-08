# 3.1 - Conditions and Branching

**Lab: Conditions and Branching**
Course 02 - Practical Python for Data Work (IBM Data Engineering Professional Certificate)
Module 3 - Python Programming Fundamentals

## Tujuan Lab Ini

- Bekerja dengan conditions dan branching (if/elif/else).

## Struktur Folder

3.1 - Conditions and Branching/
└── conditions_demo.py

## Materi yang Dipelajari

1. **Comparison Operators** — `==`, `!=`, `>`, `<`, `>=`, `<=`, bisa dipakai untuk angka, string, bahkan karakter (dibandingkan berdasarkan nilai ASCII).
2. **Branching** — `if`, `if-else`, `if-elif-else` untuk menjalankan blok kode berbeda tergantung kondisi.
3. **Logical Operators** — `and` (True kalau kedua kondisi True), `or` (True kalau salah satu True), `not` (membalik nilai boolean).

## Cara Menjalankan

python conditions_demo.py

## Cheat Sheet: Conditional Logic untuk Data Engineering

**Kenapa krusial:** conditional logic adalah dasar dari **data validation & cleaning** — hampir semua fungsi cleaning di project ETL (seperti yang sudah dikerjakan di lab-lab sebelumnya) internalnya menggunakan if/else untuk memfilter baris valid/invalid.

**Kaitan dengan Pandas (akan dipakai nanti):**
```python
# Kondisi biasa (Python murni)
if (age > 18) and (age < 65):
    ...

# Setara di Pandas (operator beda: & bukan and, | bukan or)
df[(df['age'] > 18) & (df['age'] < 65)]
```
Alasan bedanya: Python `and`/`or` bekerja per nilai tunggal, sementara Pandas butuh operator per-elemen (`&`, `|`) karena bekerja di banyak baris sekaligus (vectorized operation). Ini detail penting yang sering bikin error pemula saat pindah dari Python murni ke Pandas.

**Pola umum di data cleaning:**
```python
# Validasi baris data sebelum masuk pipeline
if row['price'] < 0 or row['quantity'] is None:
    # skip / log sebagai data invalid
    continue
```

**Perbandingan string/karakter:** perbandingan `>`/`<` pada string dilakukan berdasarkan **urutan ASCII**, huruf kapital dan huruf kecil punya kode berbeda (case-sensitive) — penting diingat saat membandingkan atau mengurutkan data teks.

## Catatan Pribadi

Poin penting: kode setelah blok `if` (di luar indentasi) **selalu jalan**, terlepas dari kondisi True/False — hanya kode **di dalam** indentasi yang bersyarat. Ini konsep dasar yang harus benar-benar dipahami sebelum lanjut ke loop dan fungsi.

## Reading: Real-World Examples of Conditions & Branching

Materi reading tambahan dari course, memberikan konteks penerapan nyata dari konsep yang sudah dipraktikkan di atas.

### ELIF — Contoh ATM
Branching bertingkat dipakai saat sistem punya lebih dari 2 kemungkinan jalur keputusan.
```python
user_choice = "Withdraw Cash"
if user_choice == "Withdraw Cash":
    amount = int(input("Enter the amount to withdraw: "))
    if amount % 10 == 0:
        print("Amount dispensed: ", amount)
    else:
        print("Please enter a multiple of 10.")
else:
    print("Thank you for using the ATM.")
```

### NOT — Contoh Notification Settings
```python
is_do_not_disturb = True
if not is_do_not_disturb:
    send_notification("New message received")
```
Analoginya: notifikasi hanya dikirim kalau kondisi "Do Not Disturb" **tidak** aktif.

### AND — Contoh Access Control
Dipakai saat semua syarat **wajib** terpenuhi sekaligus (mirip validasi data yang butuh beberapa kolom valid bersamaan).
```python
has_valid_id_card = True
has_matching_fingerprint = True
if has_valid_id_card and has_matching_fingerprint:
    open_high_security_door()
```

### OR — Contoh Movie Night
Dipakai saat **cukup satu saja** dari beberapa syarat terpenuhi.
```python
friend1_likes_comedy = True
friend2_likes_action = False
friend3_likes_drama = False
if friend1_likes_comedy or friend2_likes_action or friend3_likes_drama:
    choose_a_movie()
```

**Relevansi ke data engineering:** pola `AND` ini persis dipakai saat validasi data butuh banyak syarat sekaligus (misal: `if row['id'] is not None and row['date'] is not None and row['amount'] > 0:`), sementara `OR` cocok untuk deteksi anomali di mana **salah satu** kondisi error saja sudah cukup untuk menandai baris sebagai invalid.