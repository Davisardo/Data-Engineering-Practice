def mean(numbers):
    """Mengembalikan rata-rata dari daftar angka yang diberikan."""
    return sum(numbers) / len(numbers)


def median(numbers):
    """Mengembalikan nilai tengah (median) dari daftar angka yang diberikan."""
    numbers.sort()

    if len(numbers) % 2 == 0:
        # jumlah data genap -> rata-rata dari dua nilai tengah
        median1 = numbers[len(numbers) // 2]
        median2 = numbers[len(numbers) // 2 - 1]
        mymedian = (median1 + median2) / 2
    else:
        # jumlah data ganjil -> nilai tengah langsung
        mymedian = numbers[len(numbers) // 2]

    return mymedian
