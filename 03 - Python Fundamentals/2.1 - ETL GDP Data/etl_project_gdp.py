# Code for ETL operations on Country-GDP data

from bs4 import BeautifulSoup  # parsing HTML
import requests  # ambil halaman web
import pandas as pd  # olah data tabular
import numpy as np  # pembulatan angka
import sqlite3  # database
from datetime import datetime  # timestamp untuk log

# ==== Bagian eksekusi utama ====

url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
table_attribs = [
    "Country",
    "GDP_USD_millions",
]  # nama kolom awal, sebelum ditransformasi
db_name = "World_Economies.db"
table_name = "Countries_by_GDP"
csv_path = "./Countries_by_GDP.csv"


def extract(url, table_attribs):
    """Ekstrak data dari website, kembalikan dataframe."""
    page = requests.get(url).text
    data = BeautifulSoup(page, "html.parser")
    df = pd.DataFrame(columns=table_attribs)

    tables = data.find_all("tbody")
    rows = tables[2].find_all("tr")  # tabel yang dibutuhkan ada di index ke-2

    for row in rows:
        col = row.find_all("td")
        if len(col) != 0:
            # ambil baris kalau: kolom pertama ada link (bukan baris "World"),
            # dan kolom ketiga bukan tanda '—' (data GDP kosong)
            if col[0].find("a") is not None and "—" not in col[2]:
                data_dict = {
                    "Country": col[0].a.contents[0],
                    "GDP_USD_millions": col[2].contents[0],
                }
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df, df1], ignore_index=True)

    return df


def transform(df):
    """Ubah GDP dari Million USD ke Billion USD, dibulatkan 2 desimal."""
    GDP_list = df["GDP_USD_millions"].tolist()

    # hapus tanda koma (format currency "1,234") lalu ubah jadi angka float
    GDP_list = [float("".join(x.split(","))) for x in GDP_list]

    # ubah dari juta ke miliar (bagi 1000), bulatkan 2 desimal
    GDP_list = [np.round(x / 1000, 2) for x in GDP_list]

    df["GDP_USD_millions"] = GDP_list
    df = df.rename(columns={"GDP_USD_millions": "GDP_USD_billions"})  # ganti nama kolom
    return df


def load_to_csv(df, csv_path):
    """Simpan dataframe final ke file CSV."""
    df.to_csv(csv_path)


def load_to_db(df, sql_connection, table_name):
    """Simpan dataframe final ke tabel database."""
    df.to_sql(table_name, sql_connection, if_exists="replace", index=False)


def run_query(query_statement, sql_connection):
    """Jalankan query, print hasilnya ke terminal."""
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)


def log_progress(message):
    """Catat pesan proses ke file log."""
    timestamp_format = "%Y-%h-%d-%H:%M:%S"  # contoh: 2026-Jul-02-14:30:00
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("./etl_project_log.txt", "a") as f:  # "a" = tambah baris, bukan timpa
        f.write(timestamp + " : " + message + "\n")


# Bagian eksekusi utama (di luar semua fungsi) akan diisi di langkah terakhir

# ==== Eksekusi utama ====

log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, table_attribs)
log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df)
log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df, csv_path)
log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect('World_Economies.db')
log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)
log_progress('Data loaded to Database as table. Running the query')

query_statement = f"SELECT * from {table_name} WHERE GDP_USD_billions >= 100"
run_query(query_statement, sql_connection)

log_progress('Process Complete.')

sql_connection.close()
