import pandas as pd


def tambah_tahun_2024(df):
    # Mendapatkan daftar kode_daerah dan url_api yang perlu ditambahkan tahun 2024
    kode_daerah_url_api_tambah_tahun = df[['kode_daerah', 'url_api']].drop_duplicates()

    # Iterasi untuk setiap kombinasi kode_daerah dan url_api
    for _, row in kode_daerah_url_api_tambah_tahun.iterrows():
        kode_daerah = row['kode_daerah']
        url_api = row['url_api']

        # Memeriksa apakah sudah ada kombinasi kode_daerah, url_api, dan tahun 2024
        if df[(df['kode_daerah'] == kode_daerah) & (df['url_api'] == url_api) & (df['tahun'] == 2024)].empty:
            # Memeriksa apakah ada nilai tahun atau nilai NaN
            if not df[(df['kode_daerah'] == kode_daerah) & (df['url_api'] == url_api)]['tahun'].notna().any():
                continue  # Lanjut ke kombinasi berikutnya jika tidak ada nilai tahun

            # Menambahkan record dengan tahun 2024 untuk kombinasi kode_daerah dan url_api tertentu
            record_tambahan = {'url_api': url_api, 'tahun': 2024, 'kode_daerah': kode_daerah}
            df = df.append(record_tambahan, ignore_index=True)

    # Menghilangkan desimal .0 dari kolom tahun
    df['tahun'] = df['tahun'].astype('Int64')  # Menggunakan tipe data 'Int64' untuk mengakomodasi nilai NaN

    # Mengurutkan data berdasarkan url_api dan kode_daerah
    df = df.sort_values(by=['url_api', 'kode_daerah']).reset_index(drop=True)

    # Menghapus duplikat untuk kombinasi url_api, kode_daerah, dan tahun
    df = df.drop_duplicates(subset=['url_api', 'kode_daerah', 'tahun']).reset_index(drop=True)

    return df

if __name__ == "__main__":
    # Membaca file CSV
    df = pd.read_csv('database_epurchasing.csv')

    # Memanggil fungsi untuk menambahkan tahun 2024
    df_hasil = tambah_tahun_2024(df)

    # Menyimpan DataFrame yang telah diubah kembali ke file CSV
    df_hasil.to_csv('database_epurchasing_csv_tambahan_tahun.csv', index=False)

    # Menampilkan hasil
    print(df_hasil)
