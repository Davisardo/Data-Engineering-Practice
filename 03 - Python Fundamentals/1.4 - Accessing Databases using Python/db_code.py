import sqlite3  # database ringan bawaan Python
import pandas as pd  # olah data tabular

conn = sqlite3.connect(
    "STAFF.db"
)  # buat/koneksi ke database STAFF (otomatis dibuat kalau belum ada)

table_name = "INSTRUCTOR"
attribute_list = ["ID", "FNAME", "LNAME", "CITY", "CCODE"]  # nama kolom tabel

file_path = "INSTRUCTOR.csv"
df = pd.read_csv(
    file_path, names=attribute_list
)  # baca csv, kasih nama kolom manual (csv-nya gak ada header)

df.to_sql(
    table_name, conn, if_exists="replace", index=False
)  # simpan dataframe jadi tabel di database
print("Table is ready")

query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

data_dict = {
    'ID': [100],
    'FNAME': ['John'],
    'LNAME': ['Doe'],
    'CITY': ['Paris'],
    'CCODE': ['FR'],
}
data_append = pd.DataFrame(data_dict)                              # buat baris data baru
data_append.to_sql(table_name, conn, if_exists='append', index=False)   # tambahkan ke tabel (bukan timpa)
print('Data appended successfully')

# Cek ulang jumlah baris, harus nambah 1 dari COUNT sebelumnya
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

conn.close()   # tutup koneksi database setelah semua selesai

