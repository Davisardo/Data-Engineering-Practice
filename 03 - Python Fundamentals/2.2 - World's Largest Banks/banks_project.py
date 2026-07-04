# Code for ETL operations on World's Largest Banks data

import requests  # ambil halaman web
from bs4 import BeautifulSoup  # parsing HTML
import pandas as pd  # olah data tabular
import numpy as np  # pembulatan angka
import sqlite3  # database
from datetime import datetime  # timestamp untuk log


def log_progress(message):
    """Catat pesan proses ke file log."""
    timestamp_format = "%Y-%h-%d-%H:%M:%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("./code_log.txt", "a") as f:  # "a" = tambah baris, bukan timpa
        f.write(timestamp + " : " + message + "\n")

def extract(url, table_attribs):
    ''' Ekstrak data dari website, kembalikan dataframe. '''
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    df = pd.DataFrame(columns=table_attribs)

    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')          # tabel "By market capitalization" ada di index 0

    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            # kolom kedua (index 1) berisi 2 link: flag negara & nama bank -> ambil link ke-2
            a_tags = col[1].find_all('a')
            if len(a_tags) > 1:
                bank_name = a_tags[1].text
                market_cap = float(col[2].contents[0][:-1])   # hapus karakter terakhir ('\n'), ubah ke float
                data_dict = {"Name": bank_name, "MC_USD_Billion": market_cap}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df, df1], ignore_index=True)

    return df

def transform(df, csv_path):
    """Tambahkan kolom Market Cap dalam GBP, EUR, INR berdasarkan kurs di csv_path."""
    exchange_rate_df = pd.read_csv(csv_path)
    exchange_rate = exchange_rate_df.set_index('Currency').to_dict()['Rate']   # ubah jadi dict: {'EUR': 0.93, ...}

    df['MC_GBP_Billion'] = [np.round(x * exchange_rate['GBP'], 2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x * exchange_rate['EUR'], 2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x * exchange_rate['INR'], 2) for x in df['MC_USD_Billion']]

    return df

def load_to_csv(df, output_path):
    """Simpan dataframe final ke file CSV."""
    df.to_csv(output_path)


def load_to_db(df, sql_connection, table_name):
    """Simpan dataframe final ke tabel database."""
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)


def run_query(query_statement, sql_connection):
    """Jalankan query, print hasilnya ke terminal."""
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)


url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attribs = ["Name", "MC_USD_Billion"]  # kolom awal saat ekstraksi
output_csv_path = "./Largest_banks_data.csv"
db_name = "Banks.db"
table_name = "Largest_banks"
csv_path = "./exchange_rate.csv"  # file kurs mata uang

# Bagian pemanggilan fungsi akan diisi di langkah terakhir

log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, table_attribs)
log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df, csv_path)
log_progress('Data transformation complete. Initiating Loading process')

load_to_csv(df, output_csv_path)
log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect(db_name)
log_progress('SQL Connection initiated')

load_to_db(df, sql_connection, table_name)
log_progress('Data loaded to Database as a table, Executing queries')

run_query("SELECT * FROM Largest_banks", sql_connection)
run_query("SELECT AVG(MC_GBP_Billion) FROM Largest_banks", sql_connection)
run_query("SELECT Name FROM Largest_banks LIMIT 5", sql_connection)

log_progress('Process Complete')

sql_connection.close()
log_progress('Server Connection closed')