"""Modul ini mendemonstrasikan operasi penjumlahan sederhana menggunakan fungsi bantu."""


def add(number1, number2):
    """Mengembalikan hasil penjumlahan number1 dan number2."""
    return number1 + number2


NUM1 = 4  # konstanta pertama
NUM2 = 5  # konstanta kedua
TOTAL = add(NUM1, NUM2)  # panggil fungsi add, simpan hasilnya

print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
