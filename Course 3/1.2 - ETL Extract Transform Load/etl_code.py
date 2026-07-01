import glob  # cari file berdasarkan pola nama (*.csv, dst)
import pandas as pd  # baca & olah data tabular
import xml.etree.ElementTree as ET  # baca file XML
from datetime import datetime  # catat waktu di log

log_file = "log_file.txt"  # nama file log proses ETL
target_file = "transformed_data.csv"  # nama file hasil akhir


def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe


def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)  # tiap baris = 1 record
    return dataframe


def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=["name", "height", "weight"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:  # looping tiap data "person" di xml
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        dataframe = pd.concat(  # tambah 1 baris baru ke tabel
            [
                dataframe,
                pd.DataFrame([{"name": name, "height": height, "weight": weight}]),
            ],
            ignore_index=True,
        )
    return dataframe


def extract():
    extracted_data = pd.DataFrame(columns=["name", "height", "weight"])

    for csvfile in glob.glob("*.csv"):  # semua file .csv
        if csvfile != target_file:  # kecuali file hasil akhir
            extracted_data = pd.concat(
                [extracted_data, extract_from_csv(csvfile)], ignore_index=True
            )

    for jsonfile in glob.glob("*.json"):  # semua file .json
        extracted_data = pd.concat(
            [extracted_data, extract_from_json(jsonfile)], ignore_index=True
        )

    for xmlfile in glob.glob("*.xml"):  # semua file .xml
        extracted_data = pd.concat(
            [extracted_data, extract_from_xml(xmlfile)], ignore_index=True
        )

    return extracted_data


def transform(data):
    data["height"] = round(data.height * 0.0254, 2)  # inci -> meter
    data["weight"] = round(data.weight * 0.45359237, 2)  # pon -> kilogram
    return data


def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file)


def log_progress(message):
    timestamp_format = "%Y-%h-%d-%H:%M:%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:  # "a" = tambah baris, bukan timpa
        f.write(timestamp + "," + message + "\n")


log_progress("ETL Job Started")

log_progress("Extract phase Started")
extracted_data = extract()
log_progress("Extract phase Ended")

log_progress("Transform phase Started")
transformed_data = transform(extracted_data)
print("Transformed Data")
print(transformed_data)
log_progress("Transform phase Ended")

log_progress("Load phase Started")
load_data(target_file, transformed_data)
log_progress("Load phase Ended")

log_progress("ETL Job Ended")
