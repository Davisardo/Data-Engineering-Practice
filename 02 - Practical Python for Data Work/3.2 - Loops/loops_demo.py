# ===== 1. Range =====
print(range(3))   # range object, bukan list (beda dari Python 2)

# ===== 2. For Loop - akses via index =====
dates = [1982, 1980, 1973]
N = len(dates)

for i in range(N):
    print(dates[i])

# ===== 3. For Loop - contoh sederhana range =====
for i in range(0, 8):
    print(i)

# ===== 4. For Loop - akses langsung elemen list =====
for year in dates:
    print(year)

# ===== 5. Mengubah elemen list lewat loop =====
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range(0, 5):
    print("Before square", i, "is", squares[i])
    squares[i] = 'white'
    print("After square", i, "is", squares[i])

# ===== 6. enumerate() - akses index & value sekaligus =====
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)

# ===== 7. While Loop =====
dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while year != 1973:
    print(year)
    i = i + 1
    year = dates[i]

print("It took", i, "repetitions to get out of loop.")

# ===== 8. break =====
for num in range(1, 10):
    if num == 5:
        print("Breaking the loop at:", num)
        break
    print(num)

# ===== 9. continue =====
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# ===== 10. break + continue di while loop =====
count = 0
while count < 10:
    count += 1
    if count == 3:
        continue   # skip cetak angka 3
    if count == 8:
        break        # berhenti total di angka 8
    print(count)

# ===== 11. Quiz: Loops =====

# Print angka -5 sampai 5
for i in range(-5, 6):
    print(i)

# Print elemen list Genres
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)

# Print elemen list squares
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)

# While loop: print rating selama >= 6
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
Rating = PlayListRatings[0]
while i < len(PlayListRatings) and Rating >= 6:
    print(Rating)
    i = i + 1
    Rating = PlayListRatings[i]

# While loop: copy 'orange' sampai ketemu yang bukan 'orange'
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while i < len(squares) and squares[i] == 'orange':
    new_squares.append(squares[i])
    i = i + 1
print(new_squares)

# For loop: print 1-15, skip kelipatan 3, stop kalau > 12
for i in range(1, 16):
    if i % 3 == 0:
        continue   # skip kelipatan 3
    if i > 12:
        break        # stop kalau lebih dari 12
    print(i)