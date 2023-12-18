import csv

# Fungsi untuk membaca file teks dan mengonversinya ke CSV
def txt_to_csv(input_file, output_file):
    with open(input_file, 'r') as txt_file:
        lines = txt_file.readlines()

    # Opening the CSV file for writing
    with open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Writing the header
        csv_writer.writerow(["url_api", "tahun", "kode_daerah"])

        # Writing data rows
        for line in lines:
            # Extracting year and region code from the URL
            url_parts = line.split("/")
            tahun_kode = url_parts[-1].split(":")

            # Using a ternary conditional expression to handle the IndexError
            tahun = tahun_kode[1] if len(tahun_kode) > 1 else ""
            kode_daerah = tahun_kode[0] if len(tahun_kode) > 0 else ""

            # Checking if the last part starts with "20" to determine if it's a year or code
            if kode_daerah.startswith("20"):
                # If it doesn't start with "20", swap the values
                tahun, kode_daerah = kode_daerah, tahun

            # Removing year and region code from the URL
            url_api = '/'.join(url_parts[:-1])

            # Writing data to CSV
            csv_writer.writerow([url_api.strip(), tahun, kode_daerah])

# Memanggil fungsi untuk mengonversi file txt ke csv
txt_to_csv('generated_urls_epurchasing.txt', 'database_epurchasing.csv')
