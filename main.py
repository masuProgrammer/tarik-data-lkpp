import os
import json
import requests
from urllib.parse import urlparse
import pandas as pd
import csv

def baca_csv(nama_file):
    data = []
    with open(nama_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def panggil_api_dan_simpan(url_api, tahun, kode_daerah):
    # Parsing URL untuk mendapatkan nama API
    parsed_url = urlparse(url_api)
    path_components = parsed_url.path.split('/')
    nama_api = path_components[-4]  # Mengambil komponen sebelum terakhir
    kode_daerah = kode_daerah.replace("\n", "")
    # Membuat tahun_kode_daerah dari parameter
    tahun_kode_daerah = f"{tahun}:{kode_daerah}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        url = f"{url_api}/{tahun_kode_daerah}"
        # Menghapus karakter newline ("\n") dari URL
        url = url.replace("\n", "")
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad requests (4xx and 5xx status codes)
        # Print various attributes of the response
        print(f"mengakses url {url}")
        data = response.json()

        # Membuat direktori folder output jika belum ada
        folder_output = "data_api"
        if not os.path.exists(folder_output):
            os.makedirs(folder_output)

        # Penamaan file berdasarkan tahun, kode daerah, dan nama API
        nama_folder = f"{folder_output}/{kode_daerah}/sirup"
        if not os.path.exists(nama_folder):
            os.makedirs(nama_folder)

        nama_file = f"{nama_folder}/{nama_api}{tahun}.xlsx"

        # Convert data to DataFrame
        df = pd.DataFrame(data)

        # Save DataFrame to Excel
        df.to_excel(nama_file, index=False, encoding='utf-8')

        print(f"Data telah disimpan dalam file {nama_file}")
        return df
    except requests.exceptions.RequestException as e:
        print(f"Error saat memanggil API: {e}")
        return None

# Contoh membaca CSV
nama_file_csv = "database.csv"
data_csv = baca_csv(nama_file_csv)

# Contoh pemanggilan API untuk setiap baris dalam CSV
for row in data_csv:
    url_api = row['url_api']
    tahun = row['tahun']
    kode_daerah = row['kode_daerah']

    data_api = panggil_api_dan_simpan(url_api, tahun, kode_daerah)

    # Lakukan hal lain dengan data API jika diperlukan
    # if data_api:
    #     # Contoh: print data API
    #     # print(json.dumps(data_api, indent=2))