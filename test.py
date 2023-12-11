import requests

url = "https://isb.lkpp.go.id/isb-2/api/d5c9a703-07bb-4e87-8e08-ff04b23741b9/json/3325/RUP-SubKegiatanMaster/tipe/4:12/parameter/2022:D197"
response = requests.get(url)
print(f"mengakses url {url}")
response.raise_for_status()  # Raise an HTTPError for bad requests (4xx and 5xx status codes)
print(response.text)