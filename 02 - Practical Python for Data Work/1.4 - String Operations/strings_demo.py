# ===== 1. Dasar String =====
print("The BodyGuard")  # kutip ganda
print("The BodyGuard")  # kutip tunggal
print("1 2 3 4 5 6 ")  # spasi & angka
print("@#2_#]&*^%$")  # karakter spesial

name = "The BodyGuard"
print(name)

# ===== 2. Indexing =====
print(name[0])  # elemen pertama
print(name[6])
print(name[10])
print(name[-1])  # elemen terakhir
print(name[-13])  # elemen pertama dari belakang
print(len("The BodyGuard"))  # panjang string

# ===== 3. Slicing & Stride =====
print(name[0:4])  # index 0-3
print(name[8:12])  # index 8-11
print(name[::2])  # tiap 2 elemen
print(name[0:5:2])  # slicing + stride

# ===== 4. Concatenate & Replikasi =====
statement = name + " is the best album"
print(statement)
print(3 * "The BodyGuard")  # ulangi 3x

name = "The BodyGuard"
name = name + " is the best album"  # overwrite
print(name)

# ===== 5. Escape Sequences =====
print(" The BodyGuard\n is the best album")  # \n baris baru
print(" The BodyGuard \t is the best album")  # \t tab
print(" The BodyGuard \\ is the best album")  # \\ satu backslash
print(r" The BodyGuard \ is the best album")  # raw string

# ===== 6. Method upper/replace/find/split =====
a = "Thriller is the sixth studio album"
print("before upper:", a)
print("After upper:", a.upper())

a = "The BodyGuard is the best album"
print(a.replace("BodyGuard", "Janet"))

name = "The BodyGuard"
print(name.find("he"))  # ketemu
print(name.find("Guard"))  # ketemu
print(name.find("Jasdfasdasdf"))  # tidak ketemu -> -1
print(name.split())

# ===== 7. RegEx =====
import re

s1 = "The BodyGuard is the best album"
result = re.search(r"Body", s1)
print("Match found!" if result else "Match not found.")

text = "My Phone number is 1234567890"
match = re.search(r"\d\d\d\d\d\d\d\d\d\d", text)  # 10 digit
print("Phone number found:", match.group() if match else "No match")

text2 = "Hello, world!"
print("Matches:", re.findall(r"\W", text2))  # karakter non-word

s2 = "The BodyGuard is the best album of 'Whitney Houston'."
print(re.findall("st", s2))
print(re.split(r"\s", s2))
print(re.sub(r"Whitney Houston", "legend", s2, flags=re.IGNORECASE))

# ===== 8. Quiz =====
a, b = "1", "2"
c = a + b
print(c)  # "12" -> ini concat string, bukan penjumlahan angka

d = "ABCDEFG"
print(d[:3])

e = "clocrkr1e1c1t"
print(e[::2])

print(r"\\")  # cetak backslash

f = "You are wrong"
print(f.upper())

f2 = "YOU ARE RIGHT"
print(f2.lower())

g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"

print(g.find("snow"))
print(g.replace("Mary", "Bob"))
print(g.replace(",", "."))
print(g.split())

s3 = "House number- 1105"
result = re.search(r"\d", s3)
print("Digit found" if result else "Digit not found.")

str1 = "The quick brown fox jumps over the lazy dog."
print(re.sub(r"fox", "bear", str1))

str2 = "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
print(re.findall(r"woo", str2))
