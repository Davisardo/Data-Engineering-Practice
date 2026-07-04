import requests  # ambil konten dari halaman web
import sqlite3  # simpan data ke database
import pandas as pd  # olah data tabular
from bs4 import BeautifulSoup  # parsing HTML

url = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"
db_name = "Movies.db"
table_name = "Top_50"
csv_path = "top_50_films.csv"
df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])  # tabel kosong dulu
count = 0  # penghitung, biar cuma ambil 50 data teratas

html_page = requests.get(url).text  # ambil isi halaman web (raw HTML)
data = BeautifulSoup(
    html_page, "html.parser"
)  # parsing HTML biar bisa "dibaca" pythonnya

tables = data.find_all("tbody")  # ambil semua tabel di halaman
rows = tables[0].find_all("tr")  # ambil baris dari tabel pertama

for row in rows:
    if count < 50:  # batasi cuma 50 data teratas
        col = row.find_all("td")
        if len(col) != 0:  # skip baris kosong/gabungan
            data_dict = {
                "Average Rank": col[0].contents[0],
                "Film": col[1].contents[0],
                "Year": col[2].contents[0],
            }
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)  # tambah ke tabel utama
            count += 1
    else:
        break

print(df)

df.to_csv(csv_path)                  # simpan ke file csv

conn = sqlite3.connect(db_name)      # buka koneksi ke database (dibuat otomatis kalau belum ada)
df.to_sql(table_name, conn, if_exists='replace', index=False)   # simpan tabel ke database
conn.close()                         # tutup koneksi
