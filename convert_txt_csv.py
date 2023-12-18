import csv

# Fungsi untuk membaca file teks dan mengonversinya ke CSV
def txt_to_csv(input_file, output_file):
    with open(input_file, 'r') as txt_file:
        lines = txt_file.readlines()

    # Membuka file CSV untuk penulisan
    with open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Menulis header
        csv_writer.writerow(["url_api", "tahun", "kode_daerah"])

        # Menulis baris-baris data
        for line in lines:
            # Mengambil tahun dan kode daerah dari URL
            url_parts = line.split("/")
            tahun_kode = url_parts[-1].split(":")
            tahun = tahun_kode[0]
            kode_daerah = tahun_kode[1]

            # Menghilangkan tahun dan kode daerah dari URL
            url_api = '/'.join(url_parts[:-1])

            # Menulis data ke CSV
            csv_writer.writerow([url_api.strip(), tahun, kode_daerah])

# Memanggil fungsi untuk mengonversi file txt ke csv
txt_to_csv('generated_urls.txt', 'database.csv')
