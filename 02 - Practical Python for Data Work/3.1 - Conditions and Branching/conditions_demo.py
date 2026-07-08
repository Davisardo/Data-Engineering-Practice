# ===== 1. Comparison Operators =====
a = 5
print(a == 6)   # False

i = 6
print(i > 5)    # True

i = 2
print(i > 5)    # False

i = 2
print(i != 6)   # True

i = 6
print(i != 6)   # False

# Perbandingan string
print("ACDC" == "The Bodyguard")   # False
print("ACDC" != "The Bodyguard")   # True

# Perbandingan karakter berdasarkan ASCII
print('B' > 'A')     # True, B(66) > A(65)
print('BA' > 'AB')   # True, huruf pertama diprioritaskan

# ===== 2. If Statement =====
age = 19
if age > 18:
    print("you can enter")
print("move on")

# ===== 3. If-Else Statement =====
age = 18
if age > 18:
    print("you can enter")
else:
    print("go see Meat Loaf")
print("move on")

# ===== 4. If-Elif-Else Statement =====
age = 18
if age > 18:
    print("you can enter")
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf")
print("move on")

# ===== 5. Contoh lain =====
album_year = 1983
if album_year > 1980:
    print("Album year is greater than 1980")
print('do something..')

album_year = 1970
if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")
print('do something..')

# ===== 6. Logical Operators =====

# AND: True hanya jika KEDUA kondisi True
album_year = 1980
if (album_year > 1979) and (album_year < 1990):
    print("Album year was in between 1980 and 1989")
print("Do Stuff..")

# OR: True jika SALAH SATU kondisi True
album_year = 1990
if (album_year < 1980) or (album_year > 1989):
    print("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's")

# NOT: membalik nilai boolean
album_year = 1983
if not (album_year == 1984):
    print("Album year is not 1984")

# ===== 7. Quiz: Conditions =====

# Cek achievement Lionel Messi > 10
player_name = "Lionel Messi"
sport = "Soccer"
achievements = 7

if achievements > 10:
    print(f"{player_name} plays {sport} and has {achievements} achievements.")
else:
    print(f"{player_name} does not have more than 10 achievements.")

# Cek sport Tennis ATAU achievement == 20
player_name = "Roger Federer"
sport = "Tennis"
achievements = 20

if sport == "Tennis" or achievements == 20:
    print(f"{player_name} meets the criteria! They play {sport} and have {achievements} achievements.")
else:
    print(f"{player_name} does not meet the criteria.")

# Cek achievement < 10 DAN bukan Soccer
player_name = "Usain Bolt"
sport = "Athletics"
achievements = 8

if achievements < 10 and sport != "Soccer":
    print(f"{player_name} plays {sport} and has only {achievements} achievements.")
else:
    print(f"{player_name} does not meet the criteria.")