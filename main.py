import requests
import json
from urllib.parse import urlparse
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
    nama_api = path_components[-2]  # Mengambil komponen sebelum terakhir

    # Membuat tahun_kode_daerah dari parameter
    tahun_kode_daerah = f"{tahun}:{kode_daerah}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }

    try:
        response = requests.get(f"{url_api}/{tahun_kode_daerah}", headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad requests (4xx and 5xx status codes)
        data = response.json()
        # Membuat direktori folder output jika belum ada
        folder_output = "data_api"
        if not os.path.exists(folder_output):
            os.makedirs(folder_output)

         # Penamaan file berdasarkan tahun, kode daerah, dan nama API
        nama_file = f"{folder_output}/{kode_daerah}_{tahun}_{nama_api}_output.json"

        with open(nama_file, 'w') as file:
            json.dump(data, file, indent=2)

        print(f"Data telah disimpan dalam file {nama_file}")
        return data
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
    if data_api:
        # Contoh: print data API
        print(json.dumps(data_api, indent=2))