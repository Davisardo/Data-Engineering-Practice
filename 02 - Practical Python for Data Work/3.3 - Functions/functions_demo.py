# ===== 1. Fungsi Dasar =====
def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return b

add(1)
add(2)

# ===== 2. Fungsi dengan 2 parameter =====
def mult(a, b):
    c = a * b
    return c
    print('This is not printed')  # tidak pernah dieksekusi, karena setelah return

result = mult(12, 2)
print(result)

# Fungsi yang sama bisa dipakai untuk tipe data berbeda
print(mult(2, 3))          # integer
print(mult(10.0, 3.14))    # float
print(mult(2, "The BodyGuard "))   # string x integer -> replikasi string

# ===== 3. Local Variable =====
def square(a):
    b = 1              # variabel lokal, cuma ada di dalam fungsi ini
    c = a * a + b
    print(a, "if you square + 1", c)
    return c

x = 3
y = square(x)
print(y)

print(square(2))

# ===== 4. Fungsi tanpa return -> otomatis None =====
def MJ():
    print('The BodyGuard')

def MJ1():
    print('The BodyGuard')
    return None

MJ()
MJ1()

print(MJ())    # None
print(MJ1())   # None

# ===== 5. Fungsi concatenate string =====
def con(a, b):
    return a + b

print(con("This ", "is"))

# ===== 6. Pre-defined Functions =====
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]
print(album_ratings)
print(sum(album_ratings))    # total semua elemen
print(len(album_ratings))    # jumlah elemen

# ===== 7. Built-in Functions dengan Iterable =====
# sum(1, 2) akan ERROR -> harus dalam bentuk tuple/list/set
a = (1, 2)
c = sum(a)
print(f"The sum of the elements in the tuple {a} is {c}.")

a = [1, 2]
c = sum(a)
print(f"The sum of the elements in the list {a} is {c}.")

# ===== 8. If/Else dalam Fungsi =====
def type_of_album(album, year_released):
    print(album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"

x = type_of_album("The BodyGuard", 1980)
print(x)

# ===== 9. Loop dalam Fungsi =====
def print_list(the_list):
    for element in the_list:
        print(element)

print_list(['1', 1, 'the man', "abc"])

# ===== 10. String Comparison dengan 'in' =====
string = "The BodyGuard is the best album"

def check_string(text):
    if text in string:
        return 'String matched'
    else:
        return 'String not matched'

print(check_string("BodyGuard"))
print(check_string("Thriller"))

# ===== 11. String Comparison dengan == =====
def compare_strings(x, y):
    if x == y:
        return 1
    else:
        return 0

string1 = "The BodyGuard is the best album"
string2 = "The BodyGuard is the best album"
print(compare_strings(string1, string2))

# ===== 12. Default Argument Value =====
def is_good_rating(rating=4):
    if rating < 7:
        print("this album sucks it's rating is", rating)
    else:
        print("this album is good its rating is", rating)

is_good_rating()      # pakai default (4)
is_good_rating(10)    # override default

# ===== 13. Local Variable, tidak bisa diakses di luar fungsi =====
album = "The BodyGuard"

def printer1(album):
    internal_var1 = "Thriller"
    print(album, "is an album")

printer1(album)
# print(internal_var1)  # akan ERROR, internal_var1 cuma ada di dalam fungsi

# ===== 14. Membuat variabel global dari dalam fungsi (pakai kata kunci global) =====
album = "The BodyGuard"

def printer(album):
    global internal_var
    internal_var = "Thriller"
    print(album, "is an album")

printer(album)
print(internal_var)   # sekarang bisa diakses, karena sudah dideklarasi global

# ===== 15. Scope Variable =====
my_favourite_band = "AC/DC"

def get_band_rating(bandname):
    if bandname == my_favourite_band:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", get_band_rating("AC/DC"))
print("Deep Purple's rating is:", get_band_rating("Deep Purple"))
print("My favourite band is:", my_favourite_band)

# ===== 16. Local variable dengan nama sama, tidak konflik dengan global =====
def get_band_rating2(bandname):
    my_favourite_band = "Deep Purple"   # ini LOKAL, beda dari global di atas
    if bandname == my_favourite_band:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", get_band_rating2("AC/DC"))       # 0.0, karena lokal = Deep Purple
print("Deep Purple's rating is:", get_band_rating2("Deep Purple"))  # 10.0
print("My favourite band is still:", my_favourite_band)       # tetap AC/DC (global tidak berubah)

# ===== 17. *args - jumlah argumen tidak pasti, dibungkus tuple =====
def print_all(*args):
    print("No of arguments:", len(args))
    for argument in args:
        print(argument)

print_all('Horsefeather', 'Adonis', 'Bone')
print_all('Sidecar', 'Long Island', 'Mudslide', 'Carriage')

# ===== 18. **kwargs - keyword argument tidak pasti, dibungkus dict =====
def print_dictionary(**args):
    for key in args:
        print(key + " : " + args[key])

print_dictionary(Country='Canada', Province='Ontario', City='Toronto')

# ===== 19. Passing list ke fungsi = passing by reference (mutable!) =====
def add_items(the_list):
    the_list.append("Three")
    the_list.append("Four")

my_list = ["One", "Two"]
add_items(my_list)
print(my_list)   # list asli IKUT BERUBAH, karena reference sama

# ===== 20. Quiz: Functions =====

def div(a, b):
    return a / b

print(div(10, 2))

def con(a, b):
    return a + b

print(con(2, 2))                # bisa untuk angka
print(con(['a', 1], ['b', 1]))  # bisa untuk list juga

# Hitung kemunculan kata "little" dalam string
def freq(string, passedkey):
    words = string.split()
    count = 0
    for word in words:
        if word.lower().strip('.,') == passedkey.lower():
            count += 1
    return count

text = ("Mary had a little lamb Little lamb, little lamb Mary had a little lamb."
        "Its fleece was white as snow And everywhere that Mary went "
        "Mary went, Mary went Everywhere that Mary went The lamb was sure to go")
print(freq(text, "little"))
