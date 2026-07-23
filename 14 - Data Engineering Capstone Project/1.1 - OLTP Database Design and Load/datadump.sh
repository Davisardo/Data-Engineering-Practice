#!/bin/bash
# Script untuk export semua data dari tabel sales_data ke file SQL
mysqldump -h 172.19.16.1 -u root -p12345 sales sales_data > sales_data.sql
