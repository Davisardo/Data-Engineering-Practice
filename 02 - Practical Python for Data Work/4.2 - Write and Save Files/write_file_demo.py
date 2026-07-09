# ===== 1. Menulis 1 baris ke file =====
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# ===== 2. Menulis beberapa baris =====
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# ===== 3. Menulis list of string ke file =====
lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

with open(exmp2, 'w') as writefile:
    for line in lines:
        print(line)
        writefile.write(line)

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# ===== 4. Peringatan: mode 'w' MENIMPA semua isi lama =====
with open(exmp2, 'w') as writefile:
    writefile.write("Overwrite\n")

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# ===== 5. Append - tambah baris tanpa hapus data lama =====
with open(exmp2, 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# ===== 6. Mode a+ =====
with open(exmp2, 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())   # kosong! karena posisi cursor sudah di akhir file

# ===== 7. tell() - cek posisi cursor saat ini =====
with open(exmp2, 'a+') as testwritefile:
    print("Initial Location:", testwritefile.tell())

    data = testwritefile.read()
    if not data:   # string kosong = False di Python
        print('Read nothing')
    else:
        print(data)

    testwritefile.seek(0, 0)   # pindah cursor ke awal file (0 byte dari titik 0)
    print("Location after seek(0,0):", testwritefile.tell())
    data = testwritefile.read()
    if not data:
        print('Read nothing')
    else:
        print(data)
    print("Location at the end:", testwritefile.tell())

# ===== 8. Perbedaan r+ (tanpa truncate) =====
with open(exmp2, 'r+') as testwritefile:
    testwritefile.seek(0, 0)   # tulis dari awal file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    testwritefile.seek(0, 0)
    print("Tanpa truncate():")
    print(testwritefile.read())

# ===== 9. Dengan truncate() - hapus sisa data lama setelah data baru =====
with open(exmp2, 'r+') as testwritefile:
    testwritefile.seek(0, 0)
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    testwritefile.truncate()   # hapus SEMUA sisa data setelah posisi cursor saat ini
    testwritefile.seek(0, 0)
    print("Dengan truncate():")
    print(testwritefile.read())

# ===== 10. Copy file =====
with open('Example2.txt', 'r') as readfile:
    with open('Example3.txt', 'w') as writefile:
        for line in readfile:
            writefile.write(line)

with open('Example3.txt', 'r') as testwritefile:
    print(testwritefile.read())

# ===== 11. Exercise: Generate data dummy member =====
from random import randint as rnd

mem_reg = 'members.txt'
ex_reg = 'inactive.txt'
fee = ('yes', 'no')


def gen_files(current, old):
    with open(current, 'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(20):
            date = str(rnd(2015, 2020)) + '-' + str(rnd(1, 12)) + '-' + str(rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999), date, fee[rnd(0, 1)]))

    with open(old, 'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015, 2020)) + '-' + str(rnd(1, 12)) + '-' + str(rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999), date, fee[1]))


gen_files(mem_reg, ex_reg)

# ===== 12. Fungsi cleanFiles: pindahkan member tidak aktif =====
def clean_files(current_mem, ex_mem):
    with open(current_mem, 'r+') as write_file:
        with open(ex_mem, 'a+') as append_file:
            # ambil semua data
            write_file.seek(0)
            members = write_file.readlines()

            # pisahkan header
            header = members[0]
            members.pop(0)

            # cari member yang 'no' (tidak aktif)
            inactive = [member for member in members if ('no' in member)]

            # tulis ulang file current: header dulu, lalu hanya member aktif
            write_file.seek(0)
            write_file.write(header)
            for member in members:
                if member in inactive:
                    append_file.write(member)   # tidak aktif -> pindah ke file lama
                else:
                    write_file.write(member)    # aktif -> tetap di file current

            write_file.truncate()   # hapus sisa data lama yang lebih panjang


clean_files(mem_reg, ex_reg)

# ===== 13. Verifikasi hasil =====
with open(mem_reg, 'r') as read_file:
    print("Active Members:\n")
    print(read_file.read())

with open(ex_reg, 'r') as read_file:
    print("Inactive Members:\n")
    print(read_file.read())
    