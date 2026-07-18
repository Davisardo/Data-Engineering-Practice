from datetime import timedelta, datetime  # untuk atur retry_delay dan start_date
from airflow import DAG  # class utama buat definisikan DAG
from airflow.operators.bash import (
    BashOperator,
)  # operator yang jalanin perintah shell/bash

default_args = {
    "owner": "Davis Ardo",  # nama pemilik DAG (bebas, ini identitas doang)
    "start_date": datetime(2024, 1, 1),  # tanggal mulai DAG dianggap aktif
    "email": ["davisardo6@gmail.com"],  # email tujuan notifikasi (dummy juga oke)
    "email_on_failure": True,  # kirim email kalau task gagal
    "email_on_retry": True,  # kirim email tiap kali retry
    "retries": 1,  # jumlah percobaan ulang kalau gagal
    "retry_delay": timedelta(minutes=5),  # jeda sebelum retry
}


dag = DAG(
    dag_id="ETL_toll_data",  # ID unik DAG, ini yang muncul di UI Airflow
    schedule_interval=timedelta(days=1),  # jalan otomatis sekali sehari
    default_args=default_args,  # pakai argumen yang sudah kita definisikan tadi
    description="Apache Airflow Final Assignment",  # deskripsi singkat DAG
    catchup=False,  # jangan jalankan run yang "terlewat" dari masa lalu, cuma run terbaru aja
)


unzip_data = BashOperator(
    task_id="unzip_data",  # ID unik task ini
    bash_command="tar -xzf /opt/airflow/dags/tolldata.tgz -C /opt/airflow/dags/staging/",  # extract tgz ke folder staging
    dag=dag,  # daftarkan task ini ke DAG yang sudah kita buat
)

extract_data_from_csv = BashOperator(
    task_id="extract_data_from_csv",  # ID unik task ini
    bash_command='cut -d"," -f1-4 /opt/airflow/dags/staging/vehicle-data.csv > /opt/airflow/dags/staging/csv_data.csv',  # ambil kolom 1-4 dipisah koma
    dag=dag,
)


extract_data_from_tsv = BashOperator(
    task_id="extract_data_from_tsv",  # ID unik task ini
    bash_command='cut -f5-7 /opt/airflow/dags/staging/tollplaza-data.tsv | tr -d "\\r" | tr "\\t" "," > /opt/airflow/dags/staging/tsv_data.csv',  # ambil field 5-7, buang CR Windows, ubah tab jadi koma  # ambil field 5-7, ubah tab jadi koma
    dag=dag,
)

extract_data_from_fixed_width = BashOperator(
    task_id="extract_data_from_fixed_width",  # ID unik task ini
    bash_command='cut -c59-67 /opt/airflow/dags/staging/payment-data.txt | tr -s " " "," > /opt/airflow/dags/staging/fixed_width_data.csv',  # ambil rentang utuh (termasuk spasi pemisah), spasi jadi koma  # ambil posisi karakter tertentu, spasi jadi koma
    dag=dag,
)

consolidate_data = BashOperator(
    task_id="consolidate_data",  # ID unik task ini
    bash_command='paste -d"," /opt/airflow/dags/staging/csv_data.csv /opt/airflow/dags/staging/tsv_data.csv /opt/airflow/dags/staging/fixed_width_data.csv > /opt/airflow/dags/staging/extracted_data.csv',  # gabung 3 file jadi 1, kolom disambung koma
    dag=dag,
)

transform_data = BashOperator(
    task_id="transform_data",  # ID unik task ini
    bash_command='awk -F"," \'BEGIN{OFS=","} {$4=toupper($4); print}\' /opt/airflow/dags/staging/extracted_data.csv > /opt/airflow/dags/staging/transformed_data.csv',  # ubah kolom 4 (vehicle_type) jadi kapital
    dag=dag,
)


(
    unzip_data
    >> extract_data_from_csv
    >> extract_data_from_tsv
    >> extract_data_from_fixed_width
    >> consolidate_data
    >> transform_data
)
