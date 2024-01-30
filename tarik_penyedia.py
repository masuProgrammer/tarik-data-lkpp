import os
import pandas as pd
import requests

# Mendapatkan daftar folder di dalam data_api yang berawalan huruf "D"
data_api_path = "data_api"
daerah_folders = [folder for folder in os.listdir(data_api_path) if folder.startswith("D")]

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

def cek_dan_perbarui_penyedia(kode_daerah, kd_penyedia):
    data_api_path = "data_api"
    daerah_folder = kode_daerah
    file_path = os.path.join(data_api_path, daerah_folder, "epurchasing", "ECATPenyediaDetail2024.parquet")
    try:
        # Cek apakah file parquet sudah ada
        if os.path.exists(file_path):
            # Jika sudah ada, baca data
            data_penyedia = pd.read_parquet(file_path)
            
            # Cek apakah kd_penyedia sudah ada di data
            if kd_penyedia in data_penyedia['kd_penyedia'].values:
                print(f"Data penyedia {kd_penyedia} sudah ada di {file_path}.")
                return
        else:
            # Jika file belum ada, buat DataFrame baru
            data_penyedia = pd.DataFrame(columns=['kd_penyedia', 'kolom_lain'])

        # Jika kd_penyedia belum ada, panggil API
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        url = f"https://isb.lkpp.go.id/isb-2/api/93c2af98-02e3-483c-b597-e0a790004e90/json/3328/Ecat-PenyediaDetail/tipe/4/parameter/{kd_penyedia}"
        response = requests.get(url,headers=headers)
        
        if response.status_code == 200:
            # Ambil data dari API
            new_data = response.json()
            
            # Tambahkan data baru ke DataFrame
            data_penyedia = data_penyedia.append(new_data, ignore_index=True)
            
            # Simpan DataFrame ke file parquet
            data_penyedia.to_parquet(file_path, index=False)
            
            # send_telegram_message(f"Data penyedia {kd_penyedia} berhasil ditambahkan ke {file_path}.")
        else:
            send_telegram_message(f"Gagal mengambil data dari API untuk {kd_penyedia}. Status code: {response.status_code}")

    except Exception as e:
        send_telegram_message(f"Terjadi kesalahan: {e}")

# Fungsi untuk membaca data purchasing dan mengambil kd_penyedia
def ambil_kd_penyedia(kode_daerah):
    file_path = os.path.join(data_api_path, kode_daerah, "epurchasing", "Ecat-PaketEPurchasing2023.parquet")
    try:
        data_purchasing = pd.read_parquet(file_path)
        kd_penyedia_unik = data_purchasing['kd_penyedia'].unique()
        return kd_penyedia_unik
    except FileNotFoundError:
        send_telegram_message(f"File not found for daerah {kode_daerah}")
        return None
    except Exception as e:
        send_telegram_message(f"Error reading data for daerah {kode_daerah}: {e}")
        return None

# Array untuk menyimpan kd_penyedia unik dari setiap daerah
all_kd_penyedia = []

# Loop untuk membaca kd_penyedia dari masing-masing daerah
for daerah in daerah_folders:
    kd_penyedia_daerah = ambil_kd_penyedia(daerah)
    
    # Mengumpulkan kd_penyedia dalam array all_kd_penyedia
    if kd_penyedia_daerah is not None:
        for kd_penyedia in kd_penyedia_daerah:
            cek_dan_perbarui_penyedia(daerah, kd_penyedia)
        # Setelah menjalankan cek_dan_perbarui_penyedia, konversi parquet ke Excel
        file_path_parquet = os.path.join(data_api_path, daerah, "epurchasing", "ECATPenyediaDetail2024.parquet")
        file_path_excel = os.path.join(data_api_path, daerah, "epurchasing", "ECATPenyediaDetail2024.xlsx")
        
        try:
            # Baca data dari parquet
            data_penyedia = pd.read_parquet(file_path_parquet)

            # Simpan data ke Excel
            data_penyedia.to_excel(file_path_excel, index=False)
            
            send_telegram_message(f"File {file_path_excel} berhasil dibuat.")
            
        except Exception as e:
            send_telegram_message(f"Terjadi kesalahan saat konversi ke Excel: {e}")