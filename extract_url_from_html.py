from bs4 import BeautifulSoup
import re

html_content = """
<tbody>
    	  <tr class="odd"><td>1</td><td class="sorting_1">SIKAP</td><td>[1043] SiKAP-PelakuUsaha</td><td>Data SiKAP Pelaku Usaha</td><td><span class="badge bg-secondary">KHUSUS</span></td><td class=" nowrap"><small><a href="https://isb.lkpp.go.id/isb-2/api/jsonujilayanan/1043/tipe/12/parameter/NPWP" class="badge bg-warning" target="preview">Pratinjau</a>&nbsp;<a href="https://isb.lkpp.go.id/isb-2/api/33ed77b1-af9c-4dcf-86f0-dc8655cfec76/json/7700/SiKAP-PelakuUsaha/tipe/12/parameter/NPWP" class="badge bg-secondary">JSON</a></small><br><small><a href="https://isb.lkpp.go.id/isb-2/api/xmlujilayanan/1043/tipe/12/parameter/NPWP" class="badge bg-warning" target="preview">Pratinjau</a>&nbsp;<a href="https://isb.lkpp.go.id/isb-2/api/33ed77b1-af9c-4dcf-86f0-dc8655cfec76/xml/7700/SiKAP-PelakuUsaha/tipe/12/parameter/NPWP" class="badge bg-secondary">XML&nbsp;</a>&nbsp;</small><br><small><a href="https://isb.lkpp.go.id/isb-2/api/csvujilayanan/1043/tipe/12/parameter/NPWP" class="badge bg-warning" target="preview">Pratinjau</a>&nbsp;<a href="https://isb.lkpp.go.id/isb-2/api/33ed77b1-af9c-4dcf-86f0-dc8655cfec76/csv/7700/SiKAP-PelakuUsaha/tipe/12/parameter/NPWP" class="badge bg-secondary">CSV&nbsp;</a>&nbsp;</small></td><td><small><a href="/isb-2/UserCtr/methodView?mtd_id=1043" class="badge bg-warning">Kamus Data</a></small></td></tr><tr class="even"><td>2</td><td class="sorting_1">SIKAP</td><td>[1053] SiKAP-NarahubungPelakuUsaha</td><td>Data SiKAP Narahubung Pelaku Usaha</td><td><span class="badge bg-secondary">KHUSUS</span></td><td class=" nowrap"><small><a href="https://isb.lkpp.go.id/isb-2/api/jsonujilayanan/1053/tipe/12/parameter/NPWP" class="badge bg-warning" target="preview">Pratinjau</a>&nbsp;<a href="https://isb.lkpp.go.id/isb-2/api/77315ef8-9863-47c5-959a-2d420fd917c8/json/7701/SiKAP-NarahubungPelakuUsaha/tipe/12/parameter/NPWP" class="badge bg-secondary">JSON</a></small><br><small><a href="https://isb.lkpp.go.id/isb-2/api/xmlujilayanan/1053/tipe/12/parameter/NPWP" class="badge bg-warning" target="preview">Pratinjau</a>&nbsp;<a href="https://isb.lkpp.go.id/isb-2/api/77315ef8-9863-47c5-959a-2d420fd917c8/xml/7701/SiKAP-NarahubungPelakuUsaha/tipe/12/parameter/NPWP" class="badge bg-secondary">XML&nbsp;</a>&nbsp;</small><br><small><a href="https://isb.lkpp.go.id/isb-2/api/csvujilayanan/1053/tipe/12/parameter/NPWP" class="badge bg-warning" target="preview">Pratinjau</a>&nbsp;<a href="https://isb.lkpp.go.id/isb-2/api/77315ef8-9863-47c5-959a-2d420fd917c8/csv/7701/SiKAP-NarahubungPelakuUsaha/tipe/12/parameter/NPWP" class="badge bg-secondary">CSV&nbsp;</a>&nbsp;</small></td><td><small><a href="/isb-2/UserCtr/methodView?mtd_id=1053" class="badge bg-warning">Kamus Data</a></small></td></tr></tbody>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Find all anchor tags with class 'badge bg-secondary' and containing the text 'JSON'
json_links = soup.find_all('a', class_='badge bg-secondary', text='JSON')

# Extract and print the JSON URLs
json_urls = [link['href'] for link in json_links]
for link in json_links:
    base_url = link['href']
    json_url_2022 = base_url.replace("2023", "2022")
    json_url_2024 = base_url.replace("2023", "2024")
    
    # Print the URLs with newline characters
    print(json_url_2022)
    print(base_url)
    print(json_url_2024)