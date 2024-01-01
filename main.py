import os
import json
import requests
from urllib.parse import urlparse
import pandas as pd
import csv
from datetime import datetime

def baca_csv(nama_file):
    data = []
    with open(nama_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def send_telegram_message(message):
    telegram_api_url = f"https://api.telegram.org/bot6748527081:AAEgO61QqaMXTIi87UZ4uGff9WiW-o2FEVg/sendMessage"
    
    params = {
        'chat_id': '-4060257273',
        'text': message
    }
    
    response = requests.get(telegram_api_url, params=params)
    
    if response.status_code == 200:
        print(f"Pesan berhasil dikirim")
    else:
        print(f"Terjadi kesalahan saat mengirim pesan: {response.status_code}")

def panggil_api_dan_simpan(url_api, tahun, kode_daerah,jenis_api):
    # Parsing URL untuk mendapatkan nama API
    parsed_url = urlparse(url_api)
    path_components = parsed_url.path.split('/')
    nama_api = path_components[-4]  # Mengambil komponen sebelum terakhir
    kode_daerah = kode_daerah.replace("\n", "")
    # Membuat tahun_kode_daerah dari parameter
    if nama_api == 'RUP-MasterSatker':
        tahun_kode_daerah = f"{kode_daerah}:{tahun}"
    elif nama_api == 'Ecat-InstansiSatker':
        tahun_kode_daerah = f"{kode_daerah}"
    elif nama_api == 'Bela-TokoDaringRealisasi':
        tahun_kode_daerah = f"{kode_daerah}:{tahun}"
    else:
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

        # if nama_api == 'RUP-MasterSatker':
        #     tahun, kode_daerah = kode_daerah, tahun

        # Penamaan file berdasarkan tahun, kode daerah, dan nama API
        nama_folder = f"{folder_output}/{kode_daerah}/{jenis_api}"
        if not os.path.exists(nama_folder):
            os.makedirs(nama_folder)

        nama_file_xlsx = f"{nama_folder}/{nama_api}{tahun}.xlsx"
        nama_file_parquet = f"{nama_folder}/{nama_api}{tahun}.parquet"
        nama_file_xlsx = nama_file_xlsx.replace("\n", "")
        nama_file_parquet = nama_file_parquet.replace("\n", "")
        

        # Convert data to DataFrame
        df = pd.DataFrame(data)

        # Save DataFrame to Excel
        df.to_excel(nama_file_xlsx, index=False)
        print(f"Data telah disimpan dalam file Excel: {nama_file_xlsx}")

        # Save DataFrame to Parquet
        df.to_parquet(nama_file_parquet, index=False)
        print(f"Data telah disimpan dalam file Parquet: {nama_file_parquet}")


        print('nama_api',nama_api)
        print('tahun',tahun)
        print("datetime.now().year",datetime.now().year)
        if nama_api in ['RUP-StrukturAnggaranPD', 'RUP-PaketPenyedia-Terumumkan', 'RUP-PaketSwakelola-Terumumkan']:
            print("if nama_api in ['RUP-StrukturAnggaranPD', 'RUP-PaketPenyedia-Terumumkan', 'RUP-PaketSwakelola-Terumumkan']",True)
        if nama_api in ['RUP-StrukturAnggaranPD', 'RUP-PaketPenyedia-Terumumkan', 'RUP-PaketSwakelola-Terumumkan'] and tahun == str(datetime.now().year):
            print("Simpan data berjalan")
            bulan = datetime.now().strftime('%m')
            tanggal = datetime.now().strftime('%d')
            nama_file_xlsx = f"{nama_folder}/{nama_api}-{tahun}-{bulan}-{tanggal}.xlsx"
            nama_file_parquet = f"{nama_folder}/{nama_api}-{tahun}-{bulan}-{tanggal}.parquet"
            nama_file_xlsx = nama_file_xlsx.replace("\n", "")
            nama_file_parquet = nama_file_parquet.replace("\n", "")
            

            # Convert data to DataFrame
            df = pd.DataFrame(data)

            # Save DataFrame to Excel
            df.to_excel(nama_file_xlsx, index=False)
            print(f"Data telah disimpan dalam file Excel: {nama_file_xlsx}")

            # Save DataFrame to Parquet
            df.to_parquet(nama_file_parquet, index=False)
            print(f"Data telah disimpan dalam file Parquet: {nama_file_parquet}")



        return df
    except requests.exceptions.RequestException as e:
        url = f"{url_api}/{tahun_kode_daerah}"
        error_message = f"Error saat memanggil API: {url}"
        print(error_message)
        send_telegram_message(error_message)

        return None

    except json.JSONDecodeError as json_error:
        # Handle JSON decoding error
        url = f"{url_api}/{tahun_kode_daerah}"
        error_message = f"Error URL:{url}\nError decoding JSON: {json_error}. Response text: {response.text}"
        print(error_message)
        send_telegram_message(error_message)

        return None


def tarik_data(file,jenis_api):
    # Contoh membaca CSV
    nama_file_csv = file
    data_csv = baca_csv(nama_file_csv)

    # Contoh pemanggilan API untuk setiap baris dalam CSV
    for row in data_csv:
        url_api = row['url_api']
        tahun = row['tahun']
        kode_daerah = row['kode_daerah']

        data_api = panggil_api_dan_simpan(url_api, tahun, kode_daerah,jenis_api)

        # Lakukan hal lain dengan data API jika diperlukan
        # if data_api:
        #     # Contoh: print data API
        #     # print(json.dumps(data_api, indent=2))

tarik_data("database.csv","sirup")
tarik_data("database_spse.csv","spse")
tarik_data("database_epurchasing.csv","epurchasing")
tarik_data("database_sikap.csv","sikap")